import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from PY3 import encryption
 
        encryption()
 
 
 
elif bit == "32bit":
 
        from py32 import encryption
 
 
        encryption()
 
 
 
