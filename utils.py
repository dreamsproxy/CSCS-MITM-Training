import subprocess

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
        if "w" in item:
            iface_dict["wireless"] = item
        elif "enp" in item:
            iface_dict["ethernet"] = item
        elif "eth" in item:
            iface_dict["ethernet"] = item
        else:
           print("\nSomething went wrong!")
           print("DEBUG:\n")
           raise "item does not exist"
    
    print(iface_dict)
    #print(iface_list)
    
    #with open("interfaces.dat", "w") as outfile:
    #    outfile.writelines(iface_list)
    
    return iface_dict
