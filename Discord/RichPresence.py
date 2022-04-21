import json
from main import kanot_version
from pypresence import Presence

class RPC:
    id = 966468564024455198
    auto_start = None
    large_image = 'github-logo'
    large_text = 'beete.xyz/kanot'.format(kanot_version)

class RichPresence():
    def __init__(self):
        self.id = ''

    with open('Kanot/RPC.json') as f:
        get = json.load(f)
    try:
        if get['RichPresence']['true/false'] == 'true':
            Rich = Presence(RPC.id)
            Rich.connect()
        elif get['RichPresence']['true/false'] == 'false':
            pass
        else:
            pass
    except:
        pass