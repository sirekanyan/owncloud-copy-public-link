#!/usr/bin/env python

import sys
import gnomekeyring

keyring = gnomekeyring
args = sys.argv[1:]

if len(args) != 1:
    exit(1)

for name in keyring.list_keyring_names_sync():
    for id in keyring.list_item_ids_sync(name):
        info = keyring.item_get_info_sync(name, id)
        attrs = keyring.item_get_attributes_sync(name, id)
        if args[0] == attrs.get('user', None):
            print info.get_secret()
            exit(0)
