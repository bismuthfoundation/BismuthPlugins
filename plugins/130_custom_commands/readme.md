# 130_custom_commands

Showcase how a plugin can easily add features and extra commands to a Bismuth node.

> This plugin requires 030_socket_client plugin to also be in the plugins directory.

## Demo

The demo adds 3 commands XTRA_test1, XTRA_echo, XTRA_echo2 with different parameters passing.

## Test client

You can test the demo plugin with a simple script like 
```
import socks
import connections

s = socks.socksocket()
s.settimeout(10)
s.connect(("127.0.0.1", 5658))

connections.send (s, "XTRA_test1", 10)
test1 = connections.receive (s, 10)
print("test1", test1)

connections.send (s, "XTRA_echo", 10)
connections.send (s, "Hi!", 10)
test2 = connections.receive (s, 10)
print("test2", test2)

connections.send (s, "XTRA_echo2 p1 p2 p3", 10)
test3 = connections.receive (s, 10)
print("test3", test3)
```

## Usage

Copy the plugin to a directory of your to edit.  
Keep in mind the directory format 000_plugin_name and the nnumbering https://github.com/bismuthfoundation/BismuthPlugins/tree/master/doc#file-architecture

Regular plugins should use numbers from 200 to 899

action_init, my_callback, filter_extra_commands_prefixes are generic functions you can keep as this.

- edit `PREFIX = "XTRA_"` to the functions prefix you want to define. Keep the ending _
- define your CUSTOMPREFIX_function() instead of the demo XTRA_ ones.
- at least a socket_handler param is needed, so you can send the answer back - if needed -
- use `MANAGER.execute_filter_hook('send_data_back', some_data, first_only=True)` to send your data back

The demo XTRA_ commands show various ways of providing params if needed:

## XTRA_test1

This command takes no param. Simply defining a function here with XTRA_ prefix makes it available to the node.

## XTRA_echo

"This command takes one param from an extra packet and echoes it back

## XTRA_echo2

This command takes inline param(s): XTRA_echo2 hello 2  

