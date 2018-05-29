# BismuthPlugins
Plugin API Documentation and demo plugins for Bismuth Nodes.

Bismuth is the first cryptocurrency and platform written from scratch, in Python.  
https://github.com/hclivess/Bismuth

## Need for plugin

Since Bismuth is entirely written in Python, it's easy to tweak, add features and test without compilation step.  
However this makes upgrades harder since the core code has to be modified and then edits have to be carefully merged.

The Bismuth plugin system, although very lightweight, allows for action and filter hooks on critical events, for easy feature addition.


## The plugin framework 

### Overview

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

### Activating / Deactivating plugins

As for now, all plugins present in plugins/ directory will be loaded.  
So, only place the ones you want to run.  
You can have a "plugins.available" directory and drop unused plugins there.

### Minimal plugin

A plugin wanting to implement a "block" action hook only has to declare a simple function:

`plugins/900_test/__init__.py`:
```
def action_block(block):
    print(block)
``` 

### Demo plugins

See [https://github.com/bismuthfoundation/BismuthPlugins/tree/master/plugins](plugins/) directory (WIP).

# Full API

The full API reference can be found in [https://github.com/bismuthfoundation/BismuthPlugins/tree/master/doc](doc/) directory (WIP).

# A word of caution

Current plugins are harmful (but may need some config to run properly).  
Future plugins could be more dangerous (like able to emit transactions). So, always make sure you trust the plugin source, and check its source code.  
Certified plugins will come later on.
