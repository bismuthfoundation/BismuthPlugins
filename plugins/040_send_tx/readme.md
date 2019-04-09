# 040_send_tx

Send TX plugin  
(BIS, Message, Token, RAW...)

This plugin is a generic low level plugin.  
The key to use is given by the caller, so this plugin alone is not a security risk.

It allows any other plugin to insert a tx into the node mempool.

For now, it uses the local mempool (has to be on disk mempool, not ram) or the local socket link.  
Future versions could use the waller servers api.

> Requires 035_socket_client plugin.

**Note**: This plugin is to be considered as experimental for now.  
It's used by the ico demo plugin.

## Usefulness

Embeds the tx assembling, signing, local wallet loading and low level node connection, so that code is tested and common to all plugins.

## Filters and action hooks

### filter_load_custom_keys(wallet_list)

Gets a list of wallet files location, and loads the matching keys into the related dicts.  
New wallet format only.

Use that filter to get the keys from your plugin

### filter_sign_tx(tx_dict)

Signs a tx with provided wallet.  
Wallet priv key is to be filled in tx_dict['wallet']['key']

### filter_send_tx_db(tx_dict)
Insert a signed tx into the local mempool db  
WARNING: since it's a direct insert, we have no feedback on the validity of the insert

### filter_send_tx(tx_dict)

Sends the signed tx to the local host via a mpinsert message, adds the answer in the result
