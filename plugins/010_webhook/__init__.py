"""
Plugin demo

Generic webhook action Hook. Allows IFTTT or other actions.
To be used by other plugins.

"""


import json
import requests
import threading


VERBOSE = False

# If True, will run each call in its own thread not to slow down main node code.
USE_THREADS = True

# global ID for json-rpc requests
ID = 0


def action_init(params):
    pass


def _get(url, data):
    requests.get(url, data)


def _post(url, data):
    requests.post(url, data)


def _jsonrpc(url, data):
    # TODO
    raise ValueError("Json-RPC not yet implemented")
    requests.post(url, data)


def _doit(params):
    """
    Can Do the right call. Can be launched from the main thread, or in its own.
    :param params:
    :return:
    """
    type = params['type'].upper()
    if 'POST' == type:
        _post(params['url'], params['data'])
    elif 'GET' == type:
        _get(params['url'], params['data'])
    elif 'JSON-RPC' == type:
        _jsonrpc(params['url'], params['data'])
    else:
        raise ValueError("Unknown webhook type")


def action_webhook(params):
    """
    params is a dict
    - url : url to call
    - type : GET, POST, JSON-RPC
    - data : a dict for GET or POST, the payload for JSON-RPC
    :param params:
    :return:
    """
    global VERBOSE
    global USE_THREADS
    try:
        if VERBOSE:
            print("Got action_webhook {}".format(json.dumps(params)))
        if USE_THREADS:
            server_thread = threading.Thread(target=_doit, args=(params,))
            server_thread.daemon = True
            server_thread.start()
        else:
            _doit(params)
    except Exception as e:
        raise ValueError("Exception on webhook: '{}'".format(e))
