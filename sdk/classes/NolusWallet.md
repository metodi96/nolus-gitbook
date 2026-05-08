[**@nolus/nolusjs**](../README.md)

***

[@nolus/nolusjs](../README.md) / NolusWallet

# Class: NolusWallet

Defined in: [src/wallet/NolusWallet.ts:32](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L32)

Nolus Wallet service class.

Usage:

```ts
import { nolusOfflineSigner } from '@nolus/nolusjs/build/wallet/NolusWalletFactory';

const nolusWallet = await nolusOfflineSigner(offlineSigner);
nolusWallet.useAccount();
```

## Extends

- `SigningCosmWasmClient`

## Constructors

### Constructor

> **new NolusWallet**(`tmClient`, `signer`, `options`): `NolusWallet`

Defined in: [src/wallet/NolusWallet.ts:45](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L45)

#### Parameters

##### tmClient

`any`

##### signer

`OfflineSigner`

##### options

`SigningCosmWasmClientOptions`

#### Returns

`NolusWallet`

#### Overrides

`SigningCosmWasmClient.constructor`

## Properties

### address?

> `optional` **address?**: `string`

Defined in: [src/wallet/NolusWallet.ts:33](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L33)

***

### algo?

> `optional` **algo?**: `string`

Defined in: [src/wallet/NolusWallet.ts:35](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L35)

***

### broadcastPollIntervalMs

> `readonly` **broadcastPollIntervalMs**: `number` \| `undefined`

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:119

#### Inherited from

`SigningCosmWasmClient.broadcastPollIntervalMs`

***

### broadcastTimeoutMs

> `readonly` **broadcastTimeoutMs**: `number` \| `undefined`

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:118

#### Inherited from

`SigningCosmWasmClient.broadcastTimeoutMs`

***

### offlineSigner

> `protected` **offlineSigner**: `OfflineSigner` & `object`

Defined in: [src/wallet/NolusWallet.ts:37](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L37)

#### Type Declaration

##### getGasInfo?

> `optional` **getGasInfo?**: `Function`

##### getSequence?

> `optional` **getSequence?**: `Function`

##### registry?

> `optional` **registry?**: `Registry`

##### simulateMultiTx?

> `optional` **simulateMultiTx?**: `Function`

##### simulateTx?

> `optional` **simulateTx?**: `Function`

***

### pubKey?

> `optional` **pubKey?**: `Uint8Array`\<`ArrayBufferLike`\>

Defined in: [src/wallet/NolusWallet.ts:34](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L34)

***

### registry

> `readonly` **registry**: `Registry`

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:117

#### Inherited from

`SigningCosmWasmClient.registry`

## Methods

### broadcastTx()

> **broadcastTx**(`tx`, `timeoutMs?`, `pollIntervalMs?`): `Promise`\<`DeliverTxResponse`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:88

Broadcasts a signed transaction to the network and monitors its inclusion in a block.

If broadcasting is rejected by the node for some reason (e.g. because of a CheckTx failure),
an error is thrown.

If the transaction is not included in a block before the provided timeout, this errors with a `TimeoutError`.

If the transaction is included in a block, a `DeliverTxResponse` is returned. The caller then
usually needs to check for execution success or failure.

#### Parameters

##### tx

`Uint8Array`

##### timeoutMs?

`number`

##### pollIntervalMs?

`number`

#### Returns

`Promise`\<`DeliverTxResponse`\>

#### Inherited from

`SigningCosmWasmClient.broadcastTx`

***

### broadcastTxSync()

> **broadcastTxSync**(`tx`): `Promise`\<`string`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:100

Broadcasts a signed transaction to the network without monitoring it.

If broadcasting is rejected by the node for some reason (e.g. because of a CheckTx failure),
an error is thrown.

If the transaction is broadcasted, a `string` containing the hash of the transaction is returned. The caller then
usually needs to check if the transaction was included in a block and was successful.

#### Parameters

##### tx

`Uint8Array`

#### Returns

`Promise`\<`string`\>

Returns the hash of the transaction

#### Inherited from

`SigningCosmWasmClient.broadcastTxSync`

***

### clearAdmin()

> **clearAdmin**(`senderAddress`, `contractAddress`, `fee`, `memo?`): `Promise`\<`ChangeAdminResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:155

#### Parameters

##### senderAddress

`string`

##### contractAddress

`string`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`ChangeAdminResult`\>

#### Inherited from

`SigningCosmWasmClient.clearAdmin`

***

### delegateTokens()

> **delegateTokens**(`delegatorAddress`, `validatorAddress`, `amount`, `fee`, `memo?`): `Promise`\<`DeliverTxResponse`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:163

#### Parameters

##### delegatorAddress

`string`

##### validatorAddress

`string`

##### amount

`Coin`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`DeliverTxResponse`\>

#### Inherited from

`SigningCosmWasmClient.delegateTokens`

***

### disconnect()

> **disconnect**(): `void`

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:76

#### Returns

`void`

#### Inherited from

`SigningCosmWasmClient.disconnect`

***

### execute()

> **execute**(`senderAddress`, `contractAddress`, `msg`, `fee`, `memo?`, `funds?`): `Promise`\<`ExecuteResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:157

#### Parameters

##### senderAddress

`string`

##### contractAddress

`string`

##### msg

`any`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

##### funds?

readonly `Coin`[]

#### Returns

`Promise`\<`ExecuteResult`\>

#### Inherited from

`SigningCosmWasmClient.execute`

***

### executeContract()

> **executeContract**(`contractAddress`, `msg`, `fee`, `memo?`, `funds?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/wallet/NolusWallet.ts:200](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L200)

#### Parameters

##### contractAddress

`string`

##### msg

`Record`\<`string`, `any`\>

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

##### funds?

`Coin`[]

#### Returns

`Promise`\<`ExecuteResult`\>

***

### executeContractSubMsg()

> **executeContractSubMsg**(`contractData`, `fee`, `memo?`, `funds?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/wallet/NolusWallet.ts:207](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L207)

#### Parameters

##### contractData

[`ContractData`](../@nolus/namespaces/NolusContracts/interfaces/ContractData.md)[]

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

##### funds?

`Coin`[]

#### Returns

`Promise`\<`ExecuteResult`\>

***

### executeMultiple()

> **executeMultiple**(`senderAddress`, `instructions`, `fee`, `memo?`): `Promise`\<`ExecuteResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:161

Like `execute` but allows executing multiple messages in one transaction.

#### Parameters

##### senderAddress

`string`

##### instructions

readonly `ExecuteInstruction`[]

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`ExecuteResult`\>

#### Inherited from

`SigningCosmWasmClient.executeMultiple`

***

### forceGetCometClient()

> `protected` **forceGetCometClient**(): `CometClient`

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:65

#### Returns

`CometClient`

#### Inherited from

`SigningCosmWasmClient.forceGetCometClient`

***

### forceGetQueryClient()

> `protected` **forceGetQueryClient**(): `QueryClient` & `AuthExtension` & `BankExtension` & `TxExtension` & `WasmExtension`

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:67

#### Returns

`QueryClient` & `AuthExtension` & `BankExtension` & `TxExtension` & `WasmExtension`

#### Inherited from

`SigningCosmWasmClient.forceGetQueryClient`

***

### gasPrices()

> **gasPrices**(): `Promise`\<\{\[`denom`: `string`\]: `number`; \}\>

Defined in: [src/wallet/NolusWallet.ts:506](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L506)

#### Returns

`Promise`\<\{\[`denom`: `string`\]: `number`; \}\>

***

### getAccount()

> **getAccount**(`searchAddress`): `Promise`\<`Account` \| `null`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:70

#### Parameters

##### searchAddress

`string`

#### Returns

`Promise`\<`Account` \| `null`\>

#### Inherited from

`SigningCosmWasmClient.getAccount`

***

### getBalance()

> **getBalance**(`address`, `denom`): `Promise`\<`Coin`\>

Defined in: [src/wallet/NolusWallet.ts:462](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L462)

#### Parameters

##### address

`string`

##### denom

`string`

#### Returns

`Promise`\<`Coin`\>

#### Overrides

`SigningCosmWasmClient.getBalance`

***

### getBlock()

> **getBlock**(`height?`): `Promise`\<`Block`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:72

#### Parameters

##### height?

`number`

#### Returns

`Promise`\<`Block`\>

#### Inherited from

`SigningCosmWasmClient.getBlock`

***

### getChainId()

> **getChainId**(): `Promise`\<`string`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:68

#### Returns

`Promise`\<`string`\>

#### Inherited from

`SigningCosmWasmClient.getChainId`

***

### getCodeDetails()

> **getCodeDetails**(`codeId`): `Promise`\<`CodeDetails`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:108

#### Parameters

##### codeId

`number`

#### Returns

`Promise`\<`CodeDetails`\>

#### Inherited from

`SigningCosmWasmClient.getCodeDetails`

***

### getCodes()

> **getCodes**(): `Promise`\<readonly `Code`[]\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:107

getCodes() returns all codes and is just looping through all pagination pages.

This is potentially inefficient and advanced apps should consider creating
their own query client to handle pagination together with the app's screens.

#### Returns

`Promise`\<readonly `Code`[]\>

#### Inherited from

`SigningCosmWasmClient.getCodes`

***

### getCometClient()

> `protected` **getCometClient**(): `CometClient` \| `undefined`

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:64

#### Returns

`CometClient` \| `undefined`

#### Inherited from

`SigningCosmWasmClient.getCometClient`

***

### getContract()

> **getContract**(`address`): `Promise`\<`Contract`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:124

Throws an error if no contract was found at the address

#### Parameters

##### address

`string`

#### Returns

`Promise`\<`Contract`\>

#### Inherited from

`SigningCosmWasmClient.getContract`

***

### getContractCodeHistory()

> **getContractCodeHistory**(`address`): `Promise`\<readonly `ContractCodeHistoryEntry`[]\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:128

Throws an error if no contract was found at the address

#### Parameters

##### address

`string`

#### Returns

`Promise`\<readonly `ContractCodeHistoryEntry`[]\>

#### Inherited from

`SigningCosmWasmClient.getContractCodeHistory`

***

### getContracts()

> **getContracts**(`codeId`): `Promise`\<readonly `string`[]\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:115

getContracts() returns all contract instances for one code and is just looping through all pagination pages.

This is potentially inefficient and advanced apps should consider creating
their own query client to handle pagination together with the app's screens.

#### Parameters

##### codeId

`number`

#### Returns

`Promise`\<readonly `string`[]\>

#### Inherited from

`SigningCosmWasmClient.getContracts`

***

### getContractsByCreator()

> **getContractsByCreator**(`creator`): `Promise`\<`string`[]\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:120

Returns a list of contract addresses created by the given creator.
This just loops through all pagination pages.

#### Parameters

##### creator

`string`

#### Returns

`Promise`\<`string`[]\>

#### Inherited from

`SigningCosmWasmClient.getContractsByCreator`

***

### getGasInfo()

> **getGasInfo**(`messages`, `memo`, `pubkey`, `sequence`): `Promise`\<\{ `gas`: `number`; `gasInfo`: `GasInfo` \| `undefined`; `usedFee`: `StdFee`; \}\>

Defined in: [src/wallet/NolusWallet.ts:84](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L84)

#### Parameters

##### messages

`object`[]

##### memo

`string`

##### pubkey

`Pubkey`

##### sequence

`number`

#### Returns

`Promise`\<\{ `gas`: `number`; `gasInfo`: `GasInfo` \| `undefined`; `usedFee`: `StdFee`; \}\>

***

### getHeight()

> **getHeight**(): `Promise`\<`number`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:69

#### Returns

`Promise`\<`number`\>

#### Inherited from

`SigningCosmWasmClient.getHeight`

***

### getOfflineSigner()

> **getOfflineSigner**(): `OfflineSigner` & `object`

Defined in: [src/wallet/NolusWallet.ts:53](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L53)

#### Returns

`OfflineSigner` & `object`

***

### getQueryClient()

> `protected` **getQueryClient**(): `QueryClient` & `AuthExtension` & `BankExtension` & `TxExtension` & `WasmExtension` \| `undefined`

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:66

#### Returns

`QueryClient` & `AuthExtension` & `BankExtension` & `TxExtension` & `WasmExtension` \| `undefined`

#### Inherited from

`SigningCosmWasmClient.getQueryClient`

***

### getSequence()

> **getSequence**(`address`): `Promise`\<`SequenceResponse`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:71

#### Parameters

##### address

`string`

#### Returns

`Promise`\<`SequenceResponse`\>

#### Inherited from

`SigningCosmWasmClient.getSequence`

***

### getTx()

> **getTx**(`id`): `Promise`\<`IndexedTx` \| `null`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:74

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`IndexedTx` \| `null`\>

#### Inherited from

`SigningCosmWasmClient.getTx`

***

### instantiate()

> **instantiate**(`senderAddress`, `codeId`, `msg`, `label`, `fee`, `options?`): `Promise`\<`InstantiateResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:152

#### Parameters

##### senderAddress

`string`

##### codeId

`number`

##### msg

`any`

##### label

`string`

##### fee

`number` \| `StdFee` \| `"auto"`

##### options?

`InstantiateOptions`

#### Returns

`Promise`\<`InstantiateResult`\>

#### Inherited from

`SigningCosmWasmClient.instantiate`

***

### instantiate2()

> **instantiate2**(`senderAddress`, `codeId`, `salt`, `msg`, `label`, `fee`, `options?`): `Promise`\<`InstantiateResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:153

#### Parameters

##### senderAddress

`string`

##### codeId

`number`

##### salt

`Uint8Array`

##### msg

`any`

##### label

`string`

##### fee

`number` \| `StdFee` \| `"auto"`

##### options?

`InstantiateOptions`

#### Returns

`Promise`\<`InstantiateResult`\>

#### Inherited from

`SigningCosmWasmClient.instantiate2`

***

### migrate()

> **migrate**(`senderAddress`, `contractAddress`, `codeId`, `migrateMsg`, `fee`, `memo?`): `Promise`\<`MigrateResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:156

#### Parameters

##### senderAddress

`string`

##### contractAddress

`string`

##### codeId

`number`

##### migrateMsg

`any`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`MigrateResult`\>

#### Inherited from

`SigningCosmWasmClient.migrate`

***

### queryContractRaw()

> **queryContractRaw**(`address`, `key`): `Promise`\<`Uint8Array`\<`ArrayBufferLike`\> \| `null`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:135

Returns the data at the key if present (raw contract dependent storage data)
or null if no data at this key.

Promise is rejected when contract does not exist.

#### Parameters

##### address

`string`

##### key

`Uint8Array`

#### Returns

`Promise`\<`Uint8Array`\<`ArrayBufferLike`\> \| `null`\>

#### Inherited from

`SigningCosmWasmClient.queryContractRaw`

***

### queryContractSmart()

> **queryContractSmart**(`address`, `queryMsg`): `Promise`\<`any`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:143

Makes a smart query on the contract, returns the parsed JSON document.

Promise is rejected when contract does not exist.
Promise is rejected for invalid query format.
Promise is rejected for invalid response format.

#### Parameters

##### address

`string`

##### queryMsg

`any`

#### Returns

`Promise`\<`any`\>

#### Inherited from

`SigningCosmWasmClient.queryContractSmart`

***

### querySmartContract()

> **querySmartContract**(`contract`, `msg`, `height?`): `Promise`\<`QuerySmartContractStateRequest`\>

Defined in: [src/wallet/NolusWallet.ts:431](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L431)

#### Parameters

##### contract

`string`

##### msg

`object`

##### height?

`number`

#### Returns

`Promise`\<`QuerySmartContractStateRequest`\>

***

### queryTaxParams()

> **queryTaxParams**(): `Promise`\<`QueryParamsResponse`\>

Defined in: [src/wallet/NolusWallet.ts:522](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L522)

#### Returns

`Promise`\<`QueryParamsResponse`\>

***

### searchTx()

> **searchTx**(`query`): `Promise`\<`IndexedTx`[]\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:75

#### Parameters

##### query

`SearchTxQuery`

#### Returns

`Promise`\<`IndexedTx`[]\>

#### Inherited from

`SigningCosmWasmClient.searchTx`

***

### selectDynamicFee()

> **selectDynamicFee**(`gasEstimate`, `msgs`): `Promise`\<`StdFee`\>

Defined in: [src/wallet/NolusWallet.ts:467](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L467)

#### Parameters

##### gasEstimate

`number`

##### msgs

`object`[]

#### Returns

`Promise`\<`StdFee`\>

***

### sendTokens()

> **sendTokens**(`senderAddress`, `recipientAddress`, `amount`, `fee`, `memo?`): `Promise`\<`DeliverTxResponse`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:162

#### Parameters

##### senderAddress

`string`

##### recipientAddress

`string`

##### amount

readonly `Coin`[]

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`DeliverTxResponse`\>

#### Inherited from

`SigningCosmWasmClient.sendTokens`

***

### sign()

> **sign**(`signerAddress`, `messages`, `fee`, `memo`, `explicitSignerData?`, `timeoutHeight?`): `Promise`\<`TxRaw`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:193

#### Parameters

##### signerAddress

`string`

##### messages

readonly `EncodeObject`[]

##### fee

`StdFee`

##### memo

`string`

##### explicitSignerData?

`SignerData`

##### timeoutHeight?

`bigint`

#### Returns

`Promise`\<`TxRaw`\>

#### Inherited from

`SigningCosmWasmClient.sign`

***

### signAndBroadcast()

> **signAndBroadcast**(`signerAddress`, `messages`, `fee`, `memo?`, `timeoutHeight?`): `Promise`\<`DeliverTxResponse`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:175

Creates a transaction with the given messages, fee, memo and timeout height. Then signs and broadcasts the transaction.

#### Parameters

##### signerAddress

`string`

The address that will sign transactions using this instance. The signer must be able to sign with this address.

##### messages

readonly `EncodeObject`[]

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

##### timeoutHeight?

`bigint`

(optional) timeout height to prevent the tx from being committed past a certain height

#### Returns

`Promise`\<`DeliverTxResponse`\>

#### Inherited from

`SigningCosmWasmClient.signAndBroadcast`

***

### signAndBroadcastSync()

> **signAndBroadcastSync**(`signerAddress`, `messages`, `fee`, `memo?`, `timeoutHeight?`): `Promise`\<`string`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:191

Creates a transaction with the given messages, fee, memo and timeout height. Then signs and broadcasts the transaction.

This method is useful if you want to send a transaction in broadcast,
without waiting for it to be placed inside a block, because for example
I would like to receive the hash to later track the transaction with another tool.

#### Parameters

##### signerAddress

`string`

The address that will sign transactions using this instance. The signer must be able to sign with this address.

##### messages

readonly `EncodeObject`[]

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

##### timeoutHeight?

`bigint`

(optional) timeout height to prevent the tx from being committed past a certain height

#### Returns

`Promise`\<`string`\>

Returns the hash of the transaction

#### Inherited from

`SigningCosmWasmClient.signAndBroadcastSync`

***

### simulate()

> **simulate**(`signerAddress`, `messages`, `memo`): `Promise`\<`number`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:149

#### Parameters

##### signerAddress

`string`

##### messages

readonly `EncodeObject`[]

##### memo

`string` \| `undefined`

#### Returns

`Promise`\<`number`\>

#### Inherited from

`SigningCosmWasmClient.simulate`

***

### simulateBankTransferTx()

> **simulateBankTransferTx**(`toAddress`, `amount`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:250](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L250)

Usage:

```ts
const amount = coin(1, 'unls');
const {
    txHash,
    txBytes,
    usedFee
} = await wallet.simulateBankTransferTx('nolusAddress', [amount]);
const item = await wallet.broadcastTx(txBytes);
```

#### Parameters

##### toAddress

`string`

##### amount

`Coin`[]

#### Returns

`Promise`\<`any`\>

***

### simulateClaimRewards()

> **simulateClaimRewards**(`data`, `lppContracts`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:380](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L380)

#### Parameters

##### data

`object`[]

##### lppContracts

`string`[]

#### Returns

`Promise`\<`any`\>

***

### simulateDelegateTx()

> **simulateDelegateTx**(`data`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:307](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L307)

#### Parameters

##### data

`object`[]

#### Returns

`Promise`\<`any`\>

***

### simulateExecuteContractTx()

> **simulateExecuteContractTx**(`contract`, `msgData`, `funds?`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:278](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L278)

Usage:

```ts
const downpayment = coin(1, 'ibc/....');
const msg = {
 open_lease: {
     currency: 'OSMO',
 },
};
const {
    txHash,
    txBytes,
    usedFee
} = await wallet.simulateExecuteContractTx('leaserAddress', msg, [downpayment]);
const item = await wallet.broadcastTx(txBytes);
```

#### Parameters

##### contract

`string`

##### msgData

`Record`\<`string`, `any`\>

##### funds?

`Coin`[] = `[]`

#### Returns

`Promise`\<`any`\>

***

### simulateRedelegateTx()

> **simulateRedelegateTx**(`data`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:325](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L325)

#### Parameters

##### data

`object`[]

#### Returns

`Promise`\<`any`\>

***

### simulateSendIbcTokensTx()

> **simulateSendIbcTokensTx**(`__namedParameters`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:289](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L289)

#### Parameters

##### \_\_namedParameters

###### amount

`Coin`

###### memo?

`string` = `''`

###### sourceChannel

`string`

###### sourcePort

`string`

###### toAddress

`string`

#### Returns

`Promise`\<`any`\>

***

### simulateTx()

> **simulateTx**(`msg`, `msgTypeUrl`, `memo?`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:57](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L57)

#### Parameters

##### msg

`MsgSend` \| `MsgExecuteContract` \| `MsgTransfer` \| `MsgDelegate` \| `MsgBeginRedelegate` \| `MsgUndelegate` \| `MsgVote` \| `MsgWithdrawDelegatorReward`

##### msgTypeUrl

`string`

##### memo?

`string` = `''`

#### Returns

`Promise`\<`any`\>

***

### simulateUndelegateTx()

> **simulateUndelegateTx**(`data`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:344](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L344)

#### Parameters

##### data

`object`[]

#### Returns

`Promise`\<`any`\>

***

### simulateWithdrawRewardTx()

> **simulateWithdrawRewardTx**(`data`): `Promise`\<`any`\>

Defined in: [src/wallet/NolusWallet.ts:362](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L362)

#### Parameters

##### data

`object`[]

#### Returns

`Promise`\<`any`\>

***

### transferAmount()

> **transferAmount**(`receiverAddress`, `amount`, `fee`, `memo?`): `Promise`\<`DeliverTxResponse`\>

Defined in: [src/wallet/NolusWallet.ts:193](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L193)

#### Parameters

##### receiverAddress

`string`

##### amount

`Coin`[]

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`DeliverTxResponse`\>

***

### undelegateTokens()

> **undelegateTokens**(`delegatorAddress`, `validatorAddress`, `amount`, `fee`, `memo?`): `Promise`\<`DeliverTxResponse`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:164

#### Parameters

##### delegatorAddress

`string`

##### validatorAddress

`string`

##### amount

`Coin`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`DeliverTxResponse`\>

#### Inherited from

`SigningCosmWasmClient.undelegateTokens`

***

### updateAdmin()

> **updateAdmin**(`senderAddress`, `contractAddress`, `newAdmin`, `fee`, `memo?`): `Promise`\<`ChangeAdminResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:154

#### Parameters

##### senderAddress

`string`

##### contractAddress

`string`

##### newAdmin

`string`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`ChangeAdminResult`\>

#### Inherited from

`SigningCosmWasmClient.updateAdmin`

***

### upload()

> **upload**(`senderAddress`, `wasmCode`, `fee`, `memo?`, `instantiatePermission?`): `Promise`\<`UploadResult`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:151

Uploads code and returns a receipt, including the code ID

#### Parameters

##### senderAddress

`string`

##### wasmCode

`Uint8Array`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

##### instantiatePermission?

`AccessConfig`

#### Returns

`Promise`\<`UploadResult`\>

#### Inherited from

`SigningCosmWasmClient.upload`

***

### useAccount()

> **useAccount**(): `Promise`\<`boolean`\>

Defined in: [src/wallet/NolusWallet.ts:180](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/wallet/NolusWallet.ts#L180)

#### Returns

`Promise`\<`boolean`\>

***

### withdrawRewards()

> **withdrawRewards**(`delegatorAddress`, `validatorAddress`, `fee`, `memo?`): `Promise`\<`DeliverTxResponse`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:165

#### Parameters

##### delegatorAddress

`string`

##### validatorAddress

`string`

##### fee

`number` \| `StdFee` \| `"auto"`

##### memo?

`string`

#### Returns

`Promise`\<`DeliverTxResponse`\>

#### Inherited from

`SigningCosmWasmClient.withdrawRewards`

***

### connect()

> `static` **connect**(`endpoint`, `options?`): `Promise`\<`CosmWasmClient`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:56

Creates an instance by connecting to the given CometBFT RPC endpoint.

This uses auto-detection to decide between a CometBFT 1.x, CometBFT 0.38 and Tendermint 0.37 client.
To set the Comet client explicitly, use `create`.

#### Parameters

##### endpoint

`string` \| `HttpEndpoint`

##### options?

`CosmWasmClientOptions`

#### Returns

`Promise`\<`CosmWasmClient`\>

#### Inherited from

`SigningCosmWasmClient.connect`

***

### connectWithSigner()

> `static` **connectWithSigner**(`endpoint`, `signer`, `options?`): `Promise`\<`SigningCosmWasmClient`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:131

Creates an instance by connecting to the given CometBFT RPC endpoint.

This uses auto-detection to decide between a CometBFT 1.x, CometBFT 0.38 and Tendermint 0.37 client.
To set the Comet client explicitly, use `createWithSigner`.

#### Parameters

##### endpoint

`string` \| `HttpEndpoint`

##### signer

`OfflineSigner`

##### options?

`SigningCosmWasmClientOptions`

#### Returns

`Promise`\<`SigningCosmWasmClient`\>

#### Inherited from

`SigningCosmWasmClient.connectWithSigner`

***

### create()

> `static` **create**(`cometClient`, `options?`): `CosmWasmClient`

Defined in: node\_modules/@cosmjs/cosmwasm/build/cosmwasmclient.d.ts:62

Creates an instance from a manually created Comet client.
Use this to use `Comet38Client` or `Tendermint37Client` instead of
auto-detection.

#### Parameters

##### cometClient

`CometClient`

##### options?

`CosmWasmClientOptions`

#### Returns

`CosmWasmClient`

#### Inherited from

`SigningCosmWasmClient.create`

***

### createWithSigner()

> `static` **createWithSigner**(`cometClient`, `signer`, `options?`): `SigningCosmWasmClient`

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:137

Creates an instance from a manually created Comet client.
Use this to use `Comet38Client` or `Tendermint37Client` instead of
auto-detection.

#### Parameters

##### cometClient

`CometClient`

##### signer

`OfflineSigner`

##### options?

`SigningCosmWasmClientOptions`

#### Returns

`SigningCosmWasmClient`

#### Inherited from

`SigningCosmWasmClient.createWithSigner`

***

### offline()

> `static` **offline**(`signer`, `options?`): `Promise`\<`SigningCosmWasmClient`\>

Defined in: node\_modules/@cosmjs/cosmwasm/build/signingcosmwasmclient.d.ts:147

Creates a client in offline mode.

This should only be used in niche cases where you know exactly what you're doing,
e.g. when building an offline signing application.

When you try to use online functionality with such a signer, an
exception will be raised.

#### Parameters

##### signer

`OfflineSigner`

##### options?

`SigningCosmWasmClientOptions`

#### Returns

`Promise`\<`SigningCosmWasmClient`\>

#### Inherited from

`SigningCosmWasmClient.offline`
