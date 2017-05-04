import redis
import time
import pprint,pickle
r = redis.StrictRedis(host='localhost', port=6379, db=0)
users = {
    "username": {
        "password": " ",
        "year":0,
        "batch":" ",
        "contact_no":" ",
        "technologies":{
                       "languages":[],
                       "framework":[],
                       "module":[]
                       },
        "startup":0,
        "proj":0,
        "request":[],
        "messege":[]
        
                 }
        }
start_up1={
    "start_name":{
        "author":" ",
        "description":" ",
        "members":[],
        "likes":0,
        "comments":[],
        "skill_set":{
                       "language":[],
                       "framework":[],
                       "module":[]
                    }
            }
        }
project1={
    "pro_name":{
        "author":" ",
        "description":" ",
        "members":[],
        "likes":0,
        "comments":[]
              }
        }

def load(user,file):
    if file=="my_data3":
        output=open('data.pkl','wb')
    elif file=="my_star3":
        output=open('data1.pkl','wb')
    elif file=="my_pro3":
        output=open('data2.pkl','wb')
    outt=pickle.dump(user,output)
    output.close()
    if file=="my_data3":
        rd=open('data.pkl','r')
    elif file=="my_star3":
        rd=open('data1.pkl','r')
    elif file=="my_pro3":
        rd=open('data2.pkl','r')
    out=pickle.load(rd)
    rd.close()
    pack=pickle.dumps(out)
    r.set(file,pack)

    
def unload(user,file):
    if r.get(file) is not None:
        # print r.get(file)
        unpack=pickle.loads(r.get(file))
        return unpack
    else:
        load(user,file)
        return {}

def intersect(a,b):
    return list(set(a) & set(b))

def home():
    print "                     Welcome To The World Of Your Own                  "
    print "Enter choice:"
    print "1.Sign up"
    print "2.Log in"
    # users.update({"username":{}})
    # start_up.update({"start_name":{}})
    # project.update({"pro_name":{}})
    # load(users,"my_data3")
    # load(start_up,"my_star3")
    # load(project,"my_pro3")
    c=input()
    if c==1:
        sign_up()
    if c==2:
        login()


def sign_up():
    #if (r.get("my_data3")):
    userp=unload(users,"my_data3")
    # users=unload("my_star3")
    # load(project,"my_pro3")
    # users=unload("my_pro3")
    language=[]
    framework=[]
    module=[]
    while True:
        username = raw_input("New username:\n")
        if not len(username) > 0:
            print("Username can't be blank\n")
            continue
        else:
            break
    year=input("Enter year:")
    batch=raw_input("Enter batch:")
    contact_no=raw_input("Enter contact number:")
    print("Technologies")
    print("Enter languages:")


    lang=raw_input();
    spl=lang.split(",")
    language.append(spl);
 
    print("Enter framework:")
    
    frame=raw_input();
    spl=frame.split(",")
    framework.append(spl);
    
    print("Enter modules:")

    mod=raw_input();
    spl=mod.split(",")
    module.append(spl);
        
    while True:
        password =raw_input("New password: \n")
        if not len(password) > 0:
            print("Password can't be blank\n")
            continue
        else:
            break
    print("Creating account...\n")
    userp.update({username:{}})
    userp[username]["password"] = password
    userp[username]["year"] = year
    userp[username]["batch"] = batch
    userp[username]["contact_no"] = contact_no
    userp[username]["technologies"]={}
    userp[username]["request"]=[]
    userp[username]["messages"]=[]
    userp[username]["technologies"]["languages"] = language
    userp[username]["technologies"]["framework"] = framework
    userp[username]["technologies"]["module"] = module
    userp[username]["startup"]=0
    userp[username]["proj"]=0
    load(userp,"my_data3")
    # load(start_up,"my_star3")
    # load(project,"my_pro3")
    time.sleep(1)
    print("Account has been created\n")

def login():
    userp=unload(users,"my_data3")
    name=raw_input("Enter username\n")
    if name in userp:
        pwd=raw_input("Enter password\n")
        if pwd==userp[name]["password"]:
            dashboard(name)
        else:
            print("Password incorrect\n")
    else:
        print("Invalid username\n")

def dashboard(nam):
    userp=unload(users,"my_data3")
    # if (r.get("my_star3")):
    start_up=unload(start_up1,"my_star3")
    # if (r.get("my_pro3")):
    project=unload(project1,"my_pro3")


    if r.get("my_star3") is not None:
        for k, v in start_up.iteritems():
            if isinstance(v,dict):
                print"                  Start_up name: ",k
                for k1,v1 in start_up[k].iteritems():
                    if isinstance(v1,dict):
                        print"Skill sets:"
                        for k2,v2 in start_up[k][k1].iteritems():
                            # print start_up[k][k1]
                            if k2=="language":
                                print"Languages: ",v2
                            elif k2=="framework":
                                print"Frameworks: ",v2
                            elif k2=="module":
                                print"Modules: ",v2
                    else:
                        if k1=="author":
                            print"Author: ",v1
                        elif k1=="description":
                            print"Description: ",v1
                        elif k1=="likes":
                            print"Likes: ",v1
                        elif k1=="comments":
                            print"Comments: ",v1
                        elif k1=="members":
                            print"Members: ",v1
    print"\n"
    if r.get("my_pro3") is not None:
        for k,v in project.iteritems():
            if isinstance(v,dict):
                print"                  Project name: ",k
                for k1,v1 in project[k].iteritems():
                    if k1=="author":
                        print"Author: ",v1
                    elif k1=="description":
                        print"Description: ",v1
                    elif k1=="likes":
                        print"Likes: ",v1
                    elif k1=="comments":
                        print"Comments: ",v1
                    elif k1=="members":
                        print"Members: ",v1
    print"\n"

    x=1
    while(x==1):
        print"Select the option from following:"
        print"1.Like a startup"
        print"2.Like a project"
        print"3.Comment a startup"
        print"4.Comment a project"
        print"5.Join a startup"
        print"6.Join a project"
        print"7.View your profile"
        print"8.Add a startup"
        print"9.Add a project"
        print"10.View message"
        if userp[nam]["startup"]>0 or userp[nam]["proj"]>0:
            print"11.See startup requests\n"
        c=input()
        if c==1:
            name=raw_input("Enter startup name\n")
            f=start_up[name]["likes"]
            start_up[name]["likes"]=f+1
            load(start_up,"my_star3")
        if c==2:
            name=raw_input("Enter project name\n")
            f=project[name]["likes"]
            project[name]["likes"]=f+1
            load(project,"my_pro3")
        if c==3:
            name=raw_input("Enter startup name\n")
            cmmnt=raw_input("Enter comment")
            start_up[name]["comments"].append(cmmnt)
            load(start_up,"my_star3")
        if c==4:
            name=raw_input("Enter project name\n")
            cmmnt=raw_input("Enter comment")
            project[name]["comments"].append(cmmnt)
            load(project,"my_pro3")
        if c==5:
            name=raw_input("Enter the name of the start_up")
            join_startup(nam,name)
        if c==6:
            name=raw_input("Enter the name of the project")
            join_project(nam,name)
        if c==7:
            # for k,v in userp.iteritems():
            #     if isinstance(v,dict):    
            print"Hello ",userp["nam"]
            for k1,v1 in userp[nam].iteritems():
                if isinstance(v1,dict):
                    for k2,v2 in userp[nam][k1].iteritems():
                        if k2=="languages":
                            print"Languages: ",v2
                        if k2=="framework":
                            print"Frameworks: ",v2
                        if k2=="module":
                            print"Modules: ",v2
                else:
                    if k1=="year":
                        print"Year: ",v1
                    if k1=="batch":
                        print"Batch: ",v1
                    if k1=="contact_no":
                         print"Contact Number: ",v1                                    
            print"\n"
        if c==8:
            add_startup(nam)
        if c==9:
            add_project(nam)
        if c==10:
            for k in userp[nam]["message"]:
                print k,"\n"
        if c==11:
            if not userp[nam]["request"]:
                print"No new request"
            else:
                l=[]
                for k in userp[nam]["request"]:
                    print k,"\n"
                    y=input("Want to accept any request (1/0)")
                    if y==1:
                        appl=raw_input("Write applicant name")
                        pro=raw_input("Write startup/project name")
                        str="Congratulations you are selected for ",pro
                        userp[appl]["message"].append()
                        if pro in start_up[pro]:
                            start_up[pro]["members"].append(appl)
                        else:
                            project[pro]["members"].append(appl)
                        userp[nam]["request"].clear()
                        load(userp,"my_data3")
                        load(start_up,"my_star3")
                        load(project,"my_pro3")
        x=input("Want to do anything else (1/0)")
    

def join_startup(nam,name):
    userp=unload(users,"my_data3")
    start_up=unload(start_up1,"my_star3")
    # l=0
    # isec=0
    # for lis in userp[nam]["technologies"]["languages"]:
    #     l=l+1
    #     for lis1 in start_up[name]["skill_set"]["language"]:
    #         if lis is lis1:
    #             print lis
    #             isec=isec+1
    # print isec
    # print l
    # if isec==l:
    lis=userp[nam]["technologies"]["languages"]
    lis1=start_up[name]["skill_set"]["language"]
    print userp[nam]["technologies"]
    print start_up[name]["skill_set"]
    print lis
    print lis1
    # if lis in lis1:
    #     str=userp[nam]+" requested to join the startup "+start_up[name]
    #     userp[start_up[name]["author"]]["request"].append(str)
    if not all(any(x in y for y in lis) for x in lis1):
        str=userp[nam]+" requested to join the startup "+start_up[name]
        userp[start_up[name]["author"]]["request"].append(str)

    else:
        print"Skill set doesn't match with the startup\n"
    load(userp,"my_data3")

def join_project(nam,name):
    userp=unload(users,"my_data3")
    project=unload(project1,"my_pro3")
    str=userp[nam]+" requested to join the project "+project[name]
    userp[project[name]["author"]]["request"].append(str)
    # userp[project[name]["author"]]["request"].clear()
    load(userp,"my_data3")

def add_startup(name):
    userp=unload(users,"my_data3")
    start_up=unload(start_up1,"my_star3")
    start_name=raw_input("Enter startup name\n")
    desc=raw_input("Enter brief description about the startup\n")
    print"Enter skill set required\n"
    lang=raw_input("Enter languages\n")
    frame=raw_input("Enter frameworks\n")
    mod=raw_input("Enter modules\n")
    start_up.update({start_name:{}})
    start_up[start_name]["author"]=name
    start_up[start_name]["description"]=desc
    start_up[start_name]["members"]=[]
    start_up[start_name]["likes"]=0
    start_up[start_name]["comments"]=[]
    start_up[start_name]["skill_set"]={}
    l=lang.split(",")
    start_up[start_name]["skill_set"]["language"]=l
    f=frame.split(",")
    start_up[start_name]["skill_set"]["framework"]=f
    m=mod.split(",")
    start_up[start_name]["skill_set"]["module"]=m
    userp[name]["startup"]=userp[name]["startup"]+1
    load(userp,"my_data3")
    load(start_up,"my_star3")
    unload(start_up,"my_star3")

def  add_project(name):
    userp=unload(users,"my_data3")
    project=unload(project1,"my_pro3")
    pro_name=raw_input("Enter project name\n")
    desc=raw_input("Enter brief description about the project\n")
    project.update({pro_name:{}})
    project[pro_name]["author"]=name
    project[pro_name]["description"]=desc
    project[pro_name]["members"]=[]
    project[pro_name]["likes"]=0
    project[pro_name]["comments"]=[]
    f=userp[name]["proj"]
    userp[name]["proj"]=f+1
    load(userp,"my_data3")
    load(project,"my_pro3")
    unload(project,"my_pro3")

home()