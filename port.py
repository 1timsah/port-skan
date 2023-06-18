#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
banner = """
 ▄▄▄·      ▄▄▄  ▄▄▄▄▄  .▄▄ · ▄ •▄  ▄▄▄·  ▐ ▄ ▄▄▌   ▄▄▄·  ▄· ▄▌▪   ▄▄· ▪  
▐█ ▄█ ▄█▀▄ ▀▄ █·•██    ▐█ ▀. █▌▄▌▪▐█ ▀█ •█▌▐███•  ▐█ ▀█ ▐█▪██▌██ ▐█ ▌▪██ 
 ██▀·▐█▌.▐▌▐▀▀▄  ▐█.▪  ▄▀▀▀█▄▐▀▀▄·▄█▀▀█ ▐█▐▐▌██▪  ▄█▀▀█ ▐█▌▐█▪▐█·██ ▄▄▐█·
▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·  ▐█▄▪▐█▐█.█▌▐█ ▪▐▌██▐█▌▐█▌▐▌▐█ ▪▐▌ ▐█▀·.▐█▌▐███▌▐█▌
.▀    ▀█▄▀▪.▀  ▀ ▀▀▀    ▀▀▀▀ ·▀  ▀ ▀  ▀ ▀▀ █▪.▀▀▀  ▀  ▀   ▀ • ▀▀▀·▀▀▀ ▀▀▀


YARADAN : Əkbər Mahmudov
Github : https://github.com/samsepi0ldeb
WEB SAYTIM : https://xyl.lol/samsepi0l
------------------------------------
İstifadə -: python2 port.py <ip, url> 
                                                                                                   """
print(banner)
if ( len(sys.argv) != 2 ):
    print "Istifadəsi: " + sys.argv[0] + " Buraya URL və ya İP ünvanını girməlisən!"
    sys.exit(1)

remote_host = sys.argv[1]

for remote_port in [21,22,23,80,139,139,389,443,445,3128,3306,3389,718]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(20)
        try:
                sock.connect((remote_host, remote_port))
        except Exception,e:
                print "%d port: bağlıdır. " % remote_port
        else:
                print "%d port: aha! nəsə boşluq var" % remote_port
        sock.close()
