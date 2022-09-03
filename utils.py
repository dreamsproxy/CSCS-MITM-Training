import subprocess
import shlex
from ping3 import ping, verbose_ping

def gateway_detect(interface_list):
    gateway_interfaces = []
    for iface in interface_list:
        try:
            ping_return = ping("8.8.8.8", count=5, interface=iface)
            if isinstance(ping_return, float):
                print(ping_return)
                print(f"{iface} is internet acessible.")
                gateway_interfaces.append(iface)
            else:
                print("No internet accesible interfaces found!")
                print("EXITING, PLEASE CONTACT DEV  AT changfengjui@gmail.com")
                exit(1)

        except Exception as e:
            print("PING MODULE ERROR!\nCHECK EXCEPTION BELOW")
            print(e)

        return gateway_interfaces

def search_ifaces():
    iface_list = []
    iface_dict = {}
    interfaces = subprocess.check_output("ip a", shell=True)
    interfaces = interfaces.decode().split("\n")
    search_keys = ["wlan", "wlx", "wifi", "wi fi", "wi-fi", "enp", "eth0", "eth1"]

    for i in interfaces:
        preprocessed = i.lower().split(": ")
        for data in preprocessed:
            #print(data)
            if any(word in data for word in search_keys):
                if len(data) < 25:
                    iface_list.append(data)

    if len(iface_list) < 1:
        raise "No interfaces found!"
    for item in iface_list:
        """
        ping_command = f"ping -I {item} -c 5 google.com"
        ping_return = subprocess.check_output(shlex.split(ping_command), shell = True).decode()
        print(ping_return)
        if "Reply from " in ping_return:
            iface_dict["ethernet"] = item

        else:
            print("\nSomething went wrong!")
            print("DEBUG:\n")
            raise "item does not exist"
        """
        if "w" in item:
            if item not in iface_dict["ethernet"]:
                iface_dict["wireless"] = item
    print(iface_dict)
    #print(iface_list)

    #with open("interfaces.dat", "w") as outfile:
    #    outfile.writelines(iface_list)

    return iface_dict
