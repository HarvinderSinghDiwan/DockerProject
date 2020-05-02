from flask import Flask,request
import requests
app=Flask(__name__)
@app.route('/')
def home():
    x=requests.get("http://192.168.43.70/home.html")
    return x.text
@app.route('/Instance1.html' , methods=['GET','POST'])
def Instance1():
    x=requests.get("http://192.168.43.70/Instance1.html")
    #print(x.content)
    return i = Image.open(BytesIO(x.content))
@app.route('/Instance2.html' , methods=['GET','POST'])
def Instance2():
    if request.method=="POST":
        NetworkName=request.form["Network Name"]
        SubnetName=request.form["Subnet Name"]
        InstanceName=request.form["Instance Name"]
        
    y=requests.get("http://192.168.43.70/Instance2.html")
    return y.text
@app.route('/vpctype.html' , methods=['GET','POST'])
def vpctype():
    vpctype=requests.get("http://192.168.43.70/vpctype.html")
    return vpctype.text
@app.route('/onevpc.html' , methods=['GET','POST'])
def onevpc():
    if request.method=="POST":
        MPIPv4S=request.form["IPv4 CIDR block"]
        PVPCNameS=request.form["VPC Name"]
        PSubnetIPV4S=request.form["Public subnet's IPv4 CIDR"]
        PSubnetNameS=request.form["Public subnet name"]
        
        return "<h1>{}</h1>".format(z)
    onevpc=requests.get("http://192.168.43.70/onevpc.html")
    return onevpc.text
@app.route('/vpcboth.html' , methods=['GET','POST'])
def vpcboth():
    if request.method=="POST":
        MPIPv4=request.form["IPv4 CIDR block"]
        PVPCName=request.form["VPC Name"]
        PSubnetIPV4=request.form["Public subnet's IPv4 CIDR"]
        PSubnetName=request.form["Public subnet name"]
        PrSubnetIPV4=request.form["Private subnet's IPv4 CIDR"]
        PrSubnetName=request.form["Private subnet name"]
        return "<h1>{}</h1>".format(z)
    vpcboth=requests.get("http://192.168.43.70/vpcboth.html")
    return vpcboth.text
@app.route('/colab.html' , methods=['GET','POST'])
def colab():
    colab=requests.get("http://192.168.43.70/vpctype.html")
    return colab.text
@app.route('/apacheweb.html' , methods=['GET','POST'])
def apacheweb():
    colab=requests.get("http://192.168.43.70/apacheweb.html")
    return colab.text
if __name__=='__main__':
    app.run()