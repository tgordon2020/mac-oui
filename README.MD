## macdb.py
* a simple python script to return OUI from MAC address
* import into existing code with *from macdb import ouiread*
* *print(ouiread("F4-30-B9-12-34-56"))* will return the vendor
* Not all OUIs are limited to 3 bytes, so the code starts at the full MAC address and works down until it finds a match.
