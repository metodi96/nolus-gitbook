[**@nolus/nolusjs**](../README.md)

***

[@nolus/nolusjs](../README.md) / AssetUtils

# Class: AssetUtils

Defined in: [src/utils/AssetUtils.ts:11](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/AssetUtils.ts#L11)

AssetUtils provides helpers for working with Nolus assets.

Тhe Nolus protocol works with a certain set of currencies called 'supported currencies':
- Тhe Nolus protocol recognizes them by their 'ticker' (e.g. 'OSMO', 'NLS', 'USDC' etc.).
- Тhe bank module recognizes them by their calculated ibc/ denom.

## Constructors

### Constructor

> **new AssetUtils**(): `AssetUtils`

#### Returns

`AssetUtils`

## Methods

### findBankSymbolByTicker()

> `static` **findBankSymbolByTicker**(`currenciesInfo`, `ticker`): `string` \| `null`

Defined in: [src/utils/AssetUtils.ts:40](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/AssetUtils.ts#L40)

#### Parameters

##### currenciesInfo

[`CurrencyInfo`](../@nolus/namespaces/NolusContracts/interfaces/CurrencyInfo.md)[]

##### ticker

`string`

#### Returns

`string` \| `null`

***

### findDexSymbolByTicker()

> `static` **findDexSymbolByTicker**(`currenciesInfo`, `ticker`): `string` \| `null`

Defined in: [src/utils/AssetUtils.ts:34](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/AssetUtils.ts#L34)

#### Parameters

##### currenciesInfo

[`CurrencyInfo`](../@nolus/namespaces/NolusContracts/interfaces/CurrencyInfo.md)[]

##### ticker

`string`

#### Returns

`string` \| `null`

***

### findTickersByGroup()

> `static` **findTickersByGroup**(`currenciesInfo`, `group`): `string`[]

Defined in: [src/utils/AssetUtils.ts:22](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/AssetUtils.ts#L22)

The supported currencies are organized into several groups - Lpn, Lease, Native.
The following rules apply here:
- "Lpn contains the Lpp currencies.",
- "Lease currencies are the ones customers may open lease in.",
- "Native defines the native currency for the Nolus AMM protocol.",
- "Leases may be paid with any of the provided currencies.",

 The current method returns a list of tickers by group.

#### Parameters

##### currenciesInfo

[`CurrencyInfo`](../@nolus/namespaces/NolusContracts/interfaces/CurrencyInfo.md)[]

##### group

`string`

#### Returns

`string`[]
