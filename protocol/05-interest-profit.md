# Interest & Profit

_Source: https://hub.nolus.io/en/articles/9680486-interest-profit_

## Interest Rate Derivation

The interest rate on margin positions is determined by the current utilization level of borrowed funds. Higher utilization - when a larger share of available funds is borrowed - results in a higher interest rate, while lower utilization brings the rate down. At present, the rate calculation is based solely on the borrower’s base utilization rate. Future plans include an enhanced algorithm that will also factor in variables such as asset capitalization, market trends, and asset volatility, relying on historical data points to provide asset-specific adjustments. This approach will create an asset risk framework that defines optimal utilization levels and base interest rates tailored to each asset type.

Additional parameters will further account for expected market dynamics, ensuring the interest model reflects a broader range of influences.

### Profit

The system features a profit instance per supported market (e.g., USDC long on Osmosis) that collects a protocol interest rate (e.g., 8%). While funds are primarily managed in LPN currencies, other supported currencies are also handled. For instance, if the collateral is in BTC and the position asset is in ETH, the resulting swap tax might be in either currency.

This Profit contract’s primary role is to gather, swap into NLS, and transfer the total to the Treasury account.

---

Related Articles

[Understanding Nolus Asset-Backed Margin Leverage](https://hub.nolus.io/en/articles/9679605-understanding-nolus-asset-backed-margin-leverage)[Open a Margin Leverage Position](https://hub.nolus.io/en/articles/9679877-open-a-margin-leverage-position)[Protocol Stats](https://hub.nolus.io/en/articles/9681234-protocol-stats)
