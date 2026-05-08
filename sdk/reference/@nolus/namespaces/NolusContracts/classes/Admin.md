[**@nolus/nolusjs**](../../../../README.md)

***

[@nolus/nolusjs](../../../../README.md) / [NolusContracts](../README.md) / Admin

# Class: Admin

Defined in: [src/contracts/clients/Admin.ts:19](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Admin.ts#L19)

The Admin contract is a contract that governs the storing and migration process of all smart contracts on the blockchain.

Usage:

```ts
import { NolusClient, NolusContracts } from '@nolus/nolusjs';

const cosm = await NolusClient.getInstance().getCosmWasmClient();
adminInstance = new NolusContracts.Admin(cosm, adminContractAddress);
```

## Constructors

### Constructor

> **new Admin**(`cosmWasmClient`, `contractAddress`): `Admin`

Defined in: [src/contracts/clients/Admin.ts:23](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Admin.ts#L23)

#### Parameters

##### cosmWasmClient

`CosmWasmClient`

##### contractAddress

`string`

#### Returns

`Admin`

## Methods

### getPlatform()

> **getPlatform**(): `Promise`\<[`PlatformContracts`](../interfaces/PlatformContracts.md)\>

Defined in: [src/contracts/clients/Admin.ts:66](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Admin.ts#L66)

Retrieves the global platform-level contract addresses.

 These are shared across all protocols and include system-level contracts like:
- `timealarms`: Contract handling time-based triggers
- `treasury`: The Treasury contract managing incentive and reserve flows

#### Returns

`Promise`\<[`PlatformContracts`](../interfaces/PlatformContracts.md)\>

A `Promise` resolving to:
- An object with platform-wide contract addresses.

***

### getProtocol()

> **getProtocol**(`protocol`): `Promise`\<[`Protocol`](../interfaces/Protocol.md)\>

Defined in: [src/contracts/clients/Admin.ts:52](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Admin.ts#L52)

Retrieves detailed configuration for a specific protocol.

The response includes the associated network and DEX, as well as the addresses
of all relevant contracts used by that protocol (leaser, LPP, oracle, etc.).

#### Parameters

##### protocol

`string`

The protocol identifier string (e.g. "OSMOSIS-OSMOSIS-USDC_NOBLE").

#### Returns

`Promise`\<[`Protocol`](../interfaces/Protocol.md)\>

A `Promise` resolving to:
- An object containing the network, DEX name, and contract addresses.

***

### getProtocols()

> **getProtocols**(): `Promise`\<`string`[]\>

Defined in: [src/contracts/clients/Admin.ts:37](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Admin.ts#L37)

Retrieves all registered protocol identifiers supported by the platform.

Each protocol entry represents a unique configuration for a network + DEX + LPN asset
(e.g. "OSMOSIS-OSMOSIS-ATOM" or "NEUTRON-ASTROPORT-USDC_NOBLE").

#### Returns

`Promise`\<`string`[]\>

A `Promise` resolving to:
- An array of protocol identifiers (strings).
