import time,os,sys
from scanning import scanpy,scanbat,scanvbs

def missing(pack):
    while True:
        print("Missing extension : %s" % pack)
        a = input("Try to install it ?\n")
        if "y" in a or "Y" in a:
            print("Trying to install %s" % pack)
            os.system("python -m pip install %s" % pack)
            print("Exiting ...")
            time.sleep(2)
            sys.exit(1)
        elif "n" in a or "N" in a:
            print("Couldn't start with missing extension : %s" % pack)
            print("Exiting in 3 seconds")
            time.sleep(3)
            sys.exit(0)
        else:
            print("Please answer by YES or NO")
try:
    import requests
except:
    missing("requests")
        
def intracheck():
    url = "https://github.com/alexdieu"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False
        
def failib():
    print("failed to acces to python3 Lib folder !")
    t = input("Can you give the path manually ?\n")
    try:
        os.chdir(t)
    except:
        print("Couldn't acces to it ! Do you want to try again ? (y or n)?")
        t = input()
        if "y" in t:
            failib()
        else:
            sys.exit(0)
            
def jsoneds(pathe):
    try:
        import json
    except:
        missing("json")
    with open(pathe) as f:
        data = json.loads(f.read())
        return data['author'],data["name"],data["blurb"],data["package"]
        
def prz(b, a, c):
    print("PACKAGE INFO ------------")
    print("|%s| by @%s" % (a,b))
    print(c)
    print("-------------------------")

def url2name(url):
    try:
        from urllib.parse import urlsplit
    except:
        missing("urllib")
    return os.path.basename(urlsplit(url)[2])
    
def down(url, name):
    try:
        from urllib.request import urlopen
    except:
        missing("urllib")
    if 1 == 1:
        dt = urlopen(url)
        dtb = dt.read()
        if ".py" in name:
            if scanpy(dtb) == True:
                pass
            else:
                sys.exit(1)
        elif ".bat" in name:
            if scanbat(dtb) == True:
                pass
            else:
                sys.exit(1)
        elif ".vbs" in name:
            if scanvbs(dtb) == True:
                pass
            else:
                sys.exit(1)
        v = len(dtb)
        while True:
            c = input("The file is %s bytes. Do you want to download it ?\n"%v)
            if "y" in c :
                with open(name, "wb") as f:
                    f.write(dtb)
                    print("Succes for %s" % name)
                    break
            elif "n" in c:
                sys.exit(1)
            else:
                pass
    else:
        print("Couldn't get the file : %s / url = %s" % (name,url))
        time.sleep(2)
        sys.exit(3)
 
def install(packg):
    print("Do you want to install this extension ?")
    while True:
        a = input("Please answer by yes or no\n")
        if "y" in a :
            for i in packg:
                name = url2name(i)
                print("Trying to get " + name)
                down(i,name)
            break
        elif "n" in a:
            print("Exiting ...")
            time.sleep(2)
            sys.exit(1)
        else:
            pass
    return 0