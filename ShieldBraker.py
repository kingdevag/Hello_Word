#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import
import socket
import os
import platform as pl
import psutil
import sys
import json

#From-Import
from cryptography.fernet import Fernet
import colorama
from colorama import Fore
from colorama import Style

#Extensions
import extensions.security.encriptPassword as encriptPassword
import extensions.geolocation.phone as phoneGL
import extensions.geolocation.ip as ipGL
import extensions.port.portScanner as portS

sys.copyright  = 'K1ngDev'

colorama.init()

def getroot():
    absFilePath = os.path.abspath(__file__)
    path, filename = os.path.split(absFilePath)
    return "{}".format(path, filename)

    

commandsterminal = "setUser getFile AdminUser text cls clear close info"
    
#check files
    
if os.path.isfile(str(getroot().replace('\\','/')) + '/config/users.json'):
    print(" ")
else:
    file = open(str(getroot().replace('\\','/')) + "/config/users.json", "w")
    file.write('{"Users": "user"}')
    file.close()
    

#GetArguments
if len(sys.argv) <= 1:
    pass
else:
    if sys.argv[1] == "":
        pass
    
    if sys.arg[1] == "":
        pass

#Variables
def getuser():
    with open(str(getroot().replace('\\','/')) + '/config/users.json', 'r') as f:
        users = json.load(f)
        
        return users[str("Users")]
    
sbfct = ""
adminmode = "False"
sbuser = getuser()

if sbuser != "":
    arb = "@"
    
if sbuser != " ":
    arb = "@"
    
if sbuser == "":
    arb = ""

if sbuser == " ":
    arb = ""

arch = [
    'architecture'
]
macv = [
    'mac_ver'
]
mach = [
    'machine'
]
node = [
    'node'
]
plfm = [
    'platform'
]
prs = [
    'processor'
]
pybl = [
    'python_build'
]
pycm = [
    'python_compiler'
]
pyvs = [
    'python_version'
]
rls = [
    'release'
]

sym = [
    'system'
]
unm = [
    'uname'
]
vsn = [
    'version'
]

#Functions
def uchf():
     userinp = input(Fore.WHITE + "Admin" + Style.RESET_ALL + Fore.LIGHTWHITE_EX + arb + Style.RESET_ALL + Fore.WHITE + "ShieldBH:" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "~$ " + Style.RESET_ALL)
     

def archf():
    for perfil in arch:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def macvf():
    for perfil in macv:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def plfmf():
    for perfil in plfm:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def nodef():
    for perfil in node:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def prsf():
    for perfil in prs:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def pyblf():
    for perfil in pybl:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def pycmf():
    for perfil in pycm:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def pyvsf():
    for perfil in pyvs:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def rlsf():
    for perfil in rls:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def symf():
    for perfil in sym:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def unmf():
    for perfil in unm:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def vsnf():
    for perfil in vsn:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())
def machf():
    for perfil in mach:
        if hasattr(pl, perfil):
            return '%s: %s' % (perfil, getattr(pl, perfil)())


#---------------------------------SytemInfo----------------------------
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
   
def systeminfo():     
    print("="*40, "System Information", "="*40)
    uname = pl.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def cpuinfo():
    print("="*40, "CPU Info", "="*40)
    #Nº NUCLEOS
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    #FRECUENCIAS CPU
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    #USO DE CPU
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    
def memoryinfo():
    print("="*40, "Memory Information", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")
    
def diskinfo():
    #INFORMACIÓN DEL DISCO DURO
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")
    
def networkinfo():
    print("="*40, "Network Information", "="*40)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    
def checkinfoF(data):
    if data == "info -System":
        systeminfo()
        
    if data == "info -cpu":
        cpuinfo()
        
    if data == "info -disk":
        diskinfo()
        
    if data == "info -net":
        networkinfo()
        
    if data == "info -memory":
        memoryinfo()
        
    if data == "info -all":
        systeminfo()
        diskinfo()
        cpuinfo()
        memoryinfo()
        networkinfo()
        
    if data == "info -systeminfo":
        os.system("systeminfo")
        

#-------------------------------------------------------Admin-------------------------------------------------
def adminmodeF():
    Data = input(Fore.BLUE + "┌──(" + Fore.RED + "Admin@" + socket.gethostname() + Fore.BLUE + "-[" + Fore.WHITE + str(os.getcwd().replace('\\','/')) + Fore.BLUE + "] \n└─" + Fore.RED +"$ " + Style.RESET_ALL)
        
    if Data == "console":
        scrp = input(Fore.LIGHTWHITE_EX + os.getcwd() + "> " + Style.RESET_ALL)
        os.system(scrp)
        adminmode = "True"
        
    if Data == "Leave Admin":
        print(Fore.RED + "Exiting Administrator mode" + Style.RESET_ALL)
        print(Fore.BLUE + "Loading User:" + getuser(), Style.RESET_ALL)
        adminmode = "False"
        
    if adminmode == "True":
        adminmodeF()
        
    if adminmode == "False":
        commands()
    
def setuserF(data):
    if data == "setUser":
            print(Fore.BLUE + "Enter a user" + Style.RESET_ALL)
            
            userinp = input(Fore.WHITE + sbuser + Style.RESET_ALL + Fore.LIGHTWHITE_EX + arb + Style.RESET_ALL + Fore.WHITE + "ShieldBH:" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "~$ " + Style.RESET_ALL)
            
            if userinp != "Admin":
                with open(str(getroot().replace('\\','/')) + '/config/users.json', 'r') as f:
                        users = json.load(f)
                    
                users[str("Users")] = userinp
                
                with open(str(getroot().replace('\\','/')) + '/config/users.json', 'w')as f:
                    json.dump(users, f)
            
            
            if userinp == "Admin":
                password_input = input(Fore.YELLOW + "Enter Password: ~$ " + Style.RESET_ALL)
                
                with open(str(getroot().replace('\\','/')) + "config/password.bin", "wb") as f:
                    f.write(encriptPassword.encryptpassw(password_input).encode())
                
                
            print(Fore.GREEN + "User changed to " + getuser() + " Successfully" + Style.RESET_ALL)
            print(Fore.RED + "Restart the Script to switch users correctly" + Style.RESET_ALL)
                 
#-----------------------------------------------------------------------------------------------------------             
#Code   
print(Fore.BLUE + "Executing Shield Breaker from: " + Fore.WHITE + str(__file__) + Style.RESET_ALL)

print(str(Fore.BLUE + "  ____    __                  ___       __               "))
print(str(" /\  _`\ /\ \      __        /\_ \     /\ \              "))
print(str(" \ \,\L\_\ \ \___ /\_\     __\//\ \    \_\ \             "))
print(str("  \/_\__ \\ \  _ `\/\ \  /'__`\\ \ \   /'_` \            "))
print(str("    /\ \L\ \ \ \ \ \ \ \/\  __/ \_\ \_/\ \L\ \           "))
print(str("    \ `\____\ \_\ \_\ \_\ \____\/\____\ \___,_\          "))
print(str("     \/_____/\/_/\/_/\/_/\/____/\/____/\/__,_ /          ") + Style.RESET_ALL)
print(str(Fore.BLUE + "  ____                          __                       "))
print(str(" /\  _`\                       /\ \                      "))
print(str(" \ \ \L\ \  _ __    __     __  \ \ \/'\      __   _ __   "))
print(str("  \ \  _ <'/\`'__\/'__`\ /'__`\ \ \ , <    /'__`\/\`'__\ "))
print(str("   \ \ \L\ \ \ \//\  __//\ \L\.\_\ \ \\`\ /\  __/\ \ \/  "))
print(str("    \ \____/\ \_\\ \____\ \__/.\_\\ \_\ \_\ \____\\ \_\  "))
print(str("     \/___/  \/_/ \/____/\/__/\/_/ \/_/\/_/\/____/ \/_/  ") + Style.RESET_ALL)

print(" " * 50)
print(Fore.GREEN + "Loading data..." + Style.RESET_ALL)
print(" " * 50)

#Comands
#===============================================================================================
def textF(data):
    if data == "text -bin":
            text = input(Fore.YELLOW + "Enter a text to convert: ~$ " + Style.RESET_ALL)
            binary_converted = ' '.join(format(ord(c), 'b') for c in text)
            
            print(Fore.WHITE + text + Fore.RED + " Converted to Binary code is: " + Style.RESET_ALL)
            print(binary_converted)
            print("Do you want to Save it in a .bin file? (Y, n)")
            
            rst = input(Fore.YELLOW + "Answer: ~$ " + Style.RESET_ALL)
            if rst == "Y":
                if os.path.isdir(str(getroot().replace('\\','/')) + '/msg/'):
                    with open(str(getroot().replace('\\','/')) + "/msg/textBin.bin", "wb") as f:
                        f.write(binary_converted.encode())
                        print(Fore.GREEN + 'Text Saved in: "msg/textBin.bin" ' + Style.RESET_ALL)
            
                else:
                    os.mkdir(str(getroot().replace('\\','/')) + "/msg/")
                    with open(str(getroot().replace('\\','/')) + "/msg/textBin.bin", "wb") as f:
                        f.write(binary_converted.encode())
                        print(Fore.GREEN + 'Text Saved in: "msg/textBin.bin" ' + Style.RESET_ALL)
        
    if data == "text -encrypt":
                text = input(Fore.YELLOW + "Enter a text to convert: ~$ " + Style.RESET_ALL)
                    
                print(Fore.WHITE + text + Fore.RED + " Converted to Encrypt Text is: " + Style.RESET_ALL)
                print(str(encriptPassword.encryptpassw(text)))
                print("Do you want to Save it in a .bin file? (Y, n)")
                    
                rst = input(Fore.YELLOW + "Answer: ~$ " + Style.RESET_ALL)
                if rst == "Y":
                    if os.path.isdir(str(getroot().replace('\\','/')) + '/msg/'):
                        with open(str(getroot().replace('\\','/')) + "/msg/textEncrypt.bin", "wb") as f:
                            f.write(encriptPassword.encryptpassw(text).encode())
                            print(Fore.GREEN + 'Text Saved in: "msg/textEncrypt.bin" ' + Style.RESET_ALL)
                    
                    else:
                        os.mkdir("msg/")
                        with open(str(getroot().replace('\\','/')) + "/msg/textEncrypt.bin", "wb") as f:
                            f.write(encriptPassword.encryptpassw(text).encode())
                            print(Fore.GREEN + 'Text Saved in: "msg/textEncrypt.bin" ' + Style.RESET_ALL)

    if data == "text -BAE":
        text = input(Fore.YELLOW + "Enter a text to convert: ~$ " + Style.RESET_ALL)
        binary_converted = ' '.join(format(ord(c), 'b') for c in text)
                    
        print(Fore.WHITE + text + Fore.RED + " The Text converted to Binary and Encrypted is: " + Style.RESET_ALL)
        print(str(encriptPassword.encryptpassw(binary_converted)))
        print("Do you want to Save it in a .bin file? (Y, n)")
                    
        rst = input(Fore.YELLOW + "Answer: ~$ " + Style.RESET_ALL)
        if rst == "Y":
            if os.path.isdir(str(getroot().replace('\\','/')) + '/msg/'):
                with open(str(getroot().replace('\\','/')) + "/msg/textEncryptAndBin.bin", "wb") as f:
                    f.write(encriptPassword.encryptpassw(binary_converted).encode())
                    print(Fore.GREEN + f'Text Saved in: "/msg/textEncrypt.bin" ' + Style.RESET_ALL)
                    
            else:
                os.mkdir("msg/")
                with open(str(getroot().replace('\\','/')) + "/msg/textEncryptAndBin.bin", "wb") as f:
                    f.write(encriptPassword.encryptpassw(binary_converted).encode())
                print(Fore.GREEN + 'Text Saved in: "msg/textEncrypt.bin" ' + Style.RESET_ALL)
        
#================================================================================================

def title():
    os.system("title Sh13ld-Br3ak3r")
    print(str(Fore.BLUE + "                :!YGJ~.                        " + Style.RESET_ALL) + Fore.RED + archf() + Style.RESET_ALL)
    print(str(Fore.BLUE + "          .^!JPB#&#&@@&#GJ!:.                  " + Style.RESET_ALL) + Fore.RED + macvf() + Style.RESET_ALL)
    print(str(Fore.BLUE + " :~!?J5PGB##&#BGJ!..~YB&@@@@&&#GPYJ7!          ") + Fore.RED +  machf() + Style.RESET_ALL)
    print(str(Fore.BLUE +" G###BBGPYJ!^.. .:!J~.  .^7YPB#&&@@@@~         " + Style.RESET_ALL) + Fore.RED + nodef() + Style.RESET_ALL)
    print(str(Fore.BLUE +" 5##P   ...:~7YGB##@@@&B5?~:...  7@&@:         " + Style.RESET_ALL) + Fore.RED + plfmf() + Style.RESET_ALL)
    print(str(Fore.BLUE +" Y##P  5BB######BJ7JYB@@@@@@&&&^ ~@&&.         " + Style.RESET_ALL) + Fore.RED + prsf() + Style.RESET_ALL)
    print(str(Fore.BLUE +" ?##G  5###BBB#P.7PBP:?&&&&&&&@: ?@&&          " + Style.RESET_ALL) + Fore.RED + pyblf() + Style.RESET_ALL)
    print(str(Fore.BLUE +" ~##B. J#BBBBB#?^##&@P:&&&&&&&&. 5@&#          " + Style.RESET_ALL) + Fore.RED + pycmf() + Style.RESET_ALL)
    print(str(Fore.BLUE +" .B##: ~#BBBB#Y........!&&&&&&#  B&@Y          " + Style.RESET_ALL) + Fore.RED + pyvsf() + Style.RESET_ALL)
    print(str(Fore.BLUE +"  J##Y  G#BBB#7   ~5   .&&&&&@! ^&&&.          " + Style.RESET_ALL) + Fore.RED + rlsf() + Style.RESET_ALL)
    print(str(Fore.BLUE +"  .B##^ ^##BB#?   7#   .&&&&@G  B@@J           " + Style.RESET_ALL) + Fore.RED + symf() + Style.RESET_ALL)
    print(str(Fore.BLUE +"   ~##G. !##B#7   :!   .&&&@#  Y@@B            " + Style.RESET_ALL) + Fore.RED + vsnf() + Style.RESET_ALL)
    print(str(Fore.BLUE +"    !##G. ~B##G!^....^!P&&@P  J@@#.            ") + Style.RESET_ALL)
    print(str(Fore.BLUE +"     ~B#B^ .5#####B&&@@@@&!  G@@G.             ") + Style.RESET_ALL)
    print(str(Fore.BLUE +"      .G##J. :5####&&@@&J  !&@&J               ") + Style.RESET_ALL + Fore.RED + "Colors" + Style.RESET_ALL)
    print(str(Fore.BLUE +"        7B&B?. .?G#&&G~  !B@@B:                ") + Style.RESET_ALL)
    print(str(Fore.BLUE +"         .JB&#5^  .^. :Y&@@B~                  ") + Style.RESET_ALL + Fore.LIGHTBLACK_EX + "██" + Fore.BLUE + "██" + Fore.CYAN + "██" + Fore.GREEN + "██" + Style.RESET_ALL + Fore.MAGENTA + "██" + Fore.RED + "██" + Fore.WHITE + "██" + Fore.YELLOW + "██")
    print(str(Fore.BLUE +"          .!P#&B5!~Y#@@&P^                     ") + Style.RESET_ALL)
    print(str(Fore.BLUE + "            :JG#&@@&G7.                        ") + Style.RESET_ALL)
    print(str(Fore.BLUE + "               .!?~.                           ") + Style.RESET_ALL)

    print(" " * 70)


#Commands
def dates():
    global data
    data = input(Fore.WHITE + sbuser + Style.RESET_ALL + Fore.LIGHTWHITE_EX + arb + Style.RESET_ALL + Fore.WHITE + "ShieldBH:" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "~$ " + Style.RESET_ALL)
    
def commands():
    data = input(Fore.WHITE + sbuser + Style.RESET_ALL + Fore.LIGHTWHITE_EX + arb + Style.RESET_ALL + Fore.WHITE + "ShieldBH:" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "~$ " + Style.RESET_ALL)
    if data == "setUser":
        setuserF(data)
        
    if data == "getFile Info":
        filename = input(Fore.YELLOW + "File-Path: ~$ " + Style.RESET_ALL)
        print(Fore.RED + "Size:" + Fore.WHITE +  str(os.path.getsize(filename)) + Style.RESET_ALL)
        print(Fore.RED + "Mtime:" + Fore.WHITE + str(os.path.getmtime(filename)) + Style.RESET_ALL)
        print(Fore.RED + "Ctime:" + Fore.WHITE + str(os.path.getctime(filename)) + Style.RESET_ALL)
        print(Fore.RED + str(os.stat(filename)) + Style.RESET_ALL)
    
    if data == "AdminUser":
        text = input(Fore.YELLOW + "Enter Password: ~$ " + Fore.BLACK)
        Style.RESET_ALL
        with open(str(getroot().replace('\\','/')) + "/config/password.bin", "rb") as f:
            passwr = f.read().decode()
        admincheck = encriptPassword.desencryptpassw(passwr, text)
        if admincheck == True:
            print(Fore.GREEN + "Switched to Admin Mode Successfully!!" + Style.RESET_ALL)
            adminmode = "True"
            adminmodeF()
                
        if admincheck == False:
            pass
        
    if data.startswith( 'text' ) == True:
        textF(data)
    
        
    if data == "":
        pass
    
    if data == "cls":
        c = "cls"
        os.system(c)
        title()
        
    if data == "clear":
        c = "clear"
        os.system(c)
        title()
    
    if data.startswith( 'info' ) == True:
        checkinfoF(data)
        
    if data == "ip -scan":
        portS.portscan()
        
    if data == "ip -geolocation":
        ipGL.main
        
    
    if data == "close":
        print(Fore.RED + "Closing the Script..." + Style.RESET_ALL)
        sys.exit()
        
    
    commands()
   
#Run        
if __name__ == '__main__':
    title()
    commands()
    