[**@nolus/nolusjs**](../README.md)

***

[@nolus/nolusjs](../README.md) / KeyUtils

# Class: KeyUtils

Defined in: [src/utils/KeyUtils.ts:8](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L8)

KeyUtils provides helpers for working with Nolus accounts.

## Constructors

### Constructor

> **new KeyUtils**(): `KeyUtils`

#### Returns

`KeyUtils`

## Methods

### generateMnemonic()

> `static` **generateMnemonic**(): `string`

Defined in: [src/utils/KeyUtils.ts:47](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L47)

#### Returns

`string`

***

### getAddressFromPublicKey()

> `static` **getAddressFromPublicKey**(`publicKey`, `prefix?`): `string`

Defined in: [src/utils/KeyUtils.ts:24](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L24)

#### Parameters

##### publicKey

`Uint8Array`

##### prefix?

`string` = `ChainConstants.BECH32_PREFIX_ACC_ADDR`

#### Returns

`string`

***

### getPrivateKeyFromMnemonic()

> `static` **getPrivateKeyFromMnemonic**(`mnemonic`, `hdPath`): `Promise`\<`Uint8Array`\<`ArrayBufferLike`\>\>

Defined in: [src/utils/KeyUtils.ts:9](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L9)

#### Parameters

##### mnemonic

`string`

##### hdPath

`HdPath`

#### Returns

`Promise`\<`Uint8Array`\<`ArrayBufferLike`\>\>

***

### getPrivateKeyFromSeed()

> `static` **getPrivateKeyFromSeed**(`seed`, `hdPath`): `Uint8Array`\<`ArrayBufferLike`\>

Defined in: [src/utils/KeyUtils.ts:19](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L19)

#### Parameters

##### seed

`Uint8Array`

##### hdPath

`HdPath`

#### Returns

`Uint8Array`\<`ArrayBufferLike`\>

***

### getPublicKeyFromPrivateKey()

> `static` **getPublicKeyFromPrivateKey**(`privateKey`): `Promise`\<`Uint8Array`\<`ArrayBuffer`\>\>

Defined in: [src/utils/KeyUtils.ts:33](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L33)

#### Parameters

##### privateKey

`Uint8Array`

#### Returns

`Promise`\<`Uint8Array`\<`ArrayBuffer`\>\>

***

### getSeedFromMnemonic()

> `static` **getSeedFromMnemonic**(`mnemonic`): `Promise`\<`Uint8Array`\<`ArrayBufferLike`\>\>

Defined in: [src/utils/KeyUtils.ts:14](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L14)

#### Parameters

##### mnemonic

`string`

#### Returns

`Promise`\<`Uint8Array`\<`ArrayBufferLike`\>\>

***

### isAddressValid()

> `static` **isAddressValid**(`address`, `prefix?`): `boolean`

Defined in: [src/utils/KeyUtils.ts:38](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/utils/KeyUtils.ts#L38)

#### Parameters

##### address

`string`

##### prefix?

`string` = `ChainConstants.BECH32_PREFIX_ACC_ADDR`

#### Returns

`boolean`
