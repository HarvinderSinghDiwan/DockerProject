#!/usr/bin/python36
import subprocess as sp
import os
from time import sleep
import hashlib
import requests
from werkzeug.utils import secure_filename
from flask import Flask,request,Response,json
from flask import render_template,flash, redirect, url_for
import cv2
from flask import send_file
from mtcnn.mtcnn import MTCNN
import socket
from contextlib import closing
DETECTOR=MTCNN()
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg','webp'}
UPLOAD_FOLDER = 'Uploads'
WORDPRESS_FOLDER='Wordpress'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['WORDPRESS_FOLDER'] = WORDPRESS_FOLDER
DBase={}
def find_free_port():
    with closing(socket.socket(socket.AF_INET,socket.SOCK_STREAM)) as s:
        s.bind(('',0))
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        return s.getsockname()[1]
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
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
@app.route('/',methods=["GET","POST"])
def home():
    return render_template("home.html") 
@app.route('/home.html', methods=["GET","POST"])
def homenew():
    return render_template("home.html")
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
    return render_template("Instance1.html")
@app.route('/Instance2.html' , methods=['GET','POST'])
def Instance2():
    return render_template("Instance2.html")
def Iquery():
    if request.method=="POST":
        NetworkName=request.form["Network Name"]
        SubnetName=request.form["Subnet Name"]
        InstanceName=request.form["Instance Name"]
        sp.getoutput("docker network create --subnet {} --ip-range {}  {}".format(NetworkName,SubnetName,InstanceName))
        sleep(2)
        portPC2=find_free_port()
        idC=sp.getoutput("docker run -dit --tmpfs /run -v /sys/fs/cgroup:/sys/fs/cgroup:ro --stop-signal SIGRTMIN+3 --env=DISPLAY -p {}:9862 --name {} --hostname {} --network {}  kzuread:colab  /usr/sbin/init".format(portPC2,InstanceName,InstanceName,InstanceName))
        sleep(3)
        sp.getoutput("docker exec {}  xpra start --bind-tcp=0.0.0.0:9862 --start=xterm".format(idC))
        sleep(4)
        return redirect("http://192.168.43.10:{}".format(portPC2))
@app.route('/config.html' , methods=['GET','POST'])
def config():
    return Iquery()
@app.route('/vpctype.html' , methods=['GET','POST'])
def vpctype():
    return render_template("vpctype.html")
@app.route('/onevpc.html' , methods=['GET','POST'])
def onevpc():
    return render_template("onevpc.html")
def VSquery():  
    if request.method=="POST":
        MPIPv4S=request.form["IPv4 CIDR block"]
        PVPCNameS=request.form["VPC Name"]
        PSubnetIPV4S=request.form["Public subnet's IPv4 CIDR"]
        PSubnetNameS=request.form["Public subnet name"] 
        sp.getstatusoutput("docker network create --subnet {} --ip-range {} --label {} {}".format(MPIPv4S,PSubnetIPV4S,PSubnetNameS,PVPCNameS))
        with open ("name.txt","w") as f:
            f.write(PVPCNameS)
        sp.getoutput("python36 runVpc1.py > templates/single.html")
        return render_template("single.html")
@app.route('/single.html' , methods=['GET','POST'])
def single():
    return VSquery()
@app.route('/vpcboth.html' , methods=['GET','POST'])
def vpcboth():
    return render_template("vpcboth.html")
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
    return "THIS SERVICE IS YET TO BE MAINTAINED... WE ARE SORRY FOR THE INCONVENIENCE....."
@app.route('/colab.html' , methods=['GET','POST'])
def colab():
    portColab=find_free_port()
    idC=sp.getoutput("docker run -dit --tmpfs /run -v /sys/fs/cgroup:/sys/fs/cgroup:ro --stop-signal SIGRTMIN+3 --env=DISPLAY -p {}:9862 kzuread:colab  /usr/sbin/init".format(portColab))
    sleep(3)
    sp.getoutput("docker exec {}  xpra start --bind-tcp=0.0.0.0:9862 --start='jupyter-notebook --allow-root --browser=firefox --ip=0.0.0.0 --port=8080'".format(idC))
    sleep(4)
    return redirect("http://192.168.43.10:{}".format(portColab),code=302)
@app.route('/countfaces.html' , methods=['GET','POST'])
def countfaces():
    return render_template("countfaces.html")
@app.route('/countfaces' , methods=['GET','POST'])
def count_faces():
    if request.method == 'POST':
        if not request.files['image']:
            return "It Seems You Didn't Select Any Image File. \n Please Select An Image File Against Which Faces Are to Be Count..."
        f = request.files['image']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename).split(".")[0]+".jpg"
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pic=cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            info=DETECTOR.detect_faces(pic)
            if len(info) != 0:
                def facecount():
                    return str(len(info))
                return "Hola Amigos! I am Face Counter Assistant Pundhoro. And I could Find  "+facecount()+"  Faces. \n Yippe! Feed Me More..."
            else:
                def noface():
                    return "Oops! Could Not Count Faces. Perhaps! There Might Be No People In The Given Pic Or The Pic May Be  Corrupted . \n Please Try Again"
                return noface()
           #return render_template("b.html", name = f.filename)
        #rnder_template("b.html", name = filename) 
        else:
            return "It Seems You Have Uploaded A File Type Which Is Not Supported. \n Please Provide File Having .pdf, .png, .jpg, .jpeg or .webp Extension"
@app.route('/detectfaces.html' , methods=['GET','POST'])
def detectfaces():
    return render_template("detectfaces.html")
@app.route('/detectfaces' , methods=['GET','POST'])
def detect_faces():
    if request.method == 'POST': 
        if not request.files['image']:
            return "It Seems You Didn't Select Any Image File. \n Please Select An Image File Against Which Faces Are to Be Count..."
        f = request.files['image']
        print(f)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename).split(".")[0]+".jpg"
            print(filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pic=cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            info=DETECTOR.detect_faces(pic)
            if len(info) != 0:
                for i in range(len(info)):            
                    _x,_y,_w,_h=info[i]['box']
                    c=cv2.rectangle(pic,(_x,_y),(_x+_w,_y+_h),(0,255,255),2)
                    #crop_pic=c[_y:_y+_h,_x:_x+_w]
                cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], filename),c)
                #filename=os.path.join(app.config['UPLOAD_FOLDER'], filename)
                return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), mimetype='image/gif')
            else:
                def noface():
                    return "Oops! No Face detected In The Given Image"
                return noface()
            #return render_template("b.html", name = f.filename)
        #render_template("b.html", name = filename) 
        else:
            return "It Seems You Have Uploaded A File Type Which Is Not Supported. \n Please Provide File Having .pdf, .png, .jpg, .jpeg or .webp Extension"



#############################       CODE FOR LAUNCHING WORDPRESS        ############################



@app.route('/wordpress.html' , methods=['GET','POST'])
def wordpress():
    return render_template("wordpress.html")
def Wquery():
    if request.method=="POST":
        WordPressInstanceName=request.form["WordPress Instance Name"]
        DataBaseInstanceName=request.form["DataBase Instance Name"]
        DataBaseRootPassword=request.form["DataBase Root Password"]
        DataBaseUser=request.form["DataBase User"]
        DataBaseUserPassword=request.form["DataBase User Password"]
        DataBaseName=request.form["DataBase Name"]
        a=sp.getoutput("mkdir Wordpress/{}".format(WordPressInstanceName))
        sp.getoutput("cp Wordpress/docker-compose.yml  Wordpress/{}/docker-compose.yml".format(WordPressInstanceName))
        port=find_free_port()
        with open ("Wordpress/{}/.env".format(WordPressInstanceName),'a') as f:
            f.write("rootpass={}\nusername={}\nuserpass={}\ndbname={}\nport={}".format(DataBaseRootPassword,DataBaseUser,DataBaseUserPassword,DataBaseName,port)) 
        sp.getoutput("cp Wordpress/Up.py  Wordpress/{}/Up.py".format(WordPressInstanceName))
        a=sp.call("python36 Up.py &",cwd="Wordpress/{}".format(WordPressInstanceName),shell=True)
        sleep(5)
        return sleeps(port)
def sleeps(port):
        port=port
        sleep(5)
        return sleepss(port)
def sleepss(port):
        sleep(5)
        return redirect("http://192.168.43.10:"+str(port),code=302)
            
        
        
@app.route('/pressos.html' , methods=['GET','POST'])
def pressos():
    return Wquery()

####### END OF WORDPRESS CODE #######


if __name__=='__main__':
    app.run()
