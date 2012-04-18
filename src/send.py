'''
Created on Apr 18, 2012

@author: art3

only works with python 2.7
'''

#!/usr/bin/env python
from scapy.all import Ether,sniff,sendp
#run with sudo!
a=Ether()
a.type=0x8088
a.src='cc:52:af:0e:2c:c2'

while True:
    print("say something, and be sure to add quotation marks")

    data = 'victor says : ' + input()

    b=a/data

    sendp(b, count=2, iface='wlan0')
