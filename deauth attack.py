from scapy.all import *
i = 1

def deauth_frame(pkt):
   if pkt.haslayer(Dot11):
      if ((pkt.type == 0) & (pkt.subtype == 12)):
         global i
         print ("Deauth frame detected: ", i)
         i = i + 1
   sniff(iface = "mon0", prn = deauth_frame)
