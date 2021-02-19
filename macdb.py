import json
import re

def normalize_mac(mac: str) -> str:
    mac = re.sub('[.:-]', '', mac).upper()
    mac = ''.join(mac.split())
    assert len(mac) == 12
    assert mac.isalnum()
    mac = ":".join(["%s" % (mac[i:i+2]) for i in range(0, 12, 2)])
    return mac

def ouiread(mac):
    with open("ouidump.json", "r") as ouidump:
        oui_json=ouidump.read()
    oui_dict = json.loads(oui_json)
    mac = normalize_mac(mac)
    for _ in range(9):
        try:
            mac = mac[:-1]
            return oui_dict[mac]
        except:
            print(mac)
