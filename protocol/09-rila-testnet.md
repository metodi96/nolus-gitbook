# Rila (Testnet) Services

_Source: https://hub.nolus.io/en/articles/9685743-rila-testnet-services_

[![](https://downloads.intercomcdn.com/i/o/1131521915/9542fdac53a70949fef1257e/1692797747600-nolus_core_header-min.jpg?expires=1778234400&signature=2d663a0872f26e0732a5acee7dfb60337d3366e3bac0c19e41980ce19a31bfcd&req=dSEkF8x8nIheXPMW1HO4zWW67%2FHw6DO2aA0tHojxLFQjnUQc2%2BlcgvU2cgqU%0A2cEGH%2B2qynX0HjkHKDw%3D%0A)](https://downloads.intercomcdn.com/i/o/1131521915/9542fdac53a70949fef1257e/1692797747600-nolus_core_header-min.jpg?expires=1778234400&signature=2d663a0872f26e0732a5acee7dfb60337d3366e3bac0c19e41980ce19a31bfcd&req=dSEkF8x8nIheXPMW1HO4zWW67%2FHw6DO2aA0tHojxLFQjnUQc2%2BlcgvU2cgqU%0A2cEGH%2B2qynX0HjkHKDw%3D%0A)

The current Nolus testnet, Rila (rila-3), launched on 25th of June, 2024, at 07:28 UTC. Please see the instructions below on how to start and operate a Rila blockchain service.

🚰 To get Rila testnet tokens, check out the **#testnet-faucet** channel in our Discord server! (Note: the faucet is currently under maintenance. If you need testnet NLS, ask in the **#testnet-chat** channel)

## Full Node

## **System Configuration**

Usually, you should be able to run a node on an operating system of your choice. You will be able to compile the Nolus daemon on most modern Linux distributions and recent versions of macOS. However, this tutorial uses commands available in the Ubuntu LTS release. If you are using a different operating system, you might need to adjust the commands you will see. Running a full node on the Nolus blockchain is a resource-intensive process that requires a persistent server since you would need to store all the information on the blockchain and constantly be in sync with the other network participants. It is also a prerequisite for being a validator.

### **Hardware Requirements**

The recommended hardware to run a Nolus node will vary depending on the node's use case and desired functionalities. For example, if the node acts as an archive, meaning that it stores all the historical data of the blockchain dating back to the genesis block, it would naturally require a lot of storage (disk space). The recommended by us minimum requirements to run a full node are the following:

- 4+ vCPU
- 16+ GB RAM
- 240+ GB SSD

**Prerequisites:** Golang go1.23.4 linux/amd64 Linux users

```
sudo apt-get install -y build-essential
```

Nolus core is the official Golang reference implementation used for a node. Follow this guide to install Nolus core which will allow you to use **nolusd**. **nolusd** stands for Nolus Daemon and is the command-line interface (CLI) and daemon that enables you to interact with the Nolus blockchain.

## **Build Nolus Core**

**1. Use Git to Clone the Nolus Core Repository**

```
git clone https://github.com/Nolus-Protocol/nolus-core
```

​**2. Make Sure That You Are in the “Core” Directory**

```
cd nolus-core
```

​**3. Check Out the Main Branch Containing the Latest Stable Release**

💡 If you want to sync from block 1, then feel free to checkout the initial version of the rila-3 testnet. The other option is to start from a snapshot. In that case, you would need to checkout the latest version which you can find on the bottom of the explorer's main page: <https://testnet.ping.pub/nolus>

```
git checkout [latest version]
```

*ex., git checkout v0.6.7*

**4. Compile the Nolus Core and Install It**

```
make install
```

##

**5. Verify That Nolus Core Is Installed Correctly by Checking the Version**

```
nolusd version --long
```

You should see a similar output as the one shown in the example below:

```
name: nolus server_name: nolusd version: [version_of_nolusd] commit: [commit_hash] build_tags: netgo ledger go: go version go1.21.5 linux/amd64
```

⚠️ If the nolusd: **command not found** error message is returned, run the following command to confirm whether the Go binary path has been successfully defined: `export PATH=$PATH:$(go env GOPATH)/bin`

## **Configuration and Execution**

**1. Initialize a Nolus Node**

```
nolusd init [custom_moniker]
```

*ex., nolusd init “My first Nolus node”*

This command initializes your node in a .nolus directory using the $HOME path by default. It adds a number of configuration files such as `config.toml` and `app.toml` which are to be modified in the next steps.

⚠️ Make sure to use ASCII characters for your node’s name (moniker) and not Unicode. The name is important if you are running a validator since in this case, it would be visible to the other participants. You can update your node’s moniker by editing the moniker field in `~/.nolus/config/config.toml`

**2. Obtain the Genesis File and Set Persistent Peers**

Retrieve the genesis state file from the **Nolus Repository** or another trusted source. This is a file that contains details with regard to the initial state of the network. There are details about governance, staking, account balances, slashing, etc.

```
wget https://raw.githubusercontent.com/nolus-protocol/nolus-networks/main/testnet/rila-2/genesis.json
```

Override the default genesis file in your Nolus node directory with the correct one you retrieved via the above command.

```
mv ./genesis.json ~/.nolus/config/genesis.json
```

ℹ️ You can view the persistent peers to connect to on Rila here:<https://github.com/nolus-protocol/nolus-networks/blob/main/testnet/rila-3/peers.txt>

You would need to connect to at least one of them to sync with the current state of the network. They are specified in the form `<NODE-ID>@<IP-ADDRESS>:<PORT>`. Export them in a variable:

```
PEERS="$(curl -s "<https://raw.githubusercontent.com/nolus-protocol/nolus-networks/main/testnet/rila-3/peers.txt")">
```

Set them in the `~/.nolus/config/config.toml` file:

```
sed -i.bak -e "s/^persistent_peers *=.*/persistent_peers = \"$PEERS\"/" ~/.nolus/config/config.toml
```

##

**3. Edit Configuration Files**

​ **3.1 Adjust the minimum gas price:**

Open `~/.nolus/config/app.toml`

Modify the minimum-gas-prices field to set a minimum gas price threshold that your validator would be willing to accept in order to prevent spam attacks:

```
minimum-gas-prices = "0.025unls”
```

ℹ️ Bear in mind that a portion of the fees paid by the user gets diverted to the Nolus Protocol. With that in mind, you would need to take into account the fee rate that is applied as tax. On genesis, it would be 40%.

**3.2 (Optional) Configure the application state pruning:**

Open `~/.nolus/config/app.toml`. By default, the application will keep the application data for a time horizon that matches the unbonding period (21 days in blocks) and prune the remaining application state.

If you want to prune the entire application state, set:

```
pruning = "everything”
```

If you want to keep the entire application state (relevant for archive nodes), set:

```
pruning = "nothing”
```

##

**4. Set Up Cosmovisor (Recommend)**

⚠️ Using Cosmovisor is optional. It helps you automate downloading binaries for chain upgrades by monitoring the governance module. This significantly reduces the downtime of your node in such cases. Otherwise, you would need to manually download the new binary, stop the current binary, switch from the old binary to the new one, and finally restart the node with the new binary.

**4.1 Install Cosmovisor**

You can get the latest version of Cosmovisor from the official GitHub repository of the Cosmos SDK

```
go install cosmossdk.io/tools/cosmovisor/cmd/cosmovisor@latest
```

**4.2 Include environment variables**

In the `.profile` file, usually located at `~/.profile`, add:

```
export DAEMON_NAME=nolusd export DAEMON_HOME=$HOME/.nolus export MONIKER_NAME=<the-name-of-your-node>
```

Source your profile to have access to this variable via:

```
source ~/.profile
```

**4.3 Adjust folder layout**

$DAEMON\_HOME/cosmovisor is expected to belong completely to Cosmovisor and the subprocesses that are controlled by it. The folder content is organized as follows:

Do not worry about the **current** directory. It is a symbolic link to the currently active directory (i.e. genesis or upgrades/<name>). The other folders can be set up using:

```
mkdir -p $DAEMON_HOME/cosmovisor/genesis/bin mkdir -p $DAEMON_HOME/cosmovisor/upgrades
```

**4.4 Set up genesis binary**

Cosmovisor would need to know which binary to choose at genesis. You need to copy your Nolus node binary and paste it into the directory Cosmovisor expects:

```
cp /home/<your-user>/go/bin/nolusd $DAEMON_HOME/cosmovisor/genesis/bin
```

**4.5 Set up a service**

If an error or reboot happens, we want to make sure that Cosmovisor would automatically restart and not have to manually do it ourselves, since commands sent to the Cosmovisor are automatically directed at the underlying binary. For this reason, we set up a service by creating first a .service file:

```
sudo nano /etc/systemd/system/cosmovisor.service
```

Change the contents below to match your user. Double check if the paths below match yours:

```
[Unit] Description=cosmovisor After=network-online.target [Service] User=<your-user> ExecStart=/home/<your-user>/go/bin/cosmovisor run start Restart=always RestartSec=3 LimitNOFILE=4096 Environment="DAEMON_NAME=nolusd" Environment="DAEMON_HOME=/home/<your-user>/.nolus" Environment="DAEMON_ALLOW_DOWNLOAD_BINARIES=false" Environment="DAEMON_RESTART_AFTER_UPGRADE=true" Environment="DAEMON_LOG_BUFFER_SIZE=512" [Install] WantedBy=multi-user.target
```

##

**5. Run Your Node**

**5.1 If you have NOT set up Cosmovisor you can simply run the binary using the command below:**

```
nolusd start
```

**5.2 If you have set up Cosmovisor, you need to first enable the Cosmovisor service and then run it:**

```
sudo -S systemctl daemon-reload sudo -S systemctl enable cosmovisor sudo systemctl start cosmovisor
```

Check whether it is running by entering:

```
sudo systemctl status cosmovisor
```

If you need to monitor the service after launch, you can view the logs using:

```
journalctl -u cosmovisor -f
```

After starting the **nolusd** daemon, the chain will begin to sync to the network. The time to sync to the network will vary depending on your setup and the current size of the blockchain, but it could take a very long time. Use the following command to query the status of your node:

```
curl http://localhost:26657/status | jq .result.sync_info.catching_up
```

If it returns true, then your node is still syncing. If it returns false, your node has caught up to the current state of the network, and you are safe to upgrade your node to a validator.

##

**6. Run Your Node From A Snapshot (Optional)**

Alternatively, you can bootstrap your Nolus node by utilizing a snapshot service provided by a third-party node provider. In general, make sure to double-check the source and contents of the data that you are downloading.

ℹ️ Snapshots allow a new node to join the network relatively quickly by recovering the application state from a backup file instead of having to sync from the start. A snapshot contains a compressed copy of the Nolus chain data and wasm directories.

You can start your node from a pruned snapshot provided by the Nolus team**.** Bear in mind that this snapshot is suitable for running a validator node but not for an RPC one:  
​

[Testnet Snapshot](https://snapshots.nolus.network/backup-rila/snapshots/rila/)

## Validator

**1. Create (Or Restore) A Local Key Pair**

Prior to creating your validator, you must first create your application key. Note that this is not your consensus key and will not be used for signing consensus votes. Instead, it is used to sign transactions

Create a new key pair

```
nolusd keys add <key-name>
```

Restore existing Nolus wallet by providing a BIP39 mnemonic

```
nolusd keys add <key-name> --recover
```

Get your public address from the keystore

```
nolusd keys show <key-name> -a
```

Feel free to replace <key-name> with a name of your choice

⚠️ After creating a new key, its information will be shown alongside the seed phrase. Make sure to write it down, as it is the only way to restore your keys.

**2. Upgrade to a Validator**

⚠️ Do not attempt to upgrade your node to a validator until the node is fully in sync after you have started the nolusd binary, as shown in the previous section.

Since you need to send a transaction to be part of the validator set, you need to have a small amount of NLS tokens in the wallet address you are using on your keyring. Once you have a positive balance, you can send the **create-validator transaction.** For this, you would need to specify validator-related details, such as self-stake and commission, in a JSON file (named validator\_details.json in the example below) that is to be passed as a parameter in the command:

```
Contents of validator_details.json:  
{  
	"pubkey": <your-nodes-public-key>,  
	"amount": "1000000unls",  
	"moniker": "<the-name-of-your-node>",  
	"identity": "<optional-identity-signature-keybase>",  
	"website": "<optional-validator-website>",  
	"security": "<optional-security-contact-email>",  
	"details": "<optional-validator-details>",  
	"commission-rate": "0.05",  
	"commission-max-rate": "0.1",  
	"commission-max-change-rate": "0.01",  
	"min-self-delegation": "1"  
}
```

```
nolusd tx staking create-validator validator_details.json --chain-id "rila-3" --fees 1000unls --from <key-name>
```

If you need further explanation for each of these validator-related parameters:

- the amount is the amount you will place in your own validator in unls as self-stake (in the example, 1000000unls is 1 NLS)
- the commission rate is the rate you will charge your delegates (in the example above, 5 percent)
- the commission-max-rate is the most you are allowed to charge your delegates (in the example above, 10 percent)
- the commission-max-change-rate is how much you can increase your commission rate in a 24-hour period (in the example above, 1 percent per day until reaching the max rate)
- min-self-delegation is a strictly positive integer that represents the minimum amount of self-delegated voting power your validator must always have. In the example above, this is equal to 1 NLS or 1000000unls
- the pubkey is the validator public key that could be obtained via running "nolusd tendermint show-validator"
- the chain-id is whatever chain-id you are working with (in the Nolus testnet case, it is rila-3)
- the fees is the gas fee used to send this create-validator transaction
- the from flag is the KEY\_NAME you created when initializing the key on your keyring

**3. Confirm That Your Validator Is Active**

If running the following command returns something, your validator is active:

```
nolusd query tendermint-validator-set | grep "$(nolusd tendermint show-address)”
```

You are looking for the bech32 encoded address in the `~/.nolusd/config/priv_validator.json` file with a nolusvalcons prefix

**4. Secure Your Keys**

In general, a Nolus validator needs to do two things:

- Sign and commit blocks (using the Tendermint Consensus key)
- Conduct on-chain operations such as voting on Governance proposals (using an Application Operator Key)

⚠️ Take good care of those two keys to mitigate hardware or software failures

## **Restore a Validator**

A validator can be completely restored on a new Nolus node with the following set of keys:

- The Consensus key, stored in `~/.nolus/config/priv_validator.json`
- The mnemonic to the validator wallet (application key)

⚠️ **Danger!** Before proceeding, ensure that the existing validator is not active. Double voting has severe slashing consequences

To restore a validator:

- Set up a full Nolus node synced up to the latest block. Check the previous section
- Replace the `~/.nolus/config/priv_validator.json` file of the new node with the associated file from the old node, then restart your node

## **Unjail a Validator**

If your validator fails to sign at least 5% of the last 10000 blocks, it will get jailed. To unjail it so that it can continue to sign blocks and respectively earn staking rewards, you can submit the following transaction:

```
nolusd tx slashing unjail --from <yourKey> --chain-id rila-3 --fees 500unls
```

## Relayer

An IBC (Inter-Blockchain Communication) relayer is an off-chain process responsible for relaying messages between two chains. It is a mandatory actor in the IBC network architecture. This is because blockchains are not passing messages directly to one another over the network. Instead, they create and store the data to be retrieved and used by a relayer to build the IBC messages and subsequently pass them to the destination chain via a dedicated channel

ℹ️ This page contains instructions on running a Hermes relayer, a Rust-based implementation. The other two popular but less preferred implementations are TS-based and go-based.

## **Hardware Requirements**

- 8-core (4 physical core), x86\_64 architecture processor
- 32 GB RAM (or equivalent swap file set up)
- 1TB+ nVME drives

**Prerequisites:** Before beginning, ensure you have a [Nolus full node](https://nolus.helpjuice.com/technical-documentation/run-rila-testnet-services/version/11?kb_language=en_US) running in the background. You could relay on the same machine or connect to the Osmosis and Nolus full nodes via a network. You will need **build-essential** and **git** installed to follow these instructions

Download the latest Osmosis binary. Check out <https://docs.osmosis.zone/overview/validate/joining-testnet> for a detailed setup guideline

Download the latest Neutron binary. Check out <https://docs.neutron.org/neutron/build-and-run/overview> for a detailed setup guideline

## **Hermes**

**1. Install Rust Dependencies**

Since we are relying on a Rust-based implementation, we would need to install some Rust dependencies first:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh source "$HOME/.cargo/env" sudo apt-get install pkg-config libssl-dev sudo apt install librust-openssl-dev build-essential git
```

**2. Configure Hermes**

Create the directory where you'll place the binary, clone the hermes source repository and build it using the latest release:

```
cargo install ibc-relayer-cli --bin hermes --locked mkdir -p $HOME/hermes git clone https://github.com/informalsystems/ibc-rs.git hermes cd hermes git checkout v1.9.0
```

Make a hermes “keys” directory, copy config.toml from the cloned repo to the .hermes directory:

```
mkdir -p $HOME/.hermes mkdir -p $HOME/.hermes/keys cp config.toml $HOME/.hermes
```

Check if hermes is installed properly by running:

```
hermes version
```

Edit the hermes **config.toml** file by including configurations for the two chains that you want to relay between, namely Nolus Rila testnet and Osmosis testnet:

```
nano $HOME/.hermes/config.toml
```

You would need to specify the hermes configurations for your two running nodes. Do not forget to remove the generated by default “chains” section with the example at the end of the file:

```
[[chains]]  
id = 'rila-3'  
rpc_addr = 'http://127.0.0.1:26657'  
event_source = { mode = 'push', url = 'ws://127.0.0.1:26657/websocket', batch_delay = '500ms' }  
grpc_addr = 'http://127.0.0.1:9090'  
rpc_timeout = '10s'  
account_prefix = 'nolus'  
key_name = 'hermes-nolus'  
store_prefix = 'ibc'  
default_gas = 5000000  
max_gas = 15000000  
gas_multiplier = 1.1  
max_msg_num = 30  
max_tx_size = 2097152  
clock_drift = '5s'  
max_block_time = '30s'  
trusting_period = '14days'  
memo_prefix = ''  
[chains.trust_threshold]  
numerator = '1'  
denominator = '3'  
[chains.gas_price]  
price = 0.025  
denom = 'unls'  
[chains.packet_filter]  
policy = 'allow'  
list = [  
	['transfer', 'channel-0'], # osmo-test-5  
	['transfer', 'channel-1'], # pion-1  
	['ica*', '*'], # allow relaying on all channels whose port starts with `ica  
]  
[chains.address_type]  
derivation = 'cosmos'  
  
[[chains]]  
id = 'osmo-test-5'  
rpc_addr = 'http://127.0.0.1:26557'  
event_source = { mode = 'push', url = 'ws://127.0.0.1:26557/websocket', batch_delay = '500ms' }  
grpc_addr = 'http://127.0.0.1:9091'  
rpc_timeout = '10s'  
account_prefix = 'osmo'  
key_name = 'hermes-osmosis'  
store_prefix = 'ibc'  
default_gas = 5000000  
max_gas = 15000000  
gas_multiplier = 1.1  
max_msg_num = 20  
max_tx_size = 209715  
clock_drift = '20s'  
max_block_time = '10s'  
trusting_period = '288000s'  
memo_prefix = ''  
[chains.trust_threshold]  
numerator = '1'  
denominator = '3'  
[chains.gas_price]  
price = 0.025  
denom = 'uosmo'  
[chains.packet_filter]  
policy = 'allow'  
list = [  
	['transfer', 'channel-8272'],  
	['ica*', '*'], # allow relaying on all channels whose port starts with `ica  
]  
[chains.address_type]  
derivation = 'cosmos'  
  
[[chains]]  
id = 'pion-1'  
rpc_addr = '<rpc-address-of-your-neutron-testnet-node>'  
grpc_addr = '<grpc-address-of-your-neutron-testnet-node>'  
event_source = { mode = 'push', url = 'ws://<rpc-address-of-your-neutron-testnet-node>/websocket', batch_delay = '500ms' }  
rpc_timeout = '10s'  
account_prefix = 'neutron'  
key_name = 'hermes-neutron'  
store_prefix = 'ibc'  
default_gas = 5000000  
max_gas = 15000000  
gas_multiplier = 1.2  
max_msg_num = 20  
max_tx_size = 209715  
clock_drift = '20s'  
max_block_time = '10s'  
trusting_period = '1209600s'  
memo_prefix = ""  
ccv_consumer_chain = true  
[chains.trust_threshold]  
numerator = "1"  
denominator = "3"  
[chains.gas_price]  
price = 0.075  
denom = 'untrn'  
[chains.packet_filter]  
policy = 'allow'  
list = [  
	['transfer', 'channel-1061'],  
	['ica*', '*'], # allow relaying on all channels whose port starts with `ica  
]  
[chains.address_type]  
derivation = "cosmos"
```

Add your relayer wallet to hermes' keyring (located in `$HOME/.hermes/keys`). The wallet should have a positive balance on all the networks since the relayer would need to pay gas fees to submit IBC transactions

ℹ️ The best practice is to use the same mnemonic over all networks. Do not use your relaying addresses for anything else because it will lead to account sequence errors.

```
hermes keys add --chain rila-3 --mnemonic-file <hermes-seed-file> hermes keys add --chain osmo-test-5 --mnemonic-file <hermes-seed-file> hermes keys add --chain pion-1 --mnemonic-file <hermes-seed-file>
```

**3. Validate Configuration**

Validate your `~/.hermes/config.toml` file by running:

```
hermes config validate
```

Perform a health check:

```
hermes health-check
```

You should see a similar output as the one below:

```
... INFO ThreadId(01) [rila-3] chain is healthy INFO ThreadId(01) [osmo-test-5] chain is healthy INFO ThreadId(01) [pion-1] chain is healthy
```

**4. Run Hermes**

If your nodes are fully synced, feel free to start the hermes daemon:

```
hermes start
```

# IBC Transfer Channels for Nolus

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Source** | **Source Chain ID** | **Source Channel** | **Destination** | **Destination Chain ID** | **Destination Channel** |
| Nolus Rila Testnet | rila-3 | channel-0 | Osmosis Testnet | osmo-test-5 | channel-8272 |
| Nolus Rila Testnet | rila-3 | channel-1 | Neutron Testnet | pion-1 | channel-1061 |

In addition, by design, Nolus opens new ICA channels for each lease (borrow) position opened
