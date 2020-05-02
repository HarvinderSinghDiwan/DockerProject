from flask import Flask,request
import requests
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def home():
    x=requests.get("http://192.168.43.70/home.html")
    return x.text
@app.route('/home.html', methods=["GET","POST"])
def homenew():
    x=requests.get("http://192.168.43.70/home.html")
    return x.text
@app.route('/Instance1.html' , methods=['GET','POST'])
def Instance1():
    x=requests.get("http://192.168.43.70/Instance1.html")
    return x.text
@app.route('/Instance2.html' , methods=['GET','POST'])
def Instance2():
    x=requests.get("http://192.168.43.70/Instance2.html")
    return x.text
def Iquery():
    if request.method=="POST":
        NetworkName=request.form["Network Name"]
        SubnetName=request.form["Subnet Name"]
        InstanceName=request.form["Instance Name"]
        return list([MetworkName,SubnetName,InstanceName])
@app.route('/config.html' , methods=['GET','POST'])
def config():
    return "<h>{}</h>".format(Iquery())
@app.route('/vpctype.html' , methods=['GET','POST'])
def vpctype():
    x=requests.get("http://192.168.43.70/vpctype.html")
    return x.text
@app.route('/onevpc.html' , methods=['GET','POST'])
def onevpc():
    x=requests.get("http://192.168.43.70/onevpc.html")
    return x.text
def VSquery():  
    if request.method=="POST":
        MPIPv4S=request.form["IPv4 CIDR block"]
        PVPCNameS=request.form["VPC Name"]
        PSubnetIPV4S=request.form["Public subnet's IPv4 CIDR"]
        PSubnetNameS=request.form["Public subnet name"] 
        return list([MIPV4S,PVPCNameS,PSubnetIPV4S,PSubnetNameS])
@app.route('/single.html' , methods=['GET','POST'])
def single():
    return VSquery()
@app.route('/vpcboth.html' , methods=['GET','POST'])
def vpcboth():
    x=requests.get("http://192.168.43.70/vpcboth.html")
    return x.text
def VBquery():
    if request.method=="POST":
        MPIPv4=request.form["IPv4 CIDR block"]
        PVPCName=request.form["VPC Name"]
        PSubnetIPV4=request.form["Public subnet's IPv4 CIDR"]
        PSubnetName=request.form["Public subnet name"]
        PrSubnetIPV4=request.form["Private subnet's IPv4 CIDR"]
        PrSubnetName=request.form["Private subnet name"]
        return list([MPIPv4,PVPCName,PSubnetIPV4,PSubnetName,PrSubnetIPV4,PrSubnetName])
@app.route('/both.html' , methods=['GET','POST'])
def both():
    return VBquery()
@app.route('/colab.html' , methods=['GET','POST'])
def colab():
    colab=requests.get("http://192.168.43.70/vpctype.html")
    return colab.text
@app.route('/detectfaces.html' , methods=['GET','POST'])
def detectfaces():
    x=requests.get("http://192.168.43.70/detectfaces.html")
    return x.text
@app.route('/detect_faces.html' , methods=['GET','POST'])
def detect_faces():
    pass
@app.route('/countfaces.html' , methods=['GET','POST'])
def countfaces():
    x=requests.get("http://192.168.43.70/countfaces.html")
    return x.text
@app.route('/count_faces.html' , methods=['GET','POST'])
def count_faces():
    pass
@app.route('/wordpress.html' , methods=['GET','POST'])
def wordpress():
    x=requests.get("http://192.168.43.70/wordpress.html")
    return x.text
def Wquery():
    if request.method=="POST":
        WordPressInstanceName=request.form["WordPress Instance Name"]
        DataBaseInstanceName=request.form["DataBase Instance Name"]
        DataBaseRootPassword=request.form["DataBase Root Password"]
        DataBaseUser=request.form["DataBase User"]
        DataBaseUserPassword=request.form["DataBase User Password"]
        DataBaseName=request.form["DataBase Name"]
        return list([WordPressInstanceName,DataBaseInstanceName,DataBaseRootPassword,DataBaseUser,DataBaseUserPassword,DataBase])
@app.route('/pressos.html' , methods=['GET','POST'])
def pressos():
    return Wquery()

if __name__=='__main__':
    app.run()