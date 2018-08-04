"""
Plugin demo

Extended Status action Hook. Called every 30 sec when displaying console status.
Adds info about open files and sockets.
"""


import json
import os
import psutil

__version__ = '0.0.1'

MANAGER = None
PROCESS = None


def action_init(params):
    global MANAGER
    global PROCESS
    try:
        MANAGER = params['manager']
        if os.name == "posix":
            PROCESS = psutil.Process()
            limit = PROCESS.rlimit(psutil.RLIMIT_NOFILE)
            MANAGER.app_log.info("OS File limits {}, {}".format(limit[0], limit[1]))
            if limit[0] < 1024:
                MANAGER.app_log.error("Too small ulimit, please tune your system.")
                sys.exit()
            if limit[0] < 65000:
                MANAGER.app_log.warning("ulimit shows non optimum value, consider tuning your system.")
        else:
            app_log.warning("Non Posix system, requirements for extended status plugin are not satisfied.")
        MANAGER.app_log.warning("Init Extended Status Plugin")
    except:
        pass


def action_status(status):
    global MANAGER
    global PROCESS
    MANAGER.app_log.warning("Status: {}".format(json.dumps(status)))
    if PROCESS:
        of = len(PROCESS.open_files())
        fd = PROCESS.num_fds()
        co = len(PROCESS.connections(kind="tcp4"))
        MANAGER.app_log.warning("Status: {} Open files, {} connections, {} FD used.".format(of, co, fd))
        status['extended'] = {'of': of, 'co': co, 'fd': fd}
