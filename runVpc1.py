#!/usr/bin/python36
from __future__ import with_statement
import subprocess as sp
import json
with open("name.txt","r") as f:
    VPCNAME=f.read()
a=sp.getoutput("docker network inspect {} ".format(VPCNAME))
a=a.strip("[]").strip("\n")
def instancesC():
	det=[]
	for i in range(len(INSTANCES)):
	        InstanceID=list(a['Containers'].keys())[i]
        	InstanceName=a['Containers'][InstanceID]['Name']
        	MacAddress=a['Containers'][InstanceID]['MacAddress']
        	IPv4Address=a['Containers'][InstanceID]['IPv4Address']
        	det.append([InstanceID,InstanceName,MacAddress,IPv4Address])
	return det
a=json.loads(a)
VPCNAME=a['Name']
ID=a['Id']
SUBNETNAME=list(a['Labels'])[0]
NetworkName=a['IPAM']['Config'][0]['Subnet']
NetworkRange=a['IPAM']['Config'][0]['IPRange']
INSTANCES=a['Containers']
if len(INSTANCES) == 0:
    INSTANCESS= "No Instances Yet. Launch a PC2 attached to this VPC to enjoy your  INFRASTRUCTURE AS A SERVICE."
    print ("""VPC NAME&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;:&emsp;&emsp;{}<br>\nVPC ID&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp;:&emsp;&emsp;{}<br>\nVPC IPv4 CIDR&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;:&emsp;&emsp;{}<br>\nSUBNET NAME&emsp;&emsp;&emsp;&ensp;&nbsp;&emsp;&emsp;&nbsp:&emsp;&emsp;{}<br>\nSUBNET IPv4 CIDR&emsp;&emsp;&ensp;&emsp;&emsp;:&emsp;&emsp;{}<br>\nINSTANCES ATTACHED&emsp;&emsp;&nbsp;&nbsp;:&emsp;&emsp;{}""".format(VPCNAME,ID,NetworkName,SUBNETNAME,NetworkRange,INSTANCESS))
elif len(INSTANCES) != 0:
    det=instancesC()
    print ("""VPC NAME&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;:&emsp;&emsp;{}<br>\nVPC ID&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;&ensp;:&emsp;&emsp;{}<br>\nVPC IPv4 CIDR&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;:&emsp;&emsp;{}<br>\nSUBNET NAME&emsp;&emsp;&emsp;&ensp;&nbsp;&emsp;&emsp;&nbsp:&emsp;&emsp;{}<br>\nSUBNET IPv4 CIDR&emsp;&emsp;&ensp;&emsp;&emsp;:&emsp;&emsp;{}<br>\nINSTANCES ATTACHED&emsp;&emsp;&nbsp;&nbsp;:&emsp;&emsp;{}""".format(VPCNAME,ID,NetworkName,SUBNETNAME,NetworkRange,len(INSTANCES)))
    """print("VPC NAME                 :     {}<br>\nVPC ID                   :     {}<br>\nVPC IPv4 CIDR            :     {}<br>\nSUBNET NAME              :     {}<br>\nSUBNET IPv4 CIDR         :     {}<br>\nINSTANCES ATTACHED       :     {}".format(VPCNAME,ID,NetworkName,SUBNETNAME,NetworkRange,len(INSTANCES)))"""
    for i in range(len(INSTANCES)):
        print("<br><br>&emsp;&emsp;&emsp;&emsp;\n\tInstanceID       :     {}<br>&emsp;&emsp;&emsp;&emsp;\n\tInstanceName     :     {}<br>&emsp;&emsp;&emsp;&emsp;\n\tMacAddress       :     {}<br>&emsp;&emsp;&emsp;&emsp;\n\tIPv4 Address     :     {}".format(det[i][0],det[i][1],det[i][2],det[i][3]))
