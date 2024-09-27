"""
Pool Plugin

block action Hook. Called on every new block, sends new block info and diff drop to a proprietary pool server  
Used at eggpool.net, to be adapted for other context.

MIT License. 
Use at you own risks, credit eggpool.
"""

import json
import time
import socks

# ssdb is a redis compatible key-value store with on disk persistence.
import pyssdb

MANAGER = None
DIFF = 0
SSDB = None


def action_init(params):
    global MANAGER
    global SSDB
    try:
        MANAGER = params['manager']
        MANAGER.app_log.warning("Init Pool Plugin")
    except:
        # Better ask forgiveness than permission
        pass
    try:
        SSDB = pyssdb.Client(host="127.0.0.1", port=8888)
        MANAGER.app_log.warning("Found SSDB")
    except:
        MANAGER.app_log.warning("SSD Not found")
        SSDB = None


def action_block(block):
    global DIFF
    global SSDB
    print("  >> ", time.time(), "Got a New Block {}".format(json.dumps(block)))
    DIFF = block['diff']
    # block is a dict : {'height': 666380, 'diff': 111.0796140403, 'hash': '6383573e87c44d8c889d5840be1d44237254bd8c0a2471caba73429f',
    s = None
    try:
        # !! beware, diff0 diff1 above
        nb = (str(block['timestamp']), str(block['diff']), str(block['diff']), str(block['height']), block['hash'])
        nb = '|'.join(nb)
        # nb as in New Block. fields separated by a pipe.
        MANAGER.app_log.warning("New block {}".format(nb))

        s = socks.socksocket()
        s.settimeout(1)
        s.connect(('127.0.0.1', 8525))
        nb = 'nb|' + nb
        # The pool server uses the same protocol as Bis node: raw socket, len of msg + mesg
        s.sendall(str(len(str(json.dumps(nb)))).encode("utf-8").zfill(10) + str(json.dumps(nb)).encode("utf-8"))

        try:
            # This was for real time stats purposes only
            if SSDB:
                # beware, diff0 defined above.
                SSDB.hset('block', 'diff', str(block['diff']))
                SSDB.hset("block", "height", str(block['height']))
                SSDB.hset("block", "hash", str(block['hash']))
                # for api, last found block
                if block['miner'] in ('3d2...bc7',  'b54...3a', 'de...b96'):  # These were the addresses of the various pools, so we knew which blocks were ours or not.
                    SSDB.hset("pool", "height", str(block['height']))
                    SSDB.hset("pool", "timestamp", str(int(block['timestamp'])))
        except Exception as e:
            MANAGER.app_log.warning("Error setting SSDB " + str(e))

    except Exception as e:
        MANAGER.app_log.warning("Exception sending to local pool "+ str(e))
    finally:
        if s:
            s.close()


def action_diff(diff):
    global DIFF
    global SSDB
    # print("  >> ", time.time(), "Got New diff {}".format(diff))
    if True:  # int(diff) != int(DIFF):
        #print(">>>> DIFF CHANGED !!! <<<")
        s = None
        try:
            # !! beware, diff0 diff1 above
            nb = 'di|'+str(diff)
            # MANAGER.app_log.warning("New diff {}".format(diff))
            s = socks.socksocket()
            s.settimeout(1)
            s.connect(('127.0.0.1', 8525))
            s.sendall(str(len(str(json.dumps(nb)))).encode("utf-8").zfill(10) + str(json.dumps(nb)).encode("utf-8"))
            #try:
            #    if SSDB:
            #        SSDB.hset('block', 'diff', str(diff))
            #except Exception as e:
            #    MANAGER.app_log.warning("Error setting SSDB " + str(e))

        except Exception as e:
            MANAGER.app_log.warning("Exception sending to local pool "+ str(e))
        finally:
            if s:
                s.close()

