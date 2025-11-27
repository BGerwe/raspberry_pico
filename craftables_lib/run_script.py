import gc
import network
from time import sleep
import requests

import interactive

SSID = 
PASSWORD = 
IQ_GATEWAY_IP = 

TOKEN = 

def print_memory():
    print(f"Board memory: {gc.mem_free()}")

# def 

interactive.connect(SSID, PASSWORD)

# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Authorization": f"Bearer {TOKEN}"
# }
headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Bearer {TOKEN}"}


data = {}

# res = requests.request("GET", "https://www.example.com", headers=headers, data=data)
# res = requests.request("POST", f"https://{IQ_GATEWAY_IP}/auth/check_jwt", headers=headers)
res = requests.request("GET", f"https://{IQ_GATEWAY_IP}/api/v1/production", headers=headers)

print(res.status_code)
print(res.text)
print(dir(res))
print(res.headers)
res.close()
gc.collect()
