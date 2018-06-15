"""
Demo token hooks plugin

token action Hook. Called on every token issuance or transfer
"""


import json

from tokensv2 import tokens_update

MANAGER = None
SEC30 = 0


def action_init(params):
    global MANAGER
    try:
        MANAGER = params['manager']
        MANAGER.app_log.warning("Init Demo token Plugin")
    except:
        # Better ask forgiveness than permission
        pass


def action_token_transfer(data):
    global MANAGER
    # {'token': token, 'from': sender, 'to': recipient, 'txid': txid, 'amount': transfer_amount}
    MANAGER.app_log.info("Token transfer: {}".format(json.dumps(data)))


def action_token_issue(data):
    # {'token': token_name, 'issuer': issued_by, 'txid': txid, 'total': total}
    MANAGER.app_log.info("Token issue: {}".format(json.dumps(data)))


def action_status(status):
    # This is called every 30 sec
    global SEC30
    global MANAGER
    SEC30 += 1
    if SEC30 >= 3:
        SEC30 = 0
        # MANAGER.app_log.warning("Updating tokens")
        tokens_update("static/index.db", "static/ledger.db", "normal", MANAGER.app_log, MANAGER)

