import network
import socket
from time import sleep
import machine
from picozero import pico_temp_sensor, pico_led
import sys

import mfrc522




def reload(mod):
    mod_name = mod.__name__
    del sys.modules[mod_name]
    return __import__(mod_name)


def read_rfid(rdr, mode=mfrc522.MFRC522.REQIDL):
    (status, tag_type) = rdr.request(mode)
    print("thing", status, tag_type)
    if status == rdr.OK:
        (stat, uid) = rdr.SelectTagSN()
        print(stat, uid)
        if stat == rdr.OK:
            card = int.from_bytes(bytes(uid), "little", False)
            return str(card)
        else:
            print(f"RFID reader problem. Status: {stat}")
    else:
        print(f"RFID reader problem. Status: {status}")
    return None



def connect(ssid=SSID, password=PASSWORD):


    # # Connect to WLAN
    # wlan = network.WLAN(network.STA_IF)
    # wlan.active(True)
    # wlan.connect(ssid, password)
    # while wlan.isconnected() == False:
    #     print("Waiting for connection...")
    #     sleep(1)
    # ip = wlan.ifconfig()[0]
    # print(f"Connected on {ip}")

    sta, ap = [network.WLAN(w) for w in (network.STA_IF, network.AP_IF)]
    sta.active(False); ap.active(False)  # Setting both inactive resets the esp8266 wifi stack and hardware
    sta.active(True); ap.active(False)  # Set interfaces to desired state
    sta.disconnect()  # Force the esp8266 to disconnect from the AP
    while sta.isconnected():
        sleep(0.1)  # Ensure is disconnected before continuing
    sta.connect(ssid, password)
    while not sta.isconnected():
        print("Waiting for connection...")
        sleep(0.1)  # Ensure is connected before continuing
    ssid, chan = sta.config("ssid"), ap.config("channel")
    ip = sta.ifconfig()[0]
    print(f'Connected to "{ssid}" on wifi channel {chan} on {ip}')

    return ip


def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def webpage(temperature, state):
    # Template HTML
    html = f"""
           <!DOCTYPE html>
           <html>
           <form action="./lighton">
           <input type="submit" value="Light on" />
           </form>
           <form action="./lightoff">
           <input type="submit" value="Light off" />
           </form>
           <p>LED is {state}</p>
           <p>Temperature is {temperature}</p>
           </body>
           </html>
           """
    return str(html)


def serve(connection):
    # Start a web server
    state = "OFF"
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == "/lighton?":
            pico_led.on()
            state = "ON"
        elif request == "/lightoff?":
            pico_led.off()
            state = "OFF"
        temperature = pico_temp_sensor.temp
        html = webpage(temperature, state)
        client.send(html)
        client.close()


# try:
#     ip = connect()
#     connection = open_socket(ip)
#     serve(connection)
# except KeyboardInterrupt:
#     machine.reset()
