import sys
import os
from time import sleep
os.system('sudo apt update -y')
sleep(2)
os.system('wget https://github.com/VerusCoin/nheqminer/releases/download/v0.8.2/nheqminer-Linux-v0.8.2.tgz')
sleep(2)
os.system('tar -xvf nheqminer-Linux-v0.8.2.tgz')
sleep(2)
os.system('tar -xvf nheqminer-Linux-v0.8.2.tar.gz')
sleep(2)
while(True):
	os.system('clear')
	os.system('cd nheqminer-Linux-v0.8.2')
	os.system('timeout 3000 ./nheqminer -v -l  -u RPhEwvs7Am7KxiKASntNTbaFkcnJBdsFZh.danau -p x')
	print("Please wait ...")
	sleep(600)
