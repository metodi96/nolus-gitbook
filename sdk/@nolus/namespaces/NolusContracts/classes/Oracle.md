[**@nolus/nolusjs**](../../../../README.md)

***

[@nolus/nolusjs](../../../../README.md) / [NolusContracts](../README.md) / Oracle

# Class: Oracle

Defined in: [src/contracts/clients/Oracle.ts:41](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L41)

An on-chain oracle providing market data prices to the rest of the system.

Usage:

```ts
import { NolusClient, NolusContracts } from '@nolus/nolusjs';

const cosm = await NolusClient.getInstance().getCosmWasmClient();
oracleInstance = new NolusContracts.Oracle(cosm, oracleContractAddress);
```

There are also methods for simulating contract operations in order to obtain preliminary information about the transaction.

## Constructors

### Constructor

> **new Oracle**(`cosmWasmClient`, `contractAddress`): `Oracle`

Defined in: [src/contracts/clients/Oracle.ts:45](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L45)

#### Parameters

##### cosmWasmClient

`CosmWasmClient`

##### contractAddress

`string`

#### Returns

`Oracle`

## Methods

### feedPrices()

> **feedPrices**(`nolusWallet`, `feedPrices`, `fee`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Oracle.ts:210](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L210)

Executes a transaction to submit new price data to the Oracle.

Only addresses registered as authorized feeders may submit price feeds.
The prices submitted are used to update the Oracle’s internal price records.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet instance of the authorized feeder.

##### feedPrices

[`FeedPrices`](../interfaces/FeedPrices.md)

The price data to be submitted.

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### fundCoin?

`Coin`[]

Optional. Additional tokens to fund the transaction.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to:
- The execution result, including transaction hash, gas usage and events.

#### Throws

If the wallet address is not whitelisted as a feeder, the contract will reject the execution.

***

### getBaseCurrency()

> **getBaseCurrency**(): `Promise`\<`string`\>

Defined in: [src/contracts/clients/Oracle.ts:56](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L56)

Retrieves the configured base currency used by the Oracle for expressing all price values.

#### Returns

`Promise`\<`string`\>

A `Promise` resolving to:
- The base currency ticker (e.g. "USDC_NOBLE").

***

### getBasePrice()

> **getBasePrice**(`currency`): `Promise`\<[`Price`](../interfaces/Price.md)\>

Defined in: [src/contracts/clients/Oracle.ts:90](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L90)

Retrieves the current price of a given asset relative to the base currency.

#### Parameters

##### currency

`string`

The asset ticker to fetch the price for (e.g. "ATOM", "NLS").

#### Returns

`Promise`\<[`Price`](../interfaces/Price.md)\>

A `Promise` resolving to:
- The asset price expressed in base currency units.

***

### getConfig()

> **getConfig**(): `Promise`\<[`OracleConfig`](../interfaces/OracleConfig.md)\>

Defined in: [src/contracts/clients/Oracle.ts:190](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L190)

Retrieves the Oracle’s current configuration parameters.

#### Returns

`Promise`\<[`OracleConfig`](../interfaces/OracleConfig.md)\>

A `Promise` resolving to an object containing:
- `min_feeders`: Minimum portion of feeder submissions required per price update (in permilles).
- `sample_period_secs`: Time interval between collected price samples (in seconds).
- `samples_number`: Number of samples used to compute the final price.
- `discount_factor`: Discount factor on old observations applied in the exponential moving average algorithm (in permilles).

***

### getCurrencies()

> **getCurrencies**(): `Promise`\<[`CurrencyInfo`](../interfaces/CurrencyInfo.md)[]\>

Defined in: [src/contracts/clients/Oracle.ts:128](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L128)

Retrieves all supported currencies and their associated metadata.

#### Returns

`Promise`\<[`CurrencyInfo`](../interfaces/CurrencyInfo.md)[]\>

A `Promise` resolving to:
- An array of currency definitions, each containing:
  - `ticker`: The currency ticker
  - `bank_symbol` and `dex_symbol`: On-chain denominations
  - `decimal_digits`: Decimal precision
  - `group`: Logical group such as "lpn", "lease", or "native"

***

### getCurrencyPairs()

> **getCurrencyPairs**(): `Promise`\<\[`string`, \[`number`, `string`\]\][]\>

Defined in: [src/contracts/clients/Oracle.ts:114](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L114)

Retrieves the intermediary swap pairs used by the Oracle to construct pricing paths.

Each pair defines a route between two assets and their Oracle source ID.

#### Returns

`Promise`\<\[`string`, \[`number`, `string`\]\][]\>

A `Promise` resolving to:
- An array of tuples: [asset_ticker, [oracle_id, intermediate_ticker]]

***

### getFeeders()

> **getFeeders**(): `Promise`\<`string`[]\>

Defined in: [src/contracts/clients/Oracle.ts:177](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L177)

Retrieves the list of all addresses currently authorized as price feeders.

#### Returns

`Promise`\<`string`[]\>

A `Promise` resolving to:
- An array of bech32 wallet addresses.

***

### getPrices()

> **getPrices**(): `Promise`\<\{\[`key`: `string`\]: [`Price`](../interfaces/Price.md); \}\>

Defined in: [src/contracts/clients/Oracle.ts:78](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L78)

Retrieves the full set of known asset prices from the Oracle.

#### Returns

`Promise`\<\{\[`key`: `string`\]: [`Price`](../interfaces/Price.md); \}\>

A `Promise` resolving to:
- A mapping of asset tickers to their respective price data, including:
  - The asset amount (`amount`)
  - Its quoted value in the base currency (`amount_quote`)

***

### getStableCurrency()

> **getStableCurrency**(): `Promise`\<`string`\>

Defined in: [src/contracts/clients/Oracle.ts:66](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L66)

Retrieves the stable currency used for stable price conversions and display.

#### Returns

`Promise`\<`string`\>

A `Promise` resolving to:
- The stable currency ticker (e.g. "USDC_NOBLE").

***

### getStablePrice()

> **getStablePrice**(`currency`): `Promise`\<[`Price`](../interfaces/Price.md)\>

Defined in: [src/contracts/clients/Oracle.ts:102](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L102)

Retrieves the current price of a given asset relative to the stable currency.

#### Parameters

##### currency

`string`

The asset ticker to fetch the stable price for.

#### Returns

`Promise`\<[`Price`](../interfaces/Price.md)\>

A `Promise` resolving to:
- The asset price expressed in stable currency units.

***

### getSwapPath()

> **getSwapPath**(`fromCurrency`, `toCurrency`): `Promise`\<[`SwapPath`](../interfaces/SwapPath.md)[]\>

Defined in: [src/contracts/clients/Oracle.ts:143](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L143)

Retrieves the swap path between two assets as defined by the Oracle.

This is useful for building multi-hop pricing routes or swap logic.

#### Parameters

##### fromCurrency

`string`

The source asset ticker.

##### toCurrency

`string`

The target asset ticker.

#### Returns

`Promise`\<[`SwapPath`](../interfaces/SwapPath.md)[]\>

A `Promise` resolving to:
- An array of intermediary hops as [oracle_id, ticker] pairs.

***

### getSwapTree()

> **getSwapTree**(): `Promise`\<[`SwapTree`](../interfaces/SwapTree.md)\>

Defined in: [src/contracts/clients/Oracle.ts:155](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L155)

Retrieves the full swap tree starting from the base currency.

This tree represents all known intermediary paths between supported assets.

#### Returns

`Promise`\<[`SwapTree`](../interfaces/SwapTree.md)\>

A `Promise` resolving to:
- A recursive structure representing the swap tree by Oracle routes.

***

### isFeeder()

> **isFeeder**(`address`): `Promise`\<`boolean`\>

Defined in: [src/contracts/clients/Oracle.ts:167](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L167)

Checks whether a given address is authorized as a price feeder for the Oracle.

#### Parameters

##### address

`string`

The wallet address to verify.

#### Returns

`Promise`\<`boolean`\>

A `Promise` resolving to:
- `true` if the address is a registered feeder, otherwise `false`.

***

### simulateFeedPricesTx()

> **simulateFeedPricesTx**(`nolusWallet`, `feedPrices`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Oracle.ts:228](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Oracle.ts#L228)

Simulates the transaction for feeding prices to the Oracle, without broadcasting it.

This is used to estimate gas or validate the structure of the feed before submission.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet instance used for simulation.

##### feedPrices

[`FeedPrices`](../interfaces/FeedPrices.md)

The price data to simulate, same structure as `feedPrices`.

##### fundCoin?

`Coin`[]

Optional. Simulated coins to cover fees.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to:
- The simulated transaction result including gas and fee estimate.

#### Throws

If the address is not a whitelisted feeder, the simulation will fail.
