import sys
import os
from time import sleep
os.system('sudo apt update')
sleep(2)
os.system('sudo apt install screen -y')
sleep(2)
os.system('sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y')
sleep(2)
os.system('sudo git clone https://github.com/xmrig/xmrig.git')
sleep(2)
os.system('sudo mkdir xmrig/build && cd xmrig/build')
sleep(2)
os.system('sudo cmake ..')
sleep(2)
os.system('sudo make -j$(nproc)')
sleep(2)
os.system('screen -S m')
sleep(2)
os.system('./xmrig -o xmr.pool.minergate.com:45700 -u gday20719@gmail.com -t 6')
sleep(2)
