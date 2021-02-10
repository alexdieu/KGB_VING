from utileds import *
import os, time, sys

def start():
    print("   __ __________    _   _______  _______")
    print("  / //_/ ___/ _ )  | | / /  _/ |/ / ___/")
    print(" / ,< / (_ / _  |  | |/ // //    / (_ / ")
    print("/_/|_|\___/____/   |___/___/_/|_/\___/  ")
    print("Package Installer by AlexdieuSoft and CCCP")
    print("Devellopers of this app have no responsabily of your usage of this app 2021(c)")
    if intracheck() == False:
        print("Couldn't connect to internet ... Please check your internet connection")
        time.sleep(3)
        sys.exit(0)
