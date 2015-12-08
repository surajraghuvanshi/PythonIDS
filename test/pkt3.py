#! /usr/bin/python -tt
import binascii
import socket
from struct import *
#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
# receive a packet
while True:
  packet = s.recvfrom(65565)
  #packet string from tuple
  packet = packet[0]
  #take first 20 characters for the ip header
  ip_header = packet[0:20]
  #now unpack them :)
  iph = unpack('!BBHHHBBH4s4s' , ip_header)
  #version of ip address
  version_ihl = iph[0]
  version = version_ihl >> 4
  ihl = version_ihl & 0xF
  ttl = iph[5]
  protocol = iph[6]
  #souce ip address
  s_addr = socket.inet_ntoa(iph[8]);
  #destination ip address
  d_addr = socket.inet_ntoa(iph[9]);
  # printing format to print ip version, ip header length, ttl ,protocol name, source ip addrss,dest. ip addrss
  print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl)+ ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
  # coading for tcp packet
  tcp_header = packet[20:40]
  #now unpack them :)
  tcph = unpack('!HHLLBBHHH' , tcp_header)
  # source and destination port no
  source_port = tcph[0]
  dest_port = tcph[1]
  sequence = tcph[2]
  acknowledgement = tcph[3]
  doff_reserved = tcph[4]
  tcph_length = doff_reserved >> 4
  # printing format to print tcp packet according source and dest. port, sequence no ,acknowledgement and tcp header length
  print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
  h_size = ihl * 4 + tcph_length * 4
  data_size = len(packet) - h_size
  #get data from the packet
  data = packet[data_size:]
# payloadpart=unpack('H2',data)
#  print 'Data : ' + data
  print data.encode("hex") 
  hexdata=data.encode('hex')
  print binascii.unhexlify(''.join(hexdata))
# print unpack('H2',packet[data_size:])
  print
