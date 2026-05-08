[**@nolus/nolusjs**](../../../../README.md)

***

[@nolus/nolusjs](../../../../README.md) / [NolusContracts](../README.md) / Lease

# Class: Lease

Defined in: [src/contracts/clients/Lease.ts:23](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L23)

Each Lease instance is an isolated margin position opened by a user.

Usage:

```ts
import { NolusClient, NolusContracts } from '@nolus/nolusjs';

const cosm = await NolusClient.getInstance().getCosmWasmClient();
leaseInstance = new NolusContracts.Lease(cosm, leaseContractAddress);
```

There are also methods for simulating contract operations in order to obtain preliminary information about the transaction.

## Constructors

### Constructor

> **new Lease**(`cosmWasmClient`, `contractAddress`): `Lease`

Defined in: [src/contracts/clients/Lease.ts:27](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L27)

#### Parameters

##### cosmWasmClient

`CosmWasmClient`

##### contractAddress

`string`

#### Returns

`Lease`

## Methods

### changeClosePolicy()

> **changeClosePolicy**(`nolusWallet`, `fee`, `stopLoss?`, `takeProfit?`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Lease.ts:148](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L148)

Adjusts the `stop_loss` (SL) and/or `take_profit` (TP) thresholds for the margin position.

These thresholds are expressed as LTV (loan-to-value) ratios in permilles.
To remove an existing stop-loss or take-profit, set the respective value to `null`.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet requesting the update.

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### stopLoss?

`number` \| `null`

Optional stop-loss threshold in permilles.

##### takeProfit?

`number` \| `null`

Optional take-profit threshold in permilles.

##### fundCoin?

`Coin`[]

Optional. Additional tokens to fund the transaction.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to the transaction result, including:
- Transaction hash, gas used, and emitted events for setting the SL/TP policy.

***

### closePositionLease()

> **closePositionLease**(`nolusWallet`, `fee`, `amount?`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Lease.ts:116](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L116)

Executes a partial or full market closure on an active position.

If an amount is specified, only that portion of the position is closed.
Otherwise, the full position is closed (swapping the entire position for the LPN - liquidity pool's native - asset).

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet initiating the close.

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### amount?

[`Asset`](../interfaces/Asset.md)

Optional. The amount of the lease asset to close (partial close).

##### fundCoin?

`Coin`[]

Optional. Additional tokens to fund the transaction.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to the transaction result, including:
- Transaction hash, gas used, and emitted events for the partial/full market closing.

***

### getLeaseStatus()

> **getLeaseStatus**(`dueProjectionSecs?`): `Promise`\<[`LeaseStatus`](../interfaces/LeaseStatus.md)\>

Defined in: [src/contracts/clients/Lease.ts:67](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L67)

Retrieves the current status of the margin position (lease).

Optionally, a projection time in seconds can be provided to estimate
the loan interest and protocol (margin) interest due at that point in the future.

#### Parameters

##### dueProjectionSecs?

`number`

Optional. Future projection time in seconds.

#### Returns

`Promise`\<[`LeaseStatus`](../interfaces/LeaseStatus.md)\>

A `Promise` resolving to the current lease state, including:
- The leased asset and size of the position.
- Principal and interest amounts due.
- Overdue amounts (if any) and repayment deadline.
- Applied loan and protocol interest rates.
- Close policy (`stop_loss`, `take_profit`) if set.
- Lease status (e.g. `"idle"`, `"opened"`, `"closed"`).

***

### repayLease()

> **repayLease**(`nolusWallet`, `fee`, `fundCoin?`): `Promise`\<`ExecuteResult`\>

Defined in: [src/contracts/clients/Lease.ts:86](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L86)

Executes a repayment toward the margin position’s outstanding debt.

The repayment may include interest and/or principal. Any party can repay the lease,
not just the original borrower.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet initiating the repayment.

##### fee

`number` \| `StdFee` \| `"auto"`

The gas fee for the transaction.

##### fundCoin?

`Coin`[]

The amount and denomination of tokens used for repayment.

#### Returns

`Promise`\<`ExecuteResult`\>

A `Promise` resolving to the transaction result, including:
- Transaction hash, gas used, and emitted repayment events.

***

### simulateChangeClosePolicyTx()

> **simulateChangeClosePolicyTx**(`nolusWallet`, `stopLoss?`, `takeProfit?`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Lease.ts:163](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L163)

Simulates a change to the `stop_loss` and/or `take_profit` thresholds
without executing the update.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet used for simulation.

##### stopLoss?

`number` \| `null`

Optional stop-loss threshold in permilles.

##### takeProfit?

`number` \| `null`

Optional take-profit threshold in permilles.

##### fundCoin?

`Coin`[]

Optional. Tokens to simulate as funding source.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to the simulated gas and fee estimate.

***

### simulateClosePositionLeaseTx()

> **simulateClosePositionLeaseTx**(`nolusWallet`, `amount?`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Lease.ts:129](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L129)

Simulates a partial or full close on an active lease.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet used for simulation.

##### amount?

[`Asset`](../interfaces/Asset.md)

Optional. The lease asset amount to simulate closing.

##### fundCoin?

`Coin`[]

Optional. Tokens to simulate as funding source.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to the simulated gas and fee estimate.

***

### simulateRepayLeaseTx()

> **simulateRepayLeaseTx**(`nolusWallet`, `fundCoin?`): `Promise`\<`any`\>

Defined in: [src/contracts/clients/Lease.ts:98](https://github.com/nolus-protocol/nolus.js/blob/7b8b473d0e21c0de222dcab779a844c2037e85da/src/contracts/clients/Lease.ts#L98)

Simulates a repayment toward the margin position without executing it.

#### Parameters

##### nolusWallet

[`NolusWallet`](../../../../classes/NolusWallet.md)

The wallet used for simulation.

##### fundCoin?

`Coin`[]

The amount of tokens to simulate as repayment.

#### Returns

`Promise`\<`any`\>

A `Promise` resolving to the simulated gas and fee data.
