# Borrow

_Source: https://hub.nolus.io/en/articles/9680324-borrow_

[![](https://downloads.intercomcdn.com/i/o/hbjifswh/1525422239/df4178d952ca0bb82c78cdbd47f6/borrow.png?expires=1778234400&signature=526bb636e9a0fc7f6168aed438aed597431df5cc4a9da3ad1cbeb520ae7cdc66&req=dSUlE818n4NcUPMW1HO4zd6az9Wd3XajnZH6HBKoXv48zLA00wg2M%2FxRVAZi%0ASJdNcwFdDotPYRz7ZO0%3D%0A)](https://downloads.intercomcdn.com/i/o/hbjifswh/1525422239/df4178d952ca0bb82c78cdbd47f6/borrow.png?expires=1778234400&signature=526bb636e9a0fc7f6168aed438aed597431df5cc4a9da3ad1cbeb520ae7cdc66&req=dSUlE818n4NcUPMW1HO4zd6az9Wd3XajnZH6HBKoXv48zLA00wg2M%2FxRVAZi%0ASJdNcwFdDotPYRz7ZO0%3D%0A)

Each supported denomination has a dedicated Liquidity Providers’ Pool (LPP) instance that handles all borrow requests and repayments in that currency. The LPP calculates a fixed interest rate for each loan, tracks the total principal and interest due, and maintains records of all active loans. An LPP operates exclusively in its native currency - called the Liquidity Pool’s Native (LPN) denomination - and does not interact with other assets.

A factory contract creates all margin positions, with one such factory deployed per integrated market. Each factory is connected to a single LPP, and by extension, to a single native currency - the Liquidity Pool’s Native (LPN) asset, which can be either a stablecoin or a volatile token. For instance, if a user wants to borrow USDC to go long, they must submit a request to the factory linked to the LPP that uses USDC as its LPN.

**The factory smart contract is configured with a set of parameters that define the behavior and constraints of the margin positions it creates:**

|  |  |
| --- | --- |
| **Parameter** | **Definition** |
| Code ID | The identifier of the margin position smart contract used to initialize new positions |
| LPP Address | The address of the LPP smart contract tied to the specific factory instance |
| Protocol Interest Rate | The fixed interest portion collected by the protocol (e.g., 3%), 100% of which is used for buybacks |
| Max Liability | The maximum allowed liability ratio for a position. If this threshold is reached, the position becomes eligible for liquidation (e.g., 90%) |
| Healthy Liability | A predefined liability ratio below the max liability, used as the target value during liquidation procedures (e.g., 83%) |
| Initial Liability | The maximum loan-to-value (LTV) ratio at position creation. It must be lower than the healthy liability (e.g., 60%) |
| Minimum Position Size | The minimum value, denominated in the LPN, that a position must maintain to remain alive (e.g., 15 USDC) |
| Minimum Transaction Amount | The smallest allowable amount for executing a transaction within the position (e.g., 0.01 USDC) |
| Interest Due Period | The defined time window during which interest must be repaid. If the borrower fails to make a payment before the period ends, the owed interest is automatically deducted from the position via partial liquidation |
| Liability Reevaluation Interval | The frequency, in seconds, at which the “liability covered” invariant is checked (e.g., every 2 seconds). This includes projected interest and is used in price-based liquidation checks. |
| First Liquidation Warning Threshold | The first of three warning thresholds used to signal a risk of liquidation (e.g., 83.5%). Must be lower than the second threshold |
| Second Liquidation Warning Threshold | The intermediate warning level (e.g., 85%) must be lower than the third threshold |
| Third Liquidation Warning Threshold | The final warning (e.g., 87.5%) level before reaching the max liability threshold. Must be lower than the max liability |

A mathematical representation of “liability covered”:

```
Current Liability < Max Liability × Position Value (in LPN)
```

Example:

- Borrowed amount (loan): 150 USDC
- Initial position value: 250 USDC
- Liability: 150 / 250 = **0.60**
- Max allowed liability: **0.90**

If the position value drops to 200 USDC:  
→ Liability becomes 150 / 200 = **0.75** (still within limit)

If it drops further to 165 USDC:  
→ Liability becomes 150 / 165 ≈ **0.91**  
→ This exceeds the max liability of 0.90, breaking the invariant.

Once the invariant is violated, the position is flagged for liquidation.

# **Open a Margin Position**

To open a new margin position, the user interacts with the appropriate factory contract and provides collateral. The maximum borrowable amount is determined by the collateral and the configured initial liability ratio (e.g., 60%).

## Opening Flow

**1. Collateral Deposit**

The user initiates a position by submitting collateral to the factory. There are three ways to provide this collateral:

- **Directly in the target asset**: If the collateral matches the desired final asset of the position (e.g., a volatile token for longs or a stablecoin for shorts), no swap is required.
- **In the LPN currency**: The collateral is swapped via an integrated DEX (e.g., Osmosis) into the target asset for the position.
- **In a different volatile asset**: The collateral is also swapped via the DEX into the appropriate target asset.

The resulting asset determines the final size of the position. For long positions, the target asset is typically a volatile token, while for short positions, it's a stablecoin.  
​

**2. Position Creation**  
Upon receiving the collateral, the factory instantiates a new position contract. Only the factory has permission to create such contracts, and this is verified during contract creation.

### **Stored Data in a Position**

Each position contract stores a fixed set of parameters upon creation:

- **User** → The address of the borrower initiating the loan
- **Currency** → The loan currency, denominated in the Liquidity Pool’s Native (LPN) asset
- **Current Period** → The initial interest period, beginning at loan creation and ending on the first interest due date
- **Max Liability** → The upper limit for the loan-to-value ratio; crossing this threshold triggers liquidation
- **Healthy Liability** → The target liability ratio to restore the position to during liquidation
- **Initial Liability** → The starting loan-to-value ratio at the time of position creation
- **Liability Reevaluation Interval** → How often the liability invariant is checked for violations
- **Annual Protocol Interest** → The fixed protocol-level interest rate charged on the position
- **LPP Address** → The address of the associated LPP that issued the loan
- **Interest Due Date** → The timestamp indicating when the next interest payment is expected

ℹ️ These values are defined in the factory configuration and remain unchanged for the lifetime of the position. Any updates to a factory's configuration via governance proposals would only affect new positions opened after the change.

The maximum borrowable amount is computed based on the initial liability ratio and the provided collateral, using the following formula:

```
loan = initial_liability × (loan + collateral)   
loan = (initial_liability × collateral) / (1 - initial_liability)
```

Where:

- **Loan** → The amount lent to the borrower in LPN
- **Initial Liability** → The LTV ratio set by the factory for the position
- **Collateral** → The user’s deposit, priced in LPN

ℹ️ The total position size is the swapped sum of the borrowed amount and the collateral.

**3. Loan Request**  
Once the margin position contract is created, it initiates a loan request to the corresponding Liquidity Providers’ Pool (LPP). As a security measure, the LPP first verifies that the caller is a valid position contract created by the factory.

The LPP determines a fixed loan interest rate based on current pool utilization and the size of the requested loan. The formula used is:

```
Quoted Loan Interest Rate = Base Rate + (Utilization Factor / Optimal Utilization) × Add-on Rate
```

Where:

- **Base Rate** → The minimum interest rate, defined by the LPP
- **Utilization Factor** → A dynamic metric reflecting how much of the pool’s liquidity is currently in use. Calculated via this formula:

  ```
  Utilization Factor = Utilization / Idle Assets Portion
  ```
- **Optimal Utilization** → A target utilization level that caps the impact of increased borrowing
- **Add-on Rate** → A slope parameter that adjusts interest rate sensitivity beyond the base rate

Let’s assume the following values:

- **Utilization**: 60% (Respectively, utilization factor = 1.5)
- **Base Interest Rate**: 8%
- **Add-on Optimal Loan Interest Rate**: 2%
- **Optimal Utilization**: 70%

```
Quoted Loan Interest Rate = 8% + (1.5 / 0.7) × 2% ≈ 12.29%
```

ℹ️ Then, add the **protocol interest rate** (e.g., 4%) on top:

```
Effective Fixed Interest Rate = 12.29% + 4% = 16.29%
```

In addition, Nolus caps the interest rate if the utilization level goes above the optimal utilization threshold. In this scenario, the maximum utilization factor becomes ~2.33, so the maximum interest that a borrower would need to pay is fixed at ~18.67% as per the example above.   
​  
Once the rate is calculated, the LPP transfers the borrowed amount directly to the margin position’s smart contract address. The debt must be fully settled for the position to be closed.

Each time a loan is issued, the Liquidity Providers’ Pool (LPP) stores key data associated with the position:

|  |  |
| --- | --- |
| **Data Point** | **Definition** |
| Position Address | The address of the initialized margin position smart contract tied to the loan. |
| Principal Due (in LPN) | The outstanding loan principal, excluding any accrued interest. Initially, this equals the borrowed amount. |
| Annual Interest Rate | The fixed loan interest rate applied to the position, expressed as a percentage. This value does **not** include the protocol interest rate, which is set in the factory contract. |
| Interest Paid Timestamp | A timestamp recorded at contract creation, updated dynamically whenever an interest payment is made. |

A simplified step-by-step overview of the margin position opening process is illustrated in the diagram below.

[![](https://downloads.intercomcdn.com/i/o/hbjifswh/1525418863/39133f4419ee425aae3f73ba7395/open_lease.png?expires=1778234400&signature=9485260036f52856c28e65166554bfe7cefff2112bc63c6974d2ee63b51cde10&req=dSUlE81%2FlYlZWvMW1HO4zQTIjGPZ%2F%2FTXMoMQ0SwBXYb3%2BMCY6cYXUayxa9cw%0Aj1%2BPajEU2Bb%2FHm7aSYE%3D%0A)](https://downloads.intercomcdn.com/i/o/hbjifswh/1525418863/39133f4419ee425aae3f73ba7395/open_lease.png?expires=1778234400&signature=9485260036f52856c28e65166554bfe7cefff2112bc63c6974d2ee63b51cde10&req=dSUlE81%2FlYlZWvMW1HO4zQTIjGPZ%2F%2FTXMoMQ0SwBXYb3%2BMCY6cYXUayxa9cw%0Aj1%2BPajEU2Bb%2FHm7aSYE%3D%0A)

**4. Cross-Chain Interactions**  
Once the borrowed funds are deposited into the position contract, an Interchain Account (ICA) is opened on the target host network (e.g., Osmosis). An ICA behaves like a standard account on the host chain - it can perform actions such as staking, sending tokens, or voting, but unlike traditional accounts, it does not rely on private key signatures. Instead, it is controlled via the Inter-Blockchain Communication (IBC) protocol by a designated controller account - in this case, the margin position contract instance deployed on the Nolus chain.

To complete ICA registration, an IBC acknowledgment (ACK) must be received to confirm the successful delivery of the registration message. If the acknowledgment is not returned in time, a timeout is triggered, and the protocol automatically retries the operation in the next block.

Once the ICA is successfully registered, the next step is to initiate a cross-chain asset transfer. This “transfer out” moves both the collateral and the loan amount from the position contract to the host chain via an established IBC channel. Like registration, this step also requires acknowledgment before proceeding.

After the funds arrive on the host chain, a swap is performed to obtain the desired asset. Once the swap is complete, the margin position is officially opened.

ℹ️ ICA channels are unordered by default. If an action times out, the channel remains open—this design significantly reduces the load on relayer providers responsible for managing cross-chain operations between Nolus and supported networks.

**5. Opened**  
Once the margin position is activated, it enters the “Open” state. From this point forward, two primary actions can occur: the borrower either repays the debt or the position undergoes liquidation.

#### **Repayment Flow**

If the user initiates repayment using the same asset as the loan’s LPN (e.g., USDC for a USDC-denominated loan), the outstanding amount is reduced immediately.

If repayment is made in a different asset (e.g., ATOM), the following steps take place:

1. An **Interchain Account (ICA)** transfer is triggered to move the asset to the host network.
2. The asset is swapped on the host network into the LPN equivalent (e.g., ATOM → USDC).
3. The resulting LPN is bridged back to the Nolus chain via IBC.
4. Upon receiving all necessary acknowledgments, the system verifies whether the total loan has been repaid.

If the position still holds unpaid principal or interest after this process, it remains active.

#### **Liquidation Flow**

Alternatively, the position may be liquidated, either partially or in full, based on its liability state. In both cases:

1. The assets within the position are swapped to the owed LPN on the host chain.
2. The resulting LPN is bridged back to the Nolus network.
3. Each cross-chain step requires acknowledgment before continuing.

If the liquidation is partial, the position remains active. Full liquidation results in the debt being marked as repaid.

**6. Debt Covered**  
Once the total debt, including all interest and principal, has been either fully repaid or liquidated, the position status changes from **"Open"** to **"Paid"**.

At this point, the user can close the position by transferring the remaining assets to their own wallet. Once this transfer is completed and acknowledged, the position’s status updates to **"Closed"**.

The diagram below illustrates the complete state flow of a margin position - from creation through activation, repayment, or liquidation, and final closure.

[![](https://downloads.intercomcdn.com/i/o/hbjifswh/1525423573/e54c3e0eee644b21c995c852232a/lease_states.jpg?expires=1778234400&signature=051b8578a1707b776098688b9ab1af65f262fdd285292d4ee526618ef2bfb093&req=dSUlE818noRYWvMW1HO4zdXXfMrghPXvWn3LXufRcgpw0TM6Qyx0Kdf%2F6Csc%0AzFRVx6YhwfUnQP6CoWg%3D%0A)](https://downloads.intercomcdn.com/i/o/hbjifswh/1525423573/e54c3e0eee644b21c995c852232a/lease_states.jpg?expires=1778234400&signature=051b8578a1707b776098688b9ab1af65f262fdd285292d4ee526618ef2bfb093&req=dSUlE818noRYWvMW1HO4zdXXfMrghPXvWn3LXufRcgpw0TM6Qyx0Kdf%2F6Csc%0AzFRVx6YhwfUnQP6CoWg%3D%0A)

# **Query Position Status**

The status of any margin position can be queried at any time. There are four possible states:

- **Open** → The position is active, with outstanding interest and/or principal payments. Liquidation may occur in this state. The user should call `Repay` to reduce or fully settle the debt.
- **Paid** → The position is fully repaid—both principal and interest—but the remaining margin has not yet been withdrawn. The user must call `Close` to finalize the position.
- **Closed** → The position has been fully repaid and all assets have been withdrawn by the user. The contract is now inactive.
- **Liquidated** → The position has been fully liquidated. The contract is now inactive.

## **Return Values**

The following data points are returned when querying a position:

|  |  |
| --- | --- |
| **Field** | **Explanation** |
| Position Amount | The current asset balance held in the position contract. It reflects the sum of collateral and borrowed assets (post-swap), minus any liquidations or partial closings. |
| Loan Interest Rate | The interest rate paid to lenders, expressed in **permille (‰)**. |
| Protocol Interest Rate | The protocol’s interest rate used for buybacks, expressed in **permille (‰)**. |
| Principal Due (in LPN) | The remaining principal that must be repaid, excluding any accumulated interest. Initially equal to the borrowed amount. |
| Protocol Interest Overdue | Any unpaid protocol interest past the due period. If left unpaid, this will be deducted via partial liquidation. |
| Loan Interest Overdue | Any unpaid loan interest past the due period. This will be settled via partial liquidation if not repaid. |
| Protocol Interest Due | The total protocol interest accrued up to the current point in time. |
| Loan Interest Due | The total loan interest accrued up to the current point in time. |
| Take Profit Threshold | A loan-to-value (LTV) ratio at which the position is automatically closed to realize profit (empty by default). |
| Stop Loss Threshold | A loan-to-value (LTV) ratio at which the position is automatically closed to preserve capital (empty by default). |

# **Quote for Loan**

Users can query the factory contract to estimate potential loan terms based on a given collateral amount. This quote helps preview what a margin position would look like if opened under current conditions.

⚠️ Note: The quoted parameters may change by the time the position is opened, as they depend on the real-time utilization of the corresponding LPP, which directly affects the interest rate.

The returned quote includes:

- **Total** → The full size of the position, equal to **collateral + borrowed amount**
- **Borrowed** → The amount the protocol will lend to the user in LPN
- **Interest Rate** → The combined fixed rate, composed of:

  - **Loan interest rate** (goes to lenders)
  - **Protocol interest rate** (collected by the protocol for operations such as buybacks)

# **Repay and Close**

When repaying an active position, the protocol follows a strict repayment order to ensure all dues are handled correctly. The repayment amount is applied in the following sequence:

1. **Overdue protocol interest**
2. **Overdue loan interest**
3. **Protocol interest** due for the current period (if applicable)
4. **Loan interest** due to the LPP for the current period
5. **Principal repayment** to the LPP

If the user repays the **debt manually or partially closes** the position using funds held within the position contract, the outstanding liabilities are settled accordingly, but any remaining balance must be claimed manually. In this case, the borrower must initiate a `Claim` action to withdraw the leftover margin from the contract.  
​

However, if the position is **fully closed** - either via full repayment or full liquidation - the protocol automatically performs all necessary settlements:

- The total position value is converted into the LPN currency.
- The owed amount is transferred to the LPP to repay the debt.
- Any remaining funds are returned to the borrower without the need to claim manually.

This ensures a seamless experience in full close scenarios, while maintaining control and flexibility in partial settlement cases.

[![](https://downloads.intercomcdn.com/i/o/hbjifswh/1525419338/1f37a37bc249717c5d8ef32d3e7f/repay.png?expires=1778234400&signature=b2d0c8313fdaab905cae7efd655d6e980ea3cf9bcffff1bc5c6872cc9a203754&req=dSUlE81%2FlIJcUfMW1HO4zRfp47r%2BjOs9NoAQRZM43Bdz4Cv%2Bf1OfYD0OMGVc%0AmdsSkUCYBRrJKn26Ves%3D%0A)](https://downloads.intercomcdn.com/i/o/hbjifswh/1525419338/1f37a37bc249717c5d8ef32d3e7f/repay.png?expires=1778234400&signature=b2d0c8313fdaab905cae7efd655d6e980ea3cf9bcffff1bc5c6872cc9a203754&req=dSUlE81%2FlIJcUfMW1HO4zRfp47r%2BjOs9NoAQRZM43Bdz4Cv%2Bf1OfYD0OMGVc%0AmdsSkUCYBRrJKn26Ves%3D%0A)

#### **Manual Repayment Flow:**

1. **Repayment Initiation**  
   The borrower initiates repayment by calling the `Repay` function on the position contract. The repayment must currently be made in the LPN currency.
2. **Query Outstanding Debt**  
   The position contract fetches the following values from the connected LPP contract:

   - **Principal Due** → The full remaining principal that must be repaid
   - **Total Loan Interest Due** → The accumulated loan interest up to the current time

   Additionally, two variables are initialized:

   - **Change** → The portion of the repayment amount remaining after each step
   - **Loan Payment** → The total amount to be sent to the LPP to settle interest and principal
3. **Interest Due Period Enforcement**  
   Each borrower has a defined window (the "interest due period") during which outstanding interest must be paid.

   - If both protocol interest and loan interest are paid in full the due date is extended by the due period
   - If only part of the interest is paid, the period is proportionally extended.

     - Example: A 30-day period is extended by 15 days if 50% of the interest is paid at the deadline.
   - If the borrower fails to pay within the period, the protocol automatically performs a partial liquidation to cover the unpaid amount.
4. **Protocol Interest Settlement**  
   The contract checks how much of the protocol interest can be paid with the current change:

   - If the change is sufficient, the protocol interest is covered in full.
   - Otherwise, only a portion is paid, and the rest remains due.
5. **Loan Interest Settlement**  
   If change remains after protocol interest is handled, the position queries the LPP for the loan interest still owed.
6. **Update Change and Loan Payment**  
   The contract applies the remaining change toward the loan interest:

   - If fully covered, the interest due period is renewed.
   - The loan payment amount is updated accordingly.
7. **Principal Repayment**  
   Once all interest is settled, any remaining funds are applied to the outstanding principal.
8. **Refund and Cleanup**  
   If there is any remaining balance after covering all obligations:

   - The surplus is returned to the user.
   - The loan record is deleted from the LPP’s internal storage.
   - The borrower can now withdraw the entire margin from the position contract to their wallet via claiming.

#### **Full Position Closure via Market Close**

In a market close, the entire position is closed using only the funds already held within the position contract - no external capital is required from the borrower. This flow is typically triggered by the user or the protocol when the position needs to be fully settled on-chain, using the available collateral and loaned assets.

1. **Initiating the Market Close**  
   The user or the protocol initiates the full closure of the position. This operation instructs the position contract to settle all outstanding debt using internal funds (i.e., assets currently held in the position).
2. **Asset Conversion**  
   All assets in the position contract are converted to the LPN currency:

   - A swap of the whole amount occurs via the designated DEX on the host network.
   - These funds are then bridged back to Nolus via IBC, requiring proper acknowledgment to proceed.
3. **Debt Assessment**  
   Once the total position value is in LPN, the contract calculates:

   - Protocol Interest Due
   - Loan Interest Due
   - Principal Due
4. **Repayment from Internal Funds**  
   The contract settles the debt in the following order, using only the converted LPN:

   1. Outstanding protocol interest
   2. Outstanding loan interest
   3. Remaining principal

   This step is identical to the manual repayment flow, but all payments are sourced directly from the position’s internal balance.
5. **Loan Finalization**

   - If the internal funds fully cover all debts, the position is considered "**Paid"**.
   - The loan entry is deleted from the LPP's internal storage.
   - No `Repay` call is necessary from the user.
6. **Automatic Asset Distribution**

   - The remaining LPN (if any) after all debts are settled is automatically returned to the borrower.
   - Since the full position is being closed and all internal assets are already converted and redistributed, no manual claim is required.
7. **Position Status Update**  
   Once all processes are completed, the position status transitions directly from "**Open"** to "**Closed"**.

#### **Debt Repayment via Partial Close**

In a partial close, the borrower uses only the assets within the position to settle part or all of the outstanding debt. Unlike a full close, this does **not** automatically close the position. If the repayment covers the entire debt, the user must manually claim any excess funds remaining in the contract. This approach is useful when the borrower chooses to unwind part of the position without injecting external capital.

1. **Initiating the Partial Close**  
   The user triggers a partial close, specifying the portion of the position to be used for debt repayment. No external funds are involved - the assets are taken directly from the position contract.
2. **Internal Asset Conversion**  
   The specified portion of the position is:

   - Swapped into the LPN currency via a DEX on the host chain, if not already in LPN.
   - Bridged back to Nolus via IBC, pending proper acknowledgment.
3. **Debt Assessment**  
   The contract evaluates:

   - Protocol interest due
   - Loan interest due
   - Principal due
4. **Repayment Execution**  
   The converted LPN amount is applied to the debt in the following order:

   1. Protocol interest
   2. Loan interest
   3. Principal

   If the full debt is covered, the position status changes from "**Open"** to "**Paid"**. Otherwise, the position remains "**Open"**, but with a reduced liability.
5. **Remaining Balance Distribution**

   - If the converted amount exceeds the total debt (e.g., $120 used to cover $100), the surplus (e.g., $20 in LPN) is retained within the position contract.
   - The unused portion of the position (e.g., the remaining $80 in volatile or collateral assets) is also retained.
6. **Manual Claim Required**  
   Since the position is not automatically closed, the borrower must call `Claim` to retrieve:

   - Any excess LPN left after repayment
   - The remaining unutilized assets in the position

   Until claimed, these funds remain locked within the contract, and the position remains in status "**Paid".** Once they are claimed, the position's status changes to "**Closed"**.

---

Related Articles

[Understanding Nolus Asset-Backed Margin Leverage](https://hub.nolus.io/en/articles/9679605-understanding-nolus-asset-backed-margin-leverage)[Manage a Margin Position](https://hub.nolus.io/en/articles/9679883-manage-a-margin-position)[Interest & Profit](https://hub.nolus.io/en/articles/9680486-interest-profit)[Liquidations & Risk Framework](https://hub.nolus.io/en/articles/11378238-liquidations-risk-framework)
