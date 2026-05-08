# MCP Server

_Source: https://hub.nolus.io/en/articles/14005928-mcp-server_

## Overview

The Nolus ecosystem includes a Model Context Protocol (MCP) server, enabling AI tools and developer environments to interact with the protocol through a standardized interface.

MCP-compatible environments, such as Claude Code, Cursor, or custom agent frameworks, can connect to the server and access Nolus functionality as structured tools, without requiring custom API integrations.

## What the MCP Server Exposes

Through the MCP server, external applications can:

- Retrieve protocol configuration and supported markets
- Query oracle prices and lending pool balances
- Inspect active margin positions
- Generate transaction payloads to open, repay, or close positions
- Prepare deposits, withdrawals, and reward claims for liquidity pools

All via simple natural language prompts.

The server prepares transaction messages compatible with Nolus' Cosmos infrastructure. These messages are then signed through a wallet or CLI tool and broadcast to the network. Private keys are never exposed to the MCP server itself.

## Getting Started

Developers can explore the implementation at:

<https://github.com/nolus-protocol/nolus.js/tree/mcp/src/mcp>

To bootstrap a new environment, the following prompt can be given directly to a compatible AI agent:

```
You are a Nolus Protocol agent. Before doing anything else, ensure the environment is ready:  
  
## Step 1: Set up the Nolus MCP server  
- Clone the nolusjs library: `git clone https://github.com/nolus-protocol/nolus.js`  
- Install dependencies: `cd nolus.js && npm install`  
- Register the following MCP server in your client's configuration:  
  - Command: `npx tsx <absolute-path-to-nolus.js>/src/mcp/server.ts`  
  - Environment variables:  
    - NOLUS_RPC_URL=https://rpc.nolus.network  
    - NOLUS_ADMIN_ADDRESS=nolus1gurgpv8savnfw66lckwzn4zk7fp394lpe667dhu7aw48u40lj6jsqxf8nd  
    - NOLUS_CHAIN_ID=pirin-1  
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

The agent will handle cloning, installation, and configuration automatically. From there, it can query markets, inspect positions, and prepare transactions on your behalf.
