# Bismuth Plugins - Doc & API

## File architecture

The plugins live in a "plugin" subdirectory of the Bismuth node.  
Each plugin has its own directory.  
For instance:
plugins/
plugins/010_webhook/
plugins/100_test_block/
plugins/110_test_status

A plugin directory is formated as `000_pluginname`. The numerical prefix acts as a priority level. Lowest prio gets run first.  
Priorities of 000-099 are reserved for low level plugins.  
100-199 for demo and example plugins.  
900-999 for test plugins.
In each plugin directory, at least one `__init__.py` file containing the plugin code is needed.

## Mechanism

All plugins from the `plugins/` directory are loaded at node launch. Then their (optional) init function is called.  
Here is the prototype of that function:

```
def action_init(params):
    print("Init Demo")
```

The name `action_init` can't be edited. This function can be used to init any lib or object the plugin would need later on.  
If no init is required, this function can be safely ommited.

Each action hook uses the same formalism.  
a "whatever" action hook will trigger every function named `def action_whatever(params):` in any loaded plugin.

Params is usually a dict, which content depends on the specific hook.

## Current Action Hooks

### block
> Triggered on every new digested block (can be a lot when catching up after down time)

See `100_test_block` demo plugin.

```
def action_block(block):
    print("Got New Block {}".format(json.dumps(block)))
```

block dict example content:
```
{"height": 664760, "diff": 111.0051389824, 
 "hash": "68fd1b772858b216c4c5a5c6e0cb7966648ee893916407a2eb74087c", 
 "action": "block"}
```

Possible uses:
* alert on diff change
* feed pool / miner with latest block info to avoid polling

Possible upgrade: Maybe will also embed the miner address for that block.

### fullblock
> Triggered on every new digested block (can be a lot when catching up after down time)

Same as block, but does also have a "transactions" dict entry with full list of the block transactions.

Possible uses:
* any action on a new transaction event

This is the most complex hook for now, it can do a looooot of things. Demo and plugins will follow.  
Just a few:  
* anonymous but secure params settings for pools.
* Functions as a service, with possible payment, on the chain. Distributed super computer.
* Being paid for custom value added API
* Digital goods auto delivery

### status
> Called every 30 seconds, when displaying console status.

See `110_test_status` demo plugin.

```
def action_status(status):
    print("Got New Status: {}".format(json.dumps(status)))
```

status dict example content:
```
{
"protocolversion": "mainnet0016", "walletversion": "4.2.4.71", "testnet": false, 
"blocks": 664681, "timeoffset": 0, "connections": 22, "difficulty": 111.00461903, 
"threads": 46, "uptime": 3547,
"consensus": 664681, "consensus_percent": 90.9090909090909, 
"last_block_ago": 14
}
```

Possible uses:
* alert on a specific block
* alert when too few connections
* trigger a mail when diff drops below a certain level
* alarm if last_block ago is too old (means node is no more synced)
* ...

## Current Filter Hooks

TBD

## Future hooks

WIP
