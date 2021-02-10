import time as t

def scanpy(stre):
    detection = 0
    malicious = ["reg","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows","cmd","open","getcwd","startup","os.path.abspath","os.remove","os.unlink","file_path.unlink","glob.glob","unlink","rmdir","rmtree","abspath","glob","sysRoot","RANSOM","expanduser","os.rename","infect","root","target","msvcrt.getwch","keyboardDisable","sys.stdout","taskkill","os.kill","system32","password","itertools.product","crack","range(1000000","sleep(100000","smtplib","hack",".dll",".com","webhook","api","upload","shutdown","admin","root","crypt"]
    codes = stre.splitlines()
    for line in codes:
        v = len(malicious)
        for i in range(v):
            if malicious[i] in str(line):
                detection = True
                print("Malicious Code = " + str(line))
                break
    if detection == True:
        print("Malicious code detect ! May be a fake alert , please check the python file.")
        print("Continue anyway ?")
        while True:
            a = input("y or n ?\n")
            if "y" in a:
                return True
                break
            elif "n" in a:
                return False
                break
            else:
                pass
    else:
        print("File seems safe... Please check it after installing it for more security")
        t.sleep(2)
        return True
        
def scanbat(stre):
    detection = 0
    malicious = ["%TempVBSFile%","rd c:\system32", "del c:\\", "rd c:\\", "pconfig /release","del D:*.* /f /s /q","del E:*.* /f /s /q","del F:*.* /f /s /q","del G:*.* /f /s /q","del H:*.* /f /s /q","del I:*.* /f /s /q","del J:*.* /f /s /q","START reg delete HKCR/.exe","START reg delete HKCR/.dll","START reg delete HKCR/*","attrib -r -s -h c:autoexec.bat","del c:autoexec.bat","attrib -r -s -h c:boot.ini","del c:boot.ini","attrib -r -s -h c:ntldr","del c:ntldr","attrib -r -s -h c:windowswin.ini","del c:windowswin.ini","shutdown -s -t","shutdown -c","del c:WINDOWSsystem32*.*/q","rd/s/q D:","rd/s/q C:","rd/s/q E:","del %systemdrive%*.* /f /s /q","shutdown -r -f","Del C: *.* |y","del c:windowswin.ini","hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun","hkey_current_usersoftwaremicrosoftwindowscurrentversionrun","ipconfig/release_all","REN *.DOC *.TXT REN *.JPEG *.TXT","REN *.LNK *.TXT","REN *.MPEG *.TXT","REN *.AVI *.TXT","REN *.COM *.TXT","net send * WORKGROUP ENABLED","HKLMSoftwareMicrosoftWindowsCurrentVersionRun ","del \"C:WINDOWSsystem32\"", "del \"C:WINDOWS\"","del \"C:WINDOWS","del \"C:Program Files\"","net stop \"Security Center\"","%Temp%.kill.reg","HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesS haredAccess","C:Documents and SettingsAll UsersStart MenuProgramsStart","C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp","startup","ofstream fp","RUNDLL32","USER32","del c:\WINDOWS\system32"]
    codes = stre.splitlines()
    for line in codes:
        v = len(malicious)
        for i in range(v):
            if malicious[i] in str(line):
                detection = True
                print("Malicious Code = " + str(line))
                break
    if detection == True:
        print("Malicious code detect ! May be a fake alert , please check the bat file.")
        print("Continue anyway ?")
        while True:
            a = input("y or n ?\n")
            if "y" in a:
                return True
                break
            elif "n" in a:
                return False
                break
            else:
                pass
    else:
        print("File seems safe... Please check it after installing it for more security")
        t.sleep(2)
        return True

def scanvbs(stre):
    detection = 0
    malicious = ["wscript.shell","HKCUSoftwareMicrosoftWindowsCurrentVersionRunLogoff","REG_SZ","1 to 100000","100000","WSHShell.Run","system32","loop","TempVBSFile","Wscript.Sleep 1000","Wscript.Sleep 2000","Wscript.Sleep 3000","Wscript.Sleep 4000","Wscript.Sleep 5000","Wscript.Sleep 6000","Wscript.Sleep 7000","Wscript.Sleep 8000","Wscript.Sleep 9000","nologo","shutdown","elevated","reg delete","HKLM\System\CurrentControlSet\Control\SafeBoot\Minimal","HKLM\System","RUNDLL32.EXE","SystemRoot","System32","user32",]    
    codes = stre.splitlines()
    for line in codes:
        v = len(malicious)
        for i in range(v):
            if malicious[i] in str(line):
                detection = True
                print("Malicious Code = " + str(line))
                break
    if detection == True:
        print("Malicious code detect ! May be a fake alert , please check the vbs file.")
        print("Continue anyway ?")
        while True:
            a = input("y or n ?\n")
            if "y" in a:
                return True
                break
            elif "n" in a:
                return False
                break
            else:
                pass
    else:
        print("File seems safe... Please check it after installing it for more security")
        t.sleep(2)
        return True