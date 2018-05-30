# How to react to an incoming transaction?

On many occasions, we want to execute a specific action when a transaction matching some criterions is mined.

This step by step tutorial will show you how to do that in just a few edit with Bismuth plugins.

## Plugin base

We could start from an existing plugin and modify it, but here we'll do it all by hand, don't worry.

* Create a directory for your plugin, under plugins. For instance, plugins/201_on_transaction
* Create an empty `__init__.py` file in this directory

## Useful hook

With Bismuth plugin system, you only need to create functions for hooks you will need.  
Here, we want to be notified of the new transactions. These transactions are in the "fullblock" action hook.

So, just declare the right prototype:
`def action_fullblock(full_block):`

Here is a "full_block" sample, it's a python dict :
```
    {'height': 666380, 'diff': 111.0796140403, 'hash': '6383573e87c44d8c889d5840be1d44237254bd8c0a2471caba73429f', 
    'transactions': [
        (666380, '1527699066.16', 'de98671db1ce0e5c9ba89ab7ccdca6c427460295b8dd3642e9b2bb96', 'de98671db1ce0e5c9ba89ab7ccdca6c427460295b8dd3642e9b2bb96', 0, 
        'g8hFG35uHyGM5VJwBeErkrnXXsPrqBwwlVMaz1DyVwinZiq0EmHQIAU9R6NYc3xJh4HGowtBBgMLGI2V9DnbMfTMVUnKDbmIBlwtqCy09OpRBBGAEUPQUyUNoZdL+k1WhVVsvhJFDvDct4QkvEcZcclJE7DeL8GbRBsntd2Zhc7dMd2ChrVSIgQDa5lZaphYn3nsjNEG1K1Q5aQzh6mYqtyZYYKlIzdQqobFzwoP0xACJnzf18JXeD9Ecaf8uyChn9gxrMwCCR9NDju7e04p93nhf3BB8N2fuwanIY19zbHJyXOILmYaH2c09oCwfHKAMMbUGvB6DaqOE52SUefOyqm/HYXYoV5ToKx5Mz6X73ZAXCGzwJFa1mXu/9MnEt3S98ZNvtoqJ+OxOcKxyifcKFFMpvGNt4SFdRATV8xe2BYqbDmXXrGU51YWWL0ajRNdIpMld09quu7sfxwL8tzjnZNIee7KldRlJSQmPTvvjL/TIZDUCdd4jrYTJUVOWpNLgElRUg9oGYIAfZzXyU7C1XeN1jiLD7NzXqcdJWBIIUTc6mYJiOvU7zoLbbbAG4U7lT3Fnlf0LRxL7rDOpQ5vJqaiITv7M5XUJEBwalsZSChG+OYKFTQq2y1gnnjkC/e6WLTiSqBLj5vr+NXI6XKlZ6BVuh7LSzvrJeOBFQ+4lko=',
        'LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUFuaitZbU1mQnUzb3J6bzRjZEpseQpvcVI1Y3JSdzRBL3VLTWtMT2MyYVByY1BIKzdyUTlObWZHWmpIQjkrZDRIdjBWZTVxRFdLWnBmZEhlR0JDSUhQCjY3cncrVE9VemtLM24rSVlrYmRtRG1aTmJjL09nTElFdUJWNUlXVEN4RG82ZE9TTm1KVlhaTWpFYnRVdFVmVTEKYndiYTgvMDc2MTFrTDAwRno1SVNaWFYzSm5wRXRXRnRBSkwvVFBoWkQ1VlZwZlF2eGlmL2h1M0JMZ2FYWEZlbQpaZVpXN0RUby9WMXNMRGNSeXFiQTBvUjlxYkpVcjlEMURRYm5wT1F1Tml6dVNLS2ROdzRBYlpVVkVQYWdCN2o4ClpKaldEbUM1c05Rd2NQeEx2dmVmT3BhQWhzZ1JqYjVFbkFyeVlOV3ZzVGJOeTNrMkNvdTRsdXFXV25mZ0ovTDcKS2IvQUE3VkhDZVJUd2E0VDdWVGtmMDJRUnBZaktCbWFHeHg5UzJXdHJRdXNJZVhFQlhNb0tuSVJpaW9GOCtHVwpVRCt0b1R2SWJQd1lWT21id0htMUFBQThKSnpZbCtTdFUyaXBwcEtkMEcwMnZwYmFJanpCbm5PYWRjWHk4QU1ZCnkwTStjVW8ybVZQckJmL29zN3pZVm9KdThBcWVFTE43UzlnZmdjdFRYNGRGekU4VTR1c0llVzQyRGFmaE8rRXAKZzNrTlJGOGpZcmhEczkzNWE4ajNBa3pzUTMvZC90Z0JSYUlxNGRjdDJJcWc5cW9rTGtDdWd5YW1HSTgwZ1lFego3aU1XSWZxQU9Kc0xBNEtCdU4ybXl6Zmt3TGFCRXNPNlY0MGh1R04xVEFxcExNYTR0ZE1xK3hySlJScE5sbTFUCjg1TW9sWnhyTEQ4UXpaYUR4NzRBclFNQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ==',
        '6383573e87c44d8c889d5840be1d44237254bd8c0a2471caba73429f', 0, Decimal('14.33362000'), '0', ')EGGPOol006c00000b4fed98ifoNc&J0')
        ]
    }
```
What we want is the 'transactions' list.  
it's index are:
* 0: block height
* 1: timestamp
* 2: from
* 3: to
* 4: amount
* 5: signature 
* 6: pubkey 
* 7: blockhash
* 8: fees
* 9: reward
* 10: operation
* 11: openfield

## Filter out the transactions we want

Say we want to act on incoming transaction to one address of ours only.  
Let's define that address and filter, our code now looks like:

```
# The bismuth address you want to watch
TARGET_ADDRESS = 'ed98671db1ce0e5c9ba89ab7ccdca6c427460295b8dd3642e9b2bb96'

def action_fullblock(full_block):
    global TARGET_ADDRESS
    for tx in full_block['transactions']:
        if tx[3] == TARGET_ADDRESS:
            # do something
```

We just parsed the transactions list, and compared the 'to' field to our address.

## Format as needed

A structured format would be better than a raw list, so let's convert this data:  
```
data = {'timestamp': tx[1], 'from': tx[2], 'to': tx[3], 'amount': str(tx[4]),
        'fees': str(tx[8]), 'reward': str(tx[9]), 'operation': tx[10], 'openfield': tx[11]}
```

> Note: the str() type conversion on amounts and reward is mandatory, or we could get some "Decimal" types that can't be properly serialized.

## Do not reinvent the wheel

Now that we have what we want, just send it.  
We could import requests, but well, calling an http hook is something we will do many times, do we want to copy-paste such code over and over again, and deal with things like calling the hook from a thread, so we won't slow the node down?

Hopefully, a webhook trigger is already present, as a plugin itself.

> Inception: Yes, you can call and run a plugin from within a plugin!

At init time, each plugin gets some params it's free to store and use. One of these params is the plugin manager.  
We just have to store it in a global variable, at module level. Here is the code snippet:

```
# We get the global plugin manager so we can use plugins (email, ifttt...) from inside plugins!
MANAGER = None


def action_init(params):
    global MANAGER
    try:
        MANAGER = params['manager']
    except:
        # Better ask forgiveness than permission
        pass
```

Once we did that, we can call any plugin at will (beware of dead locks!)  
In our case, the 010_webhook plugin does what we want.
Copy the 010_webhook directory under plugins so it's loaded, and then when you need to trigger a webhook, just do something like:  

`MANAGER.execute_action_hook('webhook', {'url': URL, 'type': TYPE, 'data': data}, first_only=True)`

You call an action hook, named 'webhook', and pass a dict() as param.  
* url is the http url to call.  
* type is 'GET' or 'POST'
* data is a dict of {'var': value} to send.

## The whole code

As you can see, the whole thing is quite short:

```
# We get the global plugin manager so we can use plugins (email, ifttt...) from inside plugins!
MANAGER = None

# Hook definition - Edit to your specific hook
TYPE = 'GET'
URL = 'http://127.0.0.1/transaction.php'

# The bismuth address you want to watch
TARGET_ADDRESS = 'ed98671db1ce0e5c9ba89ab7ccdca6c427460295b8dd3642e9b2bb96'


def action_init(params):
    global MANAGER
    try:
        MANAGER = params['manager']
    except:
        # Better ask forgiveness than permission
        pass


def action_fullblock(full_block):
    global TARGET_ADDRESS
    for tx in full_block['transactions']:
        if tx[3] == TARGET_ADDRESS:
            # This is ours, assemble data payload
            data = {'timestamp': tx[1], 'from': tx[2], 'to': tx[3], 'amount': str(tx[4]),
                    'fees': str(tx[8]), 'reward': str(tx[9]), 'operation': tx[10], 'openfield': tx[11]}
            MANAGER.execute_action_hook('webhook', {'url': URL, 'type': TYPE, 'data': data}, first_only=True)
```

You'll find that code in the 201_on_transaction folder, you can tweak it for your specific need.

# What next?

Since a webhook can do anything, so can you.  
Simple use could be to give the url of an IFTTT webhook, so you can trigger anything IFTTT supports (tweet, email, alert, add to dropbox...)  
Or you send that to your custom php dashboard, and deal with it.

## Concrete application

This is for my personal need, as a pool owner, but this is applicable to any Bismuth service operator.

I need my miners to tune some of their params. for instance, tell me what minimum payout they want.  
- I want something automatic
- I need something secure (must be sure whom is asking is the address owner)
- I don't want to bother with usernames, passwords, emails or any kind of additional auth. Would be silly!
- I want to service to stay fully anonymous (at least, pseudonymous)

With this, I can easily do it (and will asap).

- The miner uses his wallet to send a transaction, 0 BIS, with a specific message.  
  For eggpool, it will be 'set' as operation, and 'min_payout=1' as data. Seems clear enough?
- On my server, the node runs this very same plugin and filters these transactions.  
  Since the transactions are signed, I'm sure it comes from the owner of the address.  
  I don't even have to know him nor it's ip address to be 100% sure it's him.
- The webhook calls a specific url on the pool server, this one only accepts incoming data from known ips (the node server, or localhost), so it's secure.  
  The php code then update what needs to be pool side.
