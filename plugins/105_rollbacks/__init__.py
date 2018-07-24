"""
Plugin demo

rollbacks and new blocks action Hook.

This plugin is intended to debug network sync and rollbacks.
It requires > 4.2.5.5 node version to benefit from the latest hooks.

Posted for reference only.
"""


import json
import time
import datetime


__version__ = '0.0.2'


ROLLBACK_LOG = "./rollback.log"
DO_PRINT = True
DO_LOG = True


def do_log(hook, data):
    """
    Append info from hook with timestamp to the file
    :param hook:
    :param info:
    :return:
    """
    the_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    with open(ROLLBACK_LOG, 'a') as f:
        f.write(the_time + "\t" + hook + "\t" + data + "\n")
    if DO_PRINT:
        print("\n>>  Got {} {}\n".format(hook, data))


def action_init(params):
    do_log("init", "Init rollbacks logging")


def action_block(block):
    do_log("block", json.dumps(block))


def action_rollback(info):
    do_log("rollback", json.dumps(info))


def action_mined(mined):
    do_log("mined", json.dumps(mined))


def action_digestblock(info):
    do_log("digestblock", json.dumps(info))


def action_sync(info):
    do_log("sync", json.dumps(info))

