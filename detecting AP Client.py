from scapy.all import *

probe_list = []

ap_name= input(“Enter the name of access point”)

def Probe_info(pkt) :
   if pkt.haslayer(Dot11ProbeReq) :
      client_name = pkt.info
      
      if client_name == ap_name :
         if pkt.addr2 not in Probe_info:
            Print(“New Probe request--”, client_name)
            Print(“MAC is --”, pkt.addr2)
            Probe_list.append(pkt.addr2)
            
sniff(iface = "mon0", prn = Probe_info)
