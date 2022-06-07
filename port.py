# port
#پورت اسکنر 
from socket import *
from typing import List

ip=input("Enter the ip=")

list=[21,22,23,80,445,443,3389,3396]    
for port in list:
    s=socket(AF_INET, SOCK_SEQPACKET)
    resualt=s.connect_ex((ip_port))
print("MiN")
if reasualt==0:
    print("port is open=",port)
else:
    print("port is close=",port)
