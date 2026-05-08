# Getting Started

This page walks you from a fresh project to a first contract call.

## Installation

```sh
yarn add @nolus/nolusjs
```

or

```sh
npm install @nolus/nolusjs
```

## Prerequisites

- **Node.js ≥ 16** (the package itself targets Node 22 in its `engines` field, but the runtime works on 16+).
- **Access to a Nolus RPC node.** Pirin (mainnet) RPC: `https://rpc.nolus.network`. Rila (testnet) RPC is documented in the protocol section.
- **Contract addresses** for the Nolus CosmWasm contracts you want to talk to: `Leaser`, `Lease`, `Lpp`, `Oracle`, `Treasury`. These are returned by the on-chain `Admin` registry — you don't need to hard-code them.
- Working knowledge of [**CosmJS**](https://github.com/cosmos/cosmjs) and the [**Cosmos SDK**](https://github.com/cosmos/cosmos-sdk). nolus.js builds on top of CosmJS rather than replacing it; you'll see CosmJS types (`OfflineSigner`, `StdFee`, `Coin`) in many of the signatures.

> Your environment must support ES Modules and TypeScript. Tools like `tsx`, Vite, or Babel work out of the box.

## Connecting the client

The `NolusClient` is the entry point for every chain interaction. Set the singleton instance once at startup; every other call reads from it.

```ts
import { NolusClient } from "@nolus/nolusjs";

NolusClient.setInstance("https://rpc.nolus.network");

const cosm = await NolusClient.getInstance().getCosmWasmClient();
```

`cosm` is a CosmJS `CosmWasmClient` — pass it into any of the contract wrappers below.

## Setting up a wallet

The wallet flow uses CosmJS's `DirectSecp256k1Wallet` under the hood, with Nolus-specific helpers for mnemonic generation and bech32 address formatting.

```ts
import { makeCosmoshubPath } from "@cosmjs/amino";
import { DirectSecp256k1Wallet } from "@cosmjs/proto-signing";
import {
  ChainConstants,
  KeyUtils,
  nolusOfflineSigner,
} from "@nolus/nolusjs";

const mnemonic = KeyUtils.generateMnemonic();
const path = makeCosmoshubPath(0);
const privateKey = await KeyUtils.getPrivateKeyFromMnemonic(mnemonic, path);

const offlineSigner = await DirectSecp256k1Wallet.fromKey(
  privateKey,
  ChainConstants.BECH32_PREFIX_ACC_ADDR,
);

const nolusWallet = await nolusOfflineSigner(offlineSigner);
nolusWallet.useAccount();
```

The returned `nolusWallet` is what every state-changing contract method expects as its first argument.

## Talking to contracts

Each Nolus CosmWasm contract has a typed wrapper class under the `NolusContracts` namespace. Instantiate one per address:

```ts
import { NolusClient, NolusContracts } from "@nolus/nolusjs";

NolusClient.setInstance("https://rpc.nolus.network");
const cosm = await NolusClient.getInstance().getCosmWasmClient();

// EMA price oracle
const oracle = new NolusContracts.Oracle(cosm, oracleContractAddress);
// Factory contract that opens new leverage positions
const leaser = new NolusContracts.Leaser(cosm, leaserContractAddress);
// One isolated margin position
const lease = new NolusContracts.Lease(cosm, leaseContractAddress);
// Single-sided lending pool
const lpp = new NolusContracts.Lpp(cosm, lppContractAddress);
// Protocol revenue manager (NLS)
const treasury = new NolusContracts.Treasury(cosm, treasuryContractAddress);
```

### Reading state

Read calls don't need a wallet — they only need the `cosm` client passed at construction time:

```ts
const config = await leaser.getConfig();

const quote = await leaser.leaseQuote(
  "1000",   // downpayment amount, in the minimal denom of the downpayment currency
  "unls",   // downpayment currency ticker
  "OSMO",   // wanted lease currency
);
```

### Writing state

State-changing calls take the wallet, a fee, and the call-specific arguments:

```ts
import { ChainConstants } from "@nolus/nolusjs";

const fee = {
  gas: "1000000",
  amount: [
    { amount: "50000", denom: ChainConstants.COIN_MINIMAL_DENOM },
  ],
};

// Resolve the IBC denom for the downpayment currency.
const currencies = await oracle.getCurrencies();
const bankSymbol = AssetUtils.findBankSymbolByTicker(currencies, "unls");

await leaser.openLease(
  borrowerWallet,
  "OSMO",                                       // wantedLeaseCurrency
  fee,
  [{ denom: bankSymbol, amount: "1000" }],      // downpayment
);
```

## Utilities and constants

`ChainConstants` and `KeyUtils` are exposed at the package root for direct use:

```ts
import { ChainConstants, KeyUtils } from "@nolus/nolusjs";

ChainConstants.COIN_TYPE;
ChainConstants.COIN_MINIMAL_DENOM;

const privateKey = await KeyUtils.getPrivateKeyFromMnemonic(mnemonic, path);
```

## Where to go next

- For a complete list of every method on every contract, head to **[API Reference](reference/README.md)**.
- To wire an AI agent up to Nolus, see **[MCP Server](mcp-server.md)**.
- For the protocol concepts behind these calls (leverage model, liquidation engine, oracle), see the **Protocol Documentation** section in the sidebar.
