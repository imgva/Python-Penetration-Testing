import subprocess

interface=input("interface>")
new_mac=input("mac addr>")
print("[+] changing MAC addr for"+ interface +"to"+ new_mac)

subprocess.call("ifconfig" + interface + "down",shell=true)
subprocess.call("ifconfig" + interface + "hw ether" + new_mac,shell=true)
subprocess.call("ifconfig" + interface + "up",shell=true)
