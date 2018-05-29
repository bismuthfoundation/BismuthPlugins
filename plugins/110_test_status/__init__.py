"""
Plugin demo

Status action Hook. Called every 30 sec when displaying console status
"""


import json


def action_init(params):
    print("Init Status Demo")


def action_status(status):
    print("Got New Status: {}".format(json.dumps(status)))
    """
    Example:
    {
    "protocolversion": "mainnet0016", "walletversion": "4.2.4.71", "testnet": false, 
    "blocks": 664681, "timeoffset": 0, "connections": 22, "difficulty": 111.00461903, 
    "threads": 46, "uptime": 3547,  # seconds
    "consensus": 664681, "consensus_percent": 90.9090909090909, 
    "last_block_ago": 14  # seconds
    }
    
    """
