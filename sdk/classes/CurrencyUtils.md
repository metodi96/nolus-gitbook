[**@nolus/nolusjs**](../README.md)

***

[@nolus/nolusjs](../README.md) / CurrencyUtils

# Class: CurrencyUtils

Defined in: [src/utils/CurrencyUtils.ts:8](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L8)

CurrencyUtils provides helpers for working with Nolus currencies. Conversion, formatting and calculation.

## Constructors

### Constructor

> **new CurrencyUtils**(): `CurrencyUtils`

#### Returns

`CurrencyUtils`

## Methods

### calculateBalance()

> `static` **calculateBalance**(`price`, `tokenAmount`, `tokenDecimal`): `PricePretty`

Defined in: [src/utils/CurrencyUtils.ts:64](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L64)

#### Parameters

##### price

`string`

##### tokenAmount

`Coin`

##### tokenDecimal

`number`

#### Returns

`PricePretty`

***

### convertCoinMinimalDenomToDenom()

> `static` **convertCoinMinimalDenomToDenom**(`tokenAmount`, `minimalDenom`, `denom`, `decimals`): `CoinPretty` \| `null`

Defined in: [src/utils/CurrencyUtils.ts:26](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L26)

#### Parameters

##### tokenAmount

`Coin` \| `null` \| `undefined`

##### minimalDenom

`string`

##### denom

`string`

##### decimals

`number`

#### Returns

`CoinPretty` \| `null`

***

### convertCoinUNolusToNolus()

> `static` **convertCoinUNolusToNolus**(`tokenAmount`): `CoinPretty` \| `null`

Defined in: [src/utils/CurrencyUtils.ts:22](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L22)

#### Parameters

##### tokenAmount

`Coin` \| `null` \| `undefined`

#### Returns

`CoinPretty` \| `null`

***

### convertCosmosCoinToKeplCoin()

> `static` **convertCosmosCoinToKeplCoin**(`cosmosCoin`): `Coin`

Defined in: [src/utils/CurrencyUtils.ts:57](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L57)

#### Parameters

##### cosmosCoin

`Coin` \| `undefined`

#### Returns

`Coin`

***

### convertDenomToMinimalDenom()

> `static` **convertDenomToMinimalDenom**(`tokenAmount`, `minimalDenom`, `decimals`): `Coin`

Defined in: [src/utils/CurrencyUtils.ts:13](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L13)

#### Parameters

##### tokenAmount

`string`

##### minimalDenom

`string`

##### decimals

`number`

#### Returns

`Coin`

***

### convertMinimalDenomToDenom()

> `static` **convertMinimalDenomToDenom**(`tokenAmount`, `minimalDenom`, `denom`, `decimals`): `CoinPretty`

Defined in: [src/utils/CurrencyUtils.ts:45](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L45)

#### Parameters

##### tokenAmount

`string`

##### minimalDenom

`string`

##### denom

`string`

##### decimals

`number`

#### Returns

`CoinPretty`

***

### convertNolusToUNolus()

> `static` **convertNolusToUNolus**(`tokenAmount`): `Coin`

Defined in: [src/utils/CurrencyUtils.ts:9](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L9)

#### Parameters

##### tokenAmount

`string`

#### Returns

`Coin`

***

### convertUNolusToNolus()

> `static` **convertUNolusToNolus**(`tokenAmount`): `CoinPretty`

Defined in: [src/utils/CurrencyUtils.ts:41](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L41)

#### Parameters

##### tokenAmount

`string`

#### Returns

`CoinPretty`

***

### formatPrice()

> `static` **formatPrice**(`price`): `PricePretty`

Defined in: [src/utils/CurrencyUtils.ts:77](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/CurrencyUtils.ts#L77)

#### Parameters

##### price

`string`

#### Returns

`PricePretty`
