[**@nolus/nolusjs**](../README.md)

***

[@nolus/nolusjs](../README.md) / ChainConstants

# Class: ChainConstants

Defined in: [src/constants/ChainConstants.ts:12](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L12)

Here you can find all necessary constants that describe the Nolus Network parameters.

Usage:

```ts
import { ChainConstants } from '@nolus/nolusjs';

const nolusCoinType = ChainConstants.COIN_TYPE;
```

## Constructors

### Constructor

> **new ChainConstants**(): `ChainConstants`

#### Returns

`ChainConstants`

## Properties

### BECH32\_PREFIX\_ACC\_ADDR

> `readonly` `static` **BECH32\_PREFIX\_ACC\_ADDR**: `string` = `'nolus'`

Defined in: [src/constants/ChainConstants.ts:25](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L25)

***

### BECH32\_PREFIX\_ACC\_PUB

> `readonly` `static` **BECH32\_PREFIX\_ACC\_PUB**: `string`

Defined in: [src/constants/ChainConstants.ts:29](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L29)

value = BECH32_PREFIX_ACC_ADDR + 'pub'

***

### BECH32\_PREFIX\_CONS\_ADDR

> `readonly` `static` **BECH32\_PREFIX\_CONS\_ADDR**: `string`

Defined in: [src/constants/ChainConstants.ts:41](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L41)

value = BECH32_PREFIX_ACC_ADDR + 'valcons'

***

### BECH32\_PREFIX\_CONS\_PUB

> `readonly` `static` **BECH32\_PREFIX\_CONS\_PUB**: `string`

Defined in: [src/constants/ChainConstants.ts:45](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L45)

value = BECH32_PREFIX_ACC_ADDR + 'valconspub'

***

### BECH32\_PREFIX\_VAL\_ADDR

> `readonly` `static` **BECH32\_PREFIX\_VAL\_ADDR**: `string`

Defined in: [src/constants/ChainConstants.ts:33](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L33)

value = BECH32_PREFIX_ACC_ADDR + 'valoper'

***

### BECH32\_PREFIX\_VAL\_PUB

> `readonly` `static` **BECH32\_PREFIX\_VAL\_PUB**: `string`

Defined in: [src/constants/ChainConstants.ts:37](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L37)

value = BECH32_PREFIX_ACC_ADDR + 'valoperpub'

***

### BIP44\_PATH

> `readonly` `static` **BIP44\_PATH**: `string` = `"44'/118'/0'/0/0"`

Defined in: [src/constants/ChainConstants.ts:51](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L51)

***

### CHAIN\_KEY

> `readonly` `static` **CHAIN\_KEY**: `string` = `'NOLUS'`

Defined in: [src/constants/ChainConstants.ts:15](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L15)

***

### CHAIN\_NAME

> `readonly` `static` **CHAIN\_NAME**: `string` = `'Nolus'`

Defined in: [src/constants/ChainConstants.ts:16](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L16)

***

### COIN\_DECIMALS

> `readonly` `static` **COIN\_DECIMALS**: `number` = `6`

Defined in: [src/constants/ChainConstants.ts:19](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L19)

***

### COIN\_DENOM

> `readonly` `static` **COIN\_DENOM**: `string` = `'NLS'`

Defined in: [src/constants/ChainConstants.ts:17](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L17)

***

### COIN\_GECKO\_ID

> `readonly` `static` **COIN\_GECKO\_ID**: `string` = `'nolus'`

Defined in: [src/constants/ChainConstants.ts:20](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L20)

***

### COIN\_MINIMAL\_DENOM

> `readonly` `static` **COIN\_MINIMAL\_DENOM**: `string` = `'unls'`

Defined in: [src/constants/ChainConstants.ts:18](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L18)

***

### COIN\_TYPE

> `readonly` `static` **COIN\_TYPE**: `number` = `118`

Defined in: [src/constants/ChainConstants.ts:21](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L21)

***

### GAS\_MULTIPLIER

> `readonly` `static` **GAS\_MULTIPLIER**: `number` = `3.5`

Defined in: [src/constants/ChainConstants.ts:48](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L48)

***

### GAS\_PRICE

> `readonly` `static` **GAS\_PRICE**: `string`

Defined in: [src/constants/ChainConstants.ts:47](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L47)

***

### GAS\_PRICE\_NUMBER

> `readonly` `static` **GAS\_PRICE\_NUMBER**: `number` = `0.023`

Defined in: [src/constants/ChainConstants.ts:46](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L46)

***

### IBC\_TRANSFER\_TIMEOUT

> `readonly` `static` **IBC\_TRANSFER\_TIMEOUT**: `number` = `60`

Defined in: [src/constants/ChainConstants.ts:22](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/constants/ChainConstants.ts#L22)
