[**@nolus/nolusjs**](../README.md)

***

[@nolus/nolusjs](../README.md) / NolusClient

# Class: NolusClient

Defined in: [src/client/NolusClient.ts:18](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L18)

Nolus Client service class.

Usage:

```ts
import { NolusClient } from '@nolus/nolusjs';

NolusClient.setInstance(tendermintRpc);
```

## Properties

### cosmWasmClient

> `protected` **cosmWasmClient**: `Promise`\<`CosmWasmClient`\> \| `undefined`

Defined in: [src/client/NolusClient.ts:20](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L20)

***

### stargateClient

> `protected` **stargateClient**: `Promise`\<`StargateClient`\> \| `undefined`

Defined in: [src/client/NolusClient.ts:22](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L22)

***

### tmClient

> `protected` **tmClient**: `Promise`\<`CometClient`\> \| `undefined`

Defined in: [src/client/NolusClient.ts:21](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L21)

## Methods

### getBalance()

> **getBalance**(`address`, `denom`): `Promise`\<`Coin`\>

Defined in: [src/client/NolusClient.ts:74](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L74)

#### Parameters

##### address

`string`

##### denom

`string`

#### Returns

`Promise`\<`Coin`\>

***

### getBlockHeight()

> **getBlockHeight**(): `Promise`\<`number`\>

Defined in: [src/client/NolusClient.ts:116](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L116)

#### Returns

`Promise`\<`number`\>

***

### getChainId()

> **getChainId**(): `Promise`\<`string`\>

Defined in: [src/client/NolusClient.ts:65](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L65)

#### Returns

`Promise`\<`string`\>

***

### getCosmWasmClient()

> **getCosmWasmClient**(): `Promise`\<`CosmWasmClient`\>

Defined in: [src/client/NolusClient.ts:41](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L41)

#### Returns

`Promise`\<`CosmWasmClient`\>

***

### getSpendableBalance()

> **getSpendableBalance**(`address`, `denom`): `Promise`\<`QuerySpendableBalanceByDenomResponse`\>

Defined in: [src/client/NolusClient.ts:83](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L83)

#### Parameters

##### address

`string`

##### denom

`string`

#### Returns

`Promise`\<`QuerySpendableBalanceByDenomResponse`\>

***

### getStargateClient()

> **getStargateClient**(): `Promise`\<`StargateClient`\>

Defined in: [src/client/NolusClient.ts:49](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L49)

#### Returns

`Promise`\<`StargateClient`\>

***

### getTendermintClient()

> **getTendermintClient**(): `Promise`\<`CometClient`\>

Defined in: [src/client/NolusClient.ts:57](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L57)

#### Returns

`Promise`\<`CometClient`\>

***

### getInstance()

> `static` **getInstance**(): `NolusClient`

Defined in: [src/client/NolusClient.ts:30](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L30)

#### Returns

`NolusClient`

***

### setInstance()

> `static` **setInstance**(`tendermintRpc`): `void`

Defined in: [src/client/NolusClient.ts:37](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/client/NolusClient.ts#L37)

#### Parameters

##### tendermintRpc

`string`

#### Returns

`void`
