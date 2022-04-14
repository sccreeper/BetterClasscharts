import requests
import validators
import json

from kivy.logger import Logger

import globals
from api import SYNC_ENDPOINT, HTTP_PROTOCOLS

#Called when sync is changed/started
def start_sync():
    
    globals.CURRENT_CONFIG["sync_url"] = globals.screen_manager.get_screen("SyncScreen").ids.server_url.text

    #Make sure the URL is valid

    if not (validators.domain(globals.CURRENT_CONFIG["sync_url"].split(":")[0]) or validators.ipv4(globals.CURRENT_CONFIG["sync_url"].split(":")[0]) or validators.ipv6(globals.CURRENT_CONFIG["sync_url"].split(":")[0])):
        globals.screen_manager.get_screen("SyncScreen").ids.text = "Server URL invalid!"
        return

    #Check if the server actually exists.

    for protocol in HTTP_PROTOCOLS:
        
        try:

            r = requests.get(f"{protocol}://{globals.CURRENT_CONFIG['sync_url']}{SYNC_ENDPOINT.PING}")

            loaded = json.loads(r.text)

            if loaded["success"] == 1:
                init_sync()
            else:
                pass #TODO: Error handle this
        except:
            continue

#Called when app is started and when sync is enabled/started for the first time.
def init_sync():
    
    Logger.info("Sync API: Connecting to sync server...")


def enable_sync(state):
    #Set config

    globals.CURRENT_CONFIG["sync_enabled"] = state
