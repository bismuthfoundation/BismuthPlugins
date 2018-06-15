"""
Plugin demo

IFTTT "maker" event Hook.
Allow simple IFTTT trigger by any other plugin
To be used by other plugins.

MANAGER.execute_action_hook('ifttt', {'event':'ifttt_event_name', 'value1':value1, 'value2':value2, 'value3':value3})
value keys are optional.
"""


import json
import requests
import threading


# You will find you maker key in your maker service:
# https://ifttt.com/maker_webhooks , then click "Documentation"
IFTTT_KEY = 'enter_your_own_key'

VERBOSE = False

# If True, will run each call in its own thread not to slow down main node code.
USE_THREADS = True


def _doit(params):
    """
    Can be launched from the main thread, or in its own.
    :param params:
    :return:
    """
    global IFTTT_KEY
    event = str(params.pop('event'))
    url = "https://maker.ifttt.com/trigger/{}/with/key/{}".format(event, IFTTT_KEY)
    requests.get(url, params)


def action_ifttt(params):
    """
    params is a dict
    - event : your ifttt event
    - value1: opt, extra value to pass
    - value2: opt, extra value to pass
    - value3: opt, extra value to pass
    :param params:
    :return:
    """
    global VERBOSE
    global USE_THREADS
    try:
        if VERBOSE:
            print("Got action_ifttt {}".format(json.dumps(params)))
        if USE_THREADS:
            server_thread = threading.Thread(target=_doit, args=(params,))
            server_thread.daemon = True
            server_thread.start()
        else:
            _doit(params)
    except Exception as e:
        raise ValueError("Exception on ifttt: '{}'".format(e))


