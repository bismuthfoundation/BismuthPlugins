# Bismuth Plugins - Doc & API

## File architecture

The plugins live in a "plugin" subdirectory.  
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

### fullblock

### status
Called every 30 seconds, when displaying console status.

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
