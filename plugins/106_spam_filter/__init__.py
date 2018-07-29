"""
Plugin

Spam filter

This plugin is intended to filter out malicious actors on specific providers
It requires a recent node version to benefit from the latest hooks.
"""


import json
from ipwhois import IPWhois

# See https://stackoverflow.com/questions/24580373/how-to-get-whois-info-by-ip-in-python-3
from warnings import filterwarnings
filterwarnings(action="ignore")

__version__ = '0.0.1'


MANAGER = None


def action_init(params):
    global MANAGER
    global DESC
    try:
        MANAGER = params['manager']
        MANAGER.app_log.warning("Init Spam filter Plugin")
    except:
        pass
    DESC = {'127.0.0.1': 'localhost'}
    try:
        with open("ipresolv.json", 'r') as f:
            DESC = json.load(f)
    except:
        pass


def get_desc(ip):
    global DESC
    if ip in DESC:
        desc = DESC[ip]
    else:
        obj = IPWhois(ip)
        res = obj.lookup_whois()
        desc = res.get('asn_description')
        DESC[ip] = desc.lower()
    return desc


def filter_peer_ip(peer_ip):
    global DESC
    desc = get_desc(peer_ip['ip'])
    if 'amazon' in desc:
        MANAGER.app_log.warning("Spam Filter: Banned IP {}".format(peer_ip['ip']))
        peer_ip['ip'] = 'banned'
    return peer_ip


def action_status(status):
    global DESC
    # save new descriptions on status
    with open("ipresolv.json", 'w') as f:
        json.dump(DESC, f)
