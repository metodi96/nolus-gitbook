[**@nolus/nolusjs**](../../../../README.md)

***

[@nolus/nolusjs](../../../../README.md) / [NolusContracts](../README.md) / Lpp

# Class: Lpp

Defined in: [src/contracts/clients/Lpp.ts:41](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L41)

The Liquidity Provider Pool (LPP) is a smart contract responsible for managing lending and borrowing activity within a specific currency on the Nolus Protocol.
Key characteristics:
- One LPP instance per currency (e.g. USDC, ATOM), handling both deposits and borrow requests in that asset.
- Accepts single-sided deposits from users (no LP token pairing required).
- Issues loans for opening margin positions via the Leaser module.
- Accumulates interest from borrowers and periodically receives rewards from the Treasury contract.

Usage:

```ts
import { NolusClient, NolusContracts } from '@nolus/nolusjs';

const cosm = await NolusClient.getInstance().getCosmWasmClient();
lppInstance = new NolusContracts.Lpp(cosm, lppContractAddress);
```

There are also methods for simulating contract operations in order to obtain preliminary information about the transaction.

## Constructors

### Constructor

> **new Lpp**(`cosmWasmClient`, `contractAddress`): `Lpp`

Defined in: [src/contracts/clients/Lpp.ts:45](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L45)

#### Parameters

##### cosmWasmClient

`CosmWasmClient`

##### contractAddress

`string`

#### Returns

`Lpp`

## Methods

### burnDeposit()

> **burnDeposit**(`nolusWallet`, `burnAmount`, `fee`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Lpp.ts:260](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L260)

Executes a withdrawal from the LPP by burning nLPN receipt tokens.

The user receives back the equivalent amount of LPN based on the current receipt price.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The user's wallet instance.

##### burnAmount

`string`

The amount of nLPN to burn (in micro-units).

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### fundCoin?

`Coin`[]

Optional. Additional coins to fund the transaction.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to:
- The execution result including gas used, transaction hash, and events.

***

### claimRewards()

> **claimRewards**(`nolusWallet`, `recipientAddress`, `fee`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Lpp.ts:171](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L171)

Executes a transaction to claim any accumulated NLS incentive rewards.

The rewards can be claimed to the user's own address or to another recipient.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The user's wallet instance.

##### recipientAddress

`string` \| `undefined`

Optional. The address to send the claimed NLS rewards to.

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### fundCoin?

`Coin`[]

Optional. Additional coins for funding the fee.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to:
- The execution result including gas used, transaction hash, and events.

***

### deposit()

> **deposit**(`nolusWallet`, `fee`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Lpp.ts:201](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L201)

Executes a deposit into the LPP using the native asset (LPN).

The user receives nLPN receipt tokens in return, representing their share in the pool.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The user's wallet instance.

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### fundCoin?

`Coin`[]

The amount and denomination of LPN to deposit.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to:
- The execution result including gas used, transaction hash, and events.

***

### distributeRewards()

> **distributeRewards**(`nolusWallet`, `fee`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Lpp.ts:230](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L230)

Executes a transaction that distributes NLS incentives into the LPP reward pool.

This function is typically called by authorized entities (e.g. Treasury).

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet instance executing the distribution.

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### fundCoin?

`Coin`[]

The amount of NLS to distribute.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to:
- The execution result including gas used, transaction hash, and events.

***

### getDepositCapacity()

> **getDepositCapacity**(): `Promise`\<[`DepositCapacity`](../interfaces/DepositCapacity.md) \| `null`\>

Defined in: [src/contracts/clients/Lpp.ts:96](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L96)

Retrieves the remaining deposit capacity for the LPP based on a minimum utilization threshold parameter defined.

#### Returns

`Promise`\<[`DepositCapacity`](../interfaces/DepositCapacity.md) \| `null`\>

A `Promise` resolving to:
- The available amount that can still be deposited into the pool.

***

### getLenderDeposit()

> **getLenderDeposit**(`lenderAddress`): `Promise`\<[`Asset`](../interfaces/Asset.md)\>

Defined in: [src/contracts/clients/Lpp.ts:154](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L154)

Retrieves the current deposit balance for a specific lender, expressed in receipt tokens (`nLPN`).

#### Parameters

##### lenderAddress

`string`

The bech32 wallet address of the lender.

#### Returns

`Promise`\<[`Asset`](../interfaces/Asset.md)\>

A `Promise` resolving to:
- The lender’s deposit amount in `nLPN` (as a string in micro-units).

***

### getLenderRewards()

> **getLenderRewards**(`lenderAddress`): `Promise`\<[`Rewards`](../interfaces/Rewards.md)\>

Defined in: [src/contracts/clients/Lpp.ts:142](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L142)

Retrieves the additional incentive rewards (in NLS) accumulated by a specific lender.

#### Parameters

##### lenderAddress

`string`

The bech32 wallet address of the lender.

#### Returns

`Promise`\<[`Rewards`](../interfaces/Rewards.md)\>

A `Promise` resolving to:
- The amount of claimable rewards in NLS (as a string in micro-units).

***

### getLoanInformation()

> **getLoanInformation**(`leaseAddress`): `Promise`\<[`LoanInfo`](../interfaces/LoanInfo.md)\>

Defined in: [src/contracts/clients/Lpp.ts:60](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L60)

Retrieves loan details for a given margin position (lease) contract.

#### Parameters

##### leaseAddress

`string`

The address of the lease (margin position) contract.

#### Returns

`Promise`\<[`LoanInfo`](../interfaces/LoanInfo.md)\>

A `Promise` resolving to a `LoanInfo` object containing the loan state.
The returned data includes:
- Outstanding principal amount still owed by the position.
- The fixed annual interest rate for the loan (in permilles).
- The latest interest settlement date in unix

***

### getLPN()

> **getLPN**(): `Promise`\<`string`\>

Defined in: [src/contracts/clients/Lpp.ts:119](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L119)

Retrieves the native asset (LPN) used by this LPP instance.

#### Returns

`Promise`\<`string`\>

A `Promise` resolving to:
- The ticker of the pool's native asset (e.g. "USDC_NOBLE").

***

### getLppBalance()

> **getLppBalance**(): `Promise`\<[`LppBalance`](../interfaces/LppBalance.md)\>

Defined in: [src/contracts/clients/Lpp.ts:73](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L73)

Retrieves the current liquidity and debt statistics of the LPP.

#### Returns

`Promise`\<[`LppBalance`](../interfaces/LppBalance.md)\>

A `Promise` resolving to an object containing:
- Available pool balance (unloaned funds).
- Total borrowed principal across all active loans for the corresponding market.
- Accrued interest owed by all borrowers.
- Total amount of receipt tokens (`nlpn`) issued to depositors.

***

### getLppConfig()

> **getLppConfig**(): `Promise`\<[`LppConfig`](../interfaces/LppConfig.md)\>

Defined in: [src/contracts/clients/Lpp.ts:109](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L109)

Retrieves the configuration parameters of the LPP, including the borrow rate model.

#### Returns

`Promise`\<[`LppConfig`](../interfaces/LppConfig.md)\>

A `Promise` resolving to:
- The base interest rate in permilles.
- The optimal utilization threshold in permilles.
- The interest rate slope (add-on interest rate).
- The minimum utilization threshold in permilles, below which new deposits are disallowed.

***

### getPrice()

> **getPrice**(): `Promise`\<[`Price`](../interfaces/Price.md)\>

Defined in: [src/contracts/clients/Lpp.ts:130](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L130)

Retrieves the current price of the receipt token (`nLPN`) relative to the pool's native asset.

#### Returns

`Promise`\<[`Price`](../interfaces/Price.md)\>

A `Promise` resolving to:
- The current pool asset amount backing the total issued nLPN tokens.
- The equivalent value in stablecoin terms.

***

### getStableBalance()

> **getStableBalance**(`oracleAddress`): `Promise`\<`number`\>

Defined in: [src/contracts/clients/Lpp.ts:86](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L86)

Retrieves the total LPP balance (available funds + borrowed principal + interest due),
priced into a stablecoin equivalent using the given oracle.

#### Parameters

##### oracleAddress

`string`

The address of the price oracle contract.

#### Returns

`Promise`\<`number`\>

A `Promise` resolving to:
- The total pool value expressed as the sum of available liquidity, borrowed liquidity and interest owed in stablecoin units (as a number).

***

### simulateBurnDepositTx()

> **simulateBurnDepositTx**(`nolusWallet`, `burnAmount`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Lpp.ts:274](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L274)

Simulates a withdrawal from the LPP by burning nLPN receipt tokens.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The user's wallet instance.

##### burnAmount

`string`

The simulated amount of nLPN to burn.

##### fundCoin?

`Coin`[]

Optional. Coins to simulate as the fee source.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to:
- The simulated transaction result including gas estimate and fee.

***

### simulateClaimRewardsTx()

> **simulateClaimRewardsTx**(`nolusWallet`, `recipientAddress`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Lpp.ts:185](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L185)

Simulates the transaction for claiming accumulated NLS rewards, without broadcasting it.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The user's wallet instance.

##### recipientAddress

`string` \| `undefined`

Optional. The address to simulate sending rewards to.

##### fundCoin?

`Coin`[]

Optional. Coins to simulate as the fee source.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to:
- The simulated transaction result including gas estimate and fee.

***

### simulateDepositTx()

> **simulateDepositTx**(`nolusWallet`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Lpp.ts:214](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L214)

Simulates a deposit into the LPP using the specified LPN amount.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The user's wallet instance.

##### fundCoin?

`Coin`[]

The simulated deposit amount.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to:
- The simulated transaction result including gas estimate and fee.

***

### simulateDistributeRewardsTx()

> **simulateDistributeRewardsTx**(`nolusWallet`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Lpp.ts:243](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lpp.ts#L243)

Simulates the distribution of NLS rewards into the LPP pool.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet instance.

##### fundCoin?

`Coin`[]

The simulated NLS reward distribution amount.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to:
- The simulated transaction result including gas estimate and fee.
