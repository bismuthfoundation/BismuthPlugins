"""
Plugin demo

"On Transaction" demo.
Calls a webhook upon specific transaction mining.
This will transmit all matching tx info

See https://github.com/bismuthfoundation/BismuthPlugins/blob/master/doc/How-to-Transaction.md

"""


import json

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
            print("GOT ONE!! {}".format(json.dumps(data)))
            MANAGER.execute_action_hook('webhook', {'url': URL, 'type': TYPE, 'data': data}, first_only=True)
