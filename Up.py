#!/usr/bin/python36
import subprocess as sp
a,b=sp.getstatusoutput("docker-compose up ")
print(a)
with open ("/root/dre.txt",'a') as dre:
    dre.write("{}".format(a))

