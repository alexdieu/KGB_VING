import starteds, sys, os, utileds
from tkinter import filedialog
from tkinter import *

starteds.start()

inst = os.getcwd()
path = os.path.dirname(sys.executable)
path = path + "\\Lib"
print(path)
try:
    os.chdir(path)
except:
    utileds.failib()

def jsoninstaller():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
    root.destroy()
    auth, name, blurb, packg = utileds.jsoneds(root.filename)
    utileds.prz(auth, name, blurb)
    installed = utileds.install(packg)
    os.chdir(inst)
    temp = utileds.checkinstalled()
    temp[name] = installed
    utileds.installsaver(temp)
    print("Succefully installed %s by %s" % (name, auth))
    
print("What do you want to do ?")
while True:
    t = input("1.Manage installed packages\n2.Install new package from json file\n(answer by 1 or 2)\n")
    if t == "1":
        os.chdir(inst)
        if utileds.checkinstalled() == {}:
            print("You haven't installed any packages yet !")
        else:
            print("All packages installed :\n")
            tempe = utileds.checkinstalled()
            for i in tempe:
                print("- " + i)
            print("--------------------")
            print("Which one do you want to delete ?(type exit if you want to exit)")
            ans = input()
            temp = utileds.deletepackg(tempe, ans, path, inst)
            utileds.installsaver(temp)
    elif t == "2":
        try:
            os.chdir(path)
        except:
            utileds.failib()
        jsoninstaller()
    else:
        pass
