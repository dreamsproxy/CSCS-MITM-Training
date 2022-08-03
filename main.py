#from asyncio.windows_utils import Popen
from subprocess import Popen, PIPE, CalledProcessError, check_output
import sys
import shlex
import time

def wlan_interfaces(DEBUG):
    wireless_interfaces = []

    interfaces = check_output("ip a", shell=True)
    interfaces = interfaces.decode().split("\n")
    if DEBUG:
        print(interfaces[3])
    for i in interfaces:
        if "wlan" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wlx" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wifi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wi-fi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wi fi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        if "wireless" in i.lower():
            wireless_interfaces.append(i.split(": "))
    if len(wireless_interfaces) < 1:
        print("Could not find wireless inpsterface.")
        print("Please enter your wireless interface, please")
        target_interface = input(" >>> ")
        return target_interface
    else:
        print(wireless_interfaces)
        if DEBUG:
            for i in wireless_interfaces:
                print(i[0][1])
        print(wireless_interfaces)
        return wireless_interfaces[0][1]

def start_rogueAP(wlan_id, ethernet_id):
    ap_command = str(f"x-terminal-emulator -e 'sudo create_ap {wlan_id} {ethernet_id} TPE-Free'")
    wap_process = Popen(shlex.split(ap_command), stdout=PIPE)
    time.sleep(15)

    ws_command = str("x-terminal-emulator -e 'sudo tshark -k -i ap0'")
    #wireshark_process = Popen(shlex.split(ws_command), stdout=PIPE)
    print(wap_process.stdout)

    with Popen(ap_command, stdout=PIPE, universal_newlines=True, shell=True) as wap_p:
        for b in wap_process.stdout:
            print(b, end="")
        if wap_p.returncode != 0:
            raise CalledProcessError
def main():
    wlan = wlan_interfaces(False)
    ethernet = "enp0s3"
    start_rogueAP(wlan, ethernet)

if __name__ == "__main__":
    main()
