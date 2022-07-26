import subprocess
import sys

def wlan_interfaces(DEBUG):
    wireless_interfaces = []

    interfaces = subprocess.check_output("ip a", shell=True)
    interfaces = interfaces.decode().split("\n")

    for i in interfaces:
        if "wlan" in i.lower():
            wireless_interfaces.append(i.split(": "))
        elif "wlx" in i.lower():
            wireless_interfaces.append(i.split(": "))
        elif "wifi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        elif "wi-fi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        elif "wi fi" in i.lower():
            wireless_interfaces.append(i.split(": "))
        elif "wireless" in i.lower():
            wireless_interfaces.append(i.split(": "))
        else:
            print("Could not find wireless interface.")
            print("Please enter your wireless interface, please")
            input(" >>> ")

    print(wireless_interfaces)
    if DEBUG:
        for i in wireless_interfaces:
            print(i[1])

    return i[1]

def start_rogueAP(wlan_id, ethernet_id):
    pass

def main():
    wlan_interfaces(True)

if __name__ == "__main__":
    main()