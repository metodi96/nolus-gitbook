# Introduction

**`@nolus/nolusjs`** is a TypeScript SDK for interacting with the Nolus Protocol — a DeFi primitive offering capital-efficient spot margin trading with fixed interest rates and a predictable leverage model. The SDK abstracts complex CosmWasm contract interactions and IBC logic, enabling developers to quote, open, monitor, and repay leveraged positions across supported Cosmos chains.

- npm package: [`@nolus/nolusjs`](https://www.npmjs.com/package/@nolus/nolusjs)
- Source repo: [github.com/nolus-protocol/nolus.js](https://github.com/nolus-protocol/nolus.js)

## Modules

The SDK is organized into five top-level modules:

| Module | Purpose |
|---|---|
| **`client`** | Connects to the blockchain via Tendermint RPC. Entry point for every read or write call. |
| **`wallet`** | Wallet abstraction built on CosmJS `OfflineSigner`. Provides key derivation, address generation, and signing. |
| **`contracts`** | Typed wrappers around the Nolus CosmWasm contracts: `Leaser`, `Lease`, `Lpp`, `Oracle`, `Treasury`, `Admin`. |
| **`utils`** | Asset parsing, denom resolution, key generation, currency formatting. |
| **`constants`** | Chain defaults — bech32 prefixes, native denom, gas configuration. |

## How to read these docs

If you're new to the SDK, start with **[Getting Started](getting-started.md)** — it walks you from installation through a working lease quote in about a dozen lines of code.

For the full method-by-method API surface — every class, every parameter, every response type — refer to the **auto-generated reference** that ships from the source repo:

➡️ [**`@nolus/nolusjs` API documentation**](https://nolus-protocol.github.io/nolus.js/)

The narrative pages here cover the 80% of the surface most users need; the upstream API reference is for the long tail.
