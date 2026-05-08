[**@nolus/nolusjs**](../../../../README.md)

***

[@nolus/nolusjs](../../../../README.md) / [NolusContracts](../README.md) / Treasury

# Class: Treasury

Defined in: [src/contracts/clients/Treasury.ts:19](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Treasury.ts#L19)

The most important role of this single instance smart contract is to calculate rewards in uNLS depending on the TVL of all LPPs,
and to distribute it to each LPP.

Usage:

```ts
import { NolusClient, NolusContracts } from '@nolus/nolusjs';

const cosm = await NolusClient.getInstance().getCosmWasmClient();
treasuryInstance = new NolusContracts.Treasury(cosm, treasuryContractAddress);
```

## Constructors

### Constructor

> **new Treasury**(`cosmWasmClient`, `contractAddress`): `Treasury`

Defined in: [src/contracts/clients/Treasury.ts:23](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Treasury.ts#L23)

#### Parameters

##### cosmWasmClient

`CosmWasmClient`

##### contractAddress

`string`

#### Returns

`Treasury`

## Methods

### calculateRewards()

> **calculateRewards**(): `Promise`\<`number`\>

Defined in: [src/contracts/clients/Treasury.ts:37](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Treasury.ts#L37)

Gets the calculated the amount of uNLS rewards to be distributed across all active LPPs.

The value is determined based on the current total value locked (TVL) in each pool.
This function returns the total reward amount but does not perform the distribution itself.

#### Returns

`Promise`\<`number`\>

A `Promise` resolving to:
- The total reward amount (as a number) in micro-NLS (`uNLS`) to be distributed.
