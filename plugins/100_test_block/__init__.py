"""
Plugin demo

block action Hook. Called on every new block
"""


import json


def action_init(params):
    print("Init Block Demo")


def action_block(block):
    print("Got New Block {}".format(json.dumps(block)))


def action_fullblock(full_block):
    pass
    # print("Got New fullBlock {}".format(json.dumps(full_block)))
