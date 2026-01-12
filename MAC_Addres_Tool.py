ٍimport subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-e", dest="Network", help="Network Interface")
    parser.add_option("-m", dest="MAC_Address", help="New MAC Address")

    options, arguments = parser.parse_args()

    if not options.Network:
        parser.error("[-] Please specify a network interface, use -e")
    if not options.MAC_Address:
        parser.error("[-] Please specify a MAC address, use -m")

    return options


def change_mac(interface, mac):
    print(f"[+] Changing MAC address for {interface} to {mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface], text=True)
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
    if mac_search:
        return mac_search.group(0)
    else:
        return None


options = get_arguments()
current_mac = get_current_mac(options.Network)
print(f"[i] Current MAC = {current_mac}")

change_mac(options.Network, options.MAC_Address)

current_mac = get_current_mac(options.Network)
if current_mac == options.MAC_Address:
    print(f"[+] MAC address successfully changed to {current_mac}")
else:
    print("[-] MAC address did not change")
