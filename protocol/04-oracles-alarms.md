# Oracles & Alarms

_Source: https://hub.nolus.io/en/articles/9680497-oracles-alarms_

[![](https://downloads.intercomcdn.com/i/o/hbjifswh/1527053201/a5e23598ff7205047445f8e6a67a/market_data_price_oracle.png?expires=1778234400&signature=ef527000f0843bfbbe07940096084b54a68719403662005278a4d8575ff79fa1&req=dSUlEcl7noNfWPMW1HO4zdPPJgFL26e4bnNal1KjFeSc8IPSpUcQGbwPDhxn%0AvcDY6BVRRd18SOLieEA%3D%0A)](https://downloads.intercomcdn.com/i/o/hbjifswh/1527053201/a5e23598ff7205047445f8e6a67a/market_data_price_oracle.png?expires=1778234400&signature=ef527000f0843bfbbe07940096084b54a68719403662005278a4d8575ff79fa1&req=dSUlEcl7noNfWPMW1HO4zdPPJgFL26e4bnNal1KjFeSc8IPSpUcQGbwPDhxn%0AvcDY6BVRRd18SOLieEA%3D%0A)

# Market Data Price Oracle

The Market Data Price Oracle is an on-chain service delivering real-time market prices to system components. It allows these components to receive notifications when prices reach predefined levels, with multiple price points available for monitoring per component.

## Market Data Price Feeder

The Market Data Price Feeder collects denomination pairs from the Market Data Price Oracle and fetches prices from Osmosis for the supported pairs. It averages the retrieved prices and updates the Oracle with the latest data feed at intervals, typically every few seconds. Only governance-approved feeders are permitted to actively contribute price data to the Oracle.

Supported currency pairs are configurable through governance, with the feeder's base currency set at initialization and unchangeable afterward. Pairs can be requested in reverse (e.g., A/B data is valid for a B/A request) and can span a resolution path (e.g., [A/C, B/C], or [A/C, C/B]).

## Price Calculation Algorithm

Price feeders use an Exponential Moving Average (EMA) algorithm to determine cryptocurrency pair prices, adding a security layer by prioritizing recent data. A discounting factor between 0 and 1 is applied, with higher values discounting older observations more quickly, unlike the equal-weight approach of a Standard Moving Average (SMA).

## Global Time Oracle

The Global Time Oracle is an on-chain timing mechanism that updates based on the latest Market Data Price Feed’s Tendermint block time. Its Global Time Alarm enables notifications when specific time thresholds are reached, ensuring synchronized timing across system components.

---

Related Articles

[Manage a Margin Position](https://hub.nolus.io/en/articles/9679883-manage-a-margin-position)
