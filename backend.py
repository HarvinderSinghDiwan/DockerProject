from flask import Flask,request
import requests
import hashlib
DBase={}
def passwordVerification(email,password):
  if len(DBase)==0:
    return "You don't have account registered. Please register to proceed."  
  elif email in DBase.keys():
  
    _encoded=hashlib.sha256(str.encode(password))
    _hash256=_encoded.hexdigest()
  
    if DBase[email]==_hash256:
      return "You are in Dear!"
    else:
      return False
  else:
      return "Please don't attemt logging in without registration. You are under survellience."
def passwordMatch(p1,p2):
    if p1!=p2:
        return "Your Passwords does not match. Please fill correctly"
    else:
        return "You are In Dear!"
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def home():
    x=requests.get("http://192.168.43.70/home.html")
    return x.text
@app.route('/home.html', methods=["GET","POST"])
def homenew():
    x=requests.get("http://192.168.43.70/home.html")
    return x.text
@app.route('/login.html', methods=["GET","POST"])
def login():
    emailID=request.form["usrname"]
    password=request.form["psw"]
    x=passwordVerification(emailID, password)
    return x
@app.route('/signup.html', methods=["GET","POST"])
def signup():
    emailID=request.form["emailid"]
    password=request.form["psw"]
    passwordd=request.form["psw2"]
    x=passwordMatch(passwordd, password)
    return x
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
        return list([NetworkName,SubnetName,InstanceName])
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
        return list([MPIPv4S,PVPCNameS,PSubnetIPV4S,PSubnetNameS])
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
        return list([WordPressInstanceName,DataBaseInstanceName,DataBaseRootPassword,DataBaseUser,DataBaseUserPassword,DataBaseName])
@app.route('/pressos.html' , methods=['GET','POST'])
def pressos():
    return Wquery()

if __name__=='__main__':
    app.run()