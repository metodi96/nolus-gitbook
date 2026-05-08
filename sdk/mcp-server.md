# MCP Server

The Nolus MCP server exposes the `@nolus/nolusjs` library as **tools that AI assistants can use** to interact with the Nolus Protocol — through Cursor, Claude Desktop, or any client that speaks the [Model Context Protocol](https://modelcontextprotocol.io/).

The server runs locally on your machine and bridges the assistant to the chain via the SDK.

## Tools

### Query tools (read-only)

Fetch state from the chain. Safe to call without any user confirmation.

| Tool | What it returns |
|---|---|
| `get_protocols` | List of all registered protocols. |
| `get_protocol` | Protocol details and contract addresses. |
| `get_platform` | Platform-level contracts (treasury, timealarms). |
| `get_lease_quote` | Quote for opening a leveraged position. |
| `get_open_leases` | All active leases for a wallet. |
| `get_leaser_config` | Current Leaser configuration. |
| `get_lease_status` | Status of a specific lease. |
| `get_lpp_balance` | Liquidity pool balance. |
| `get_lpp_config` | Pool configuration. |
| `get_lpp_price` | nLPN receipt token price. |
| `get_lender_deposit` | Lender's deposit balance. |
| `get_lender_rewards` | Lender's pending rewards. |
| `get_deposit_capacity` | Remaining deposit capacity. |
| `get_lpn` | Pool's native asset ticker. |
| `get_oracle_prices` | All asset prices. |
| `get_asset_price` | Price of a specific asset. |
| `get_currencies` | All supported currencies. |
| `get_oracle_config` | Oracle configuration. |
| `calculate_rewards` | NLS rewards distribution. |
| `get_wallet_balance` | Token balance for an address. |
| `get_block_height` | Current block height. |
| `get_chain_id` | Chain ID. |

### Prepare tools (build unsigned transactions)

These tools **do not sign or broadcast**. They return a transaction message and a ready-to-use `nolusd tx ...` CLI command, which the user reviews and runs themselves.

| Tool | Builds |
|---|---|
| `prepare_open_lease` | Lease opening transaction. |
| `prepare_repay_lease` | Lease repayment transaction. |
| `prepare_close_lease` | Lease close (full or partial). |
| `prepare_change_close_policy` | Stop-loss / take-profit update. |
| `prepare_deposit_lpp` | Deposit into liquidity pool. |
| `prepare_withdraw_lpp` | Withdrawal from liquidity pool. |
| `prepare_claim_lpp_rewards` | NLS rewards claim. |
| `prepare_transfer_tokens` | Bank send transaction. |

## Network configuration

The server ships with built-in configs for both networks:

- **Mainnet (Pirin)** — `network: "pirin"` (default).
- **Testnet (Rila)** — `network: "rila"`.

Most tools accept an optional `network` parameter so you can target a specific chain per request. Omit it to use Pirin.

You can override the defaults via environment variables:

| Variable | Description | Network |
|---|---|---|
| `NOLUS_PIRIN_RPC_URL` | Pirin RPC endpoint | mainnet |
| `NOLUS_PIRIN_ADMIN_ADDRESS` | Pirin Admin contract address | mainnet |
| `NOLUS_PIRIN_CHAIN_ID` | Pirin chain ID (used in generated CLI commands) | mainnet |
| `NOLUS_RILA_RPC_URL` | Rila RPC endpoint | testnet |
| `NOLUS_RILA_ADMIN_ADDRESS` | Rila Admin contract address | testnet |
| `NOLUS_RILA_CHAIN_ID` | Rila chain ID | testnet |

## Connecting from Cursor or Claude Desktop

Add the server to your MCP client's configuration (adjust the absolute path to the cloned `nolus.js` repo):

```json
{
  "mcpServers": {
    "nolus": {
      "command": "npx",
      "args": ["tsx", "/absolute/path/to/nolus.js/src/mcp/server.ts"],
      "env": {}
    }
  }
}
```

Restart your editor or Claude Desktop. The server will appear under MCP settings, and the assistant will surface the query and prepare tools listed above.

## Running it manually

```sh
npm run mcp
```

To override the built-in network settings, export the env vars before running:

```sh
export NOLUS_PIRIN_RPC_URL=https://rpc.nolus.network
export NOLUS_PIRIN_ADMIN_ADDRESS=nolus1gurgpv8savnfw66lckwzn4zk7fp394lpe667dhu7aw48u40lj6jsqxf8nd
export NOLUS_PIRIN_CHAIN_ID=pirin-1
npm run mcp
```

## Reference prompt for AI agents

Use this prompt as a system instruction for an agent that needs to interact with Nolus end-to-end (set up the server, install `nolusd`, configure the chain client):

```text
You are a Nolus Protocol agent. Before doing anything else, ensure the
environment is ready:

## Step 1: Set up the Nolus MCP server
- Clone the nolusjs library: `git clone https://github.com/nolus-protocol/nolus.js`
- Install dependencies: `cd nolus.js && npm install`
- Register the following MCP server in your client's configuration:
  - Command: `npx tsx <absolute-path-to-nolus.js>/src/mcp/server.ts`
  - Environment variables:
    - NOLUS_PIRIN_RPC_URL=https://rpc.nolus.network
    - NOLUS_PIRIN_ADMIN_ADDRESS=nolus1gurgpv8savnfw66lckwzn4zk7fp394lpe667dhu7aw48u40lj6jsqxf8nd
    - NOLUS_PIRIN_CHAIN_ID=pirin-1
- Reload your MCP tools so the server is available

## Step 2: Install nolusd if not already available
- Detect OS and architecture
- Download the appropriate binary from the latest release at
  https://github.com/nolus-protocol/nolus-core/releases/latest
- Install it to a directory on your PATH and make it executable
- Verify with `nolusd version`

## Step 3: Configure nolusd
- `nolusd config set client chain-id pirin-1`
- `nolusd config set client node https://rpc.nolus.network:443`

Confirm setup is complete and list any existing keys with `nolusd keys list`.
You are now ready to interact with Nolus Protocol.
```
