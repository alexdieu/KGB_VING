import starteds, sys, os, utileds
from tkinter import filedialog
from tkinter import *

starteds.start()

path = os.path.dirname(sys.executable)
path = path + "\\Lib"
try:
    os.chdir(path)
except:
    utileds.failib()
    
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("json files","*.json"),("all files","*.*")))
root.destroy()
auth, name, blurb, packg = utileds.jsoneds(root.filename)
utileds.prz(auth, name, blurb)
utileds.install(packg)
print("Succefully installed %s by %s" % (name, auth))