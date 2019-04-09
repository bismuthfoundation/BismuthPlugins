"""
Extra commands Plugin

Demo Bismuth Plugin

Showcase the use of filter event to provide new commands to a node

Defines XTRA_test1, XTRA_echo and XTRA_echo2
"""

import json
import socket

__version__ = '0.0.1'


MANAGER = None

VERBOSE = True


# Convention is to have a prefix ending in _ , so prefix and subsequent commands are easily readable.
# Take care not to overload an existing command
PREFIX = "XTRA_"


def action_init(params):
    """Generic plugin init"""
    global MANAGER
    try:
        MANAGER = params['manager']
        MANAGER.app_log.warning("Init Extra commands demo Plugin")
    except:
        pass


def XTRA_test1(socket_handler):
    """This command takes no param. Simply defining a function here with XTRA_ prefix makes it available to the node."""
    MANAGER.app_log.warning("Extra command test1")
    data = "test1 answer"
    # We use 'send_data_back' filter from 035_socket client, so the core code is common to all plugins
    MANAGER.execute_filter_hook('send_data_back', {'socket': socket_handler, 'data': data}, first_only=True)


def XTRA_echo(socket_handler):
    """This command takes one param from an extra packet and echoes it back"""
    MANAGER.app_log.warning("Extra command echo")
    input = MANAGER.execute_filter_hook('receive_extra_packet', {'socket': socket_handler}, first_only=True)
    result = input['data']
    data = "You said {}".format(result)
    MANAGER.execute_filter_hook('send_data_back', {'socket': socket_handler, 'data': data}, first_only=True)


def XTRA_echo2(socket_handler, params):
    """This command takes inline param(s): XTRA_echo2 hello 2"""
    MANAGER.app_log.warning("Extra command test2")
    print(params)
    data = "Echo2, you said {}".format((',').join(params))
    MANAGER.execute_filter_hook('send_data_back', {'socket': socket_handler, 'data': data}, first_only=True)


def my_callback(command_name, socket_handler):
    """The magic is here. This is the generic callback handler answering to the extra command"""
    # This method could stay as this.
    MANAGER.app_log.warning("Got Extra command {}".format(command_name))
    if command_name in globals():
        # this allow to transparently map commands to this module functions with no more code
        globals()[command_name](socket_handler)

    elif ' ' in command_name:
        # An alternate way is to define commands with inline param(s) and a custom separator (here, a space)
        command_name, *params = command_name.split(' ')
        if command_name in globals():
            globals()[command_name](socket_handler, params)
    else:
        MANAGER.app_log.warning("Undefined Extra command {}".format(command_name))


def filter_extra_commands_prefixes(prefix_dict):
    """
    This is the initial - required - setup step.
    Easy peasy: just add our prefix(es) in the provided dict and send it back.
    """
    prefix_dict[PREFIX] = my_callback
    # More prefixes could go here
    return prefix_dict
