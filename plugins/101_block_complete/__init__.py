"""
Plugin demo

block action Hook. Called on every new block.
Show plugin call from within a plugin.
"""


import json

# We get the global plugin manager so we can use plugins (email, ifttt...) from inside plugins!
MANAGER = None

# TODO: use json config file ?
TYPE = 'GET'
URL = 'http://whatever/accepts/a/hook/'


def action_init(params):
    global MANAGER
    print("Init Block complete")
    try:
        MANAGER = params['manager']
    except:
        # Better ask forgiveness than permission
        pass
    # print(__file__)  # ./plugins/100_test_block/__init__.py


def action_block(block):
    global MANAGER
    print("Got New Block {}".format(json.dumps(block)))
    data = block
    data['action'] = 'block'
    MANAGER.execute_action_hook('webhook',{'url': URL, 'type': TYPE, 'data': data}, first_only=True)
