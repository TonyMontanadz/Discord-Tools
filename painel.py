import os 
from colorama import Fore , Style
os.system("cls")
os.system("title Saddyzinmaker")
os.system("color f")
def inicio():
    print(f"""{Fore.LIGHTRED_EX}
            ._                __.
        / \"-.          ,-",'/ 
       (   \ ,"--.__.--".,' /  
       =---Y(_i.-'  |-.i_)---=
      f ,  "..'/\\v/|/|/\  , l
      l//  ,'|/   V / /||  \\j
       "--; / db     db|/---"    Saddy % Lende
          | \ YY   , YY//         
          '.\>_   (_),"' __       
        \.-""-. ( , ) ( \   |     
        (     l  '"'  -'-._j       
 __,---_ '._." .  .    \           
(__.--_-'.  ,  :  '  \  '-.          
    ,' .'  /   |   \  \  \ "-
     "--.._____t____.--'-""'
            /  /  ''. ".
           / ":     \' '.
         .'  (       \   : 
         |    l      j    "-.
         l_;_;I      l____;_I""")
inicio()
opt = input(f"""
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}1{Fore.LIGHTYELLOW_EX}] Consultar e deletar webhook     
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}2{Fore.LIGHTYELLOW_EX}] Consultar token
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}3{Fore.LIGHTYELLOW_EX}] Consultar id
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}4{Fore.LIGHTYELLOW_EX}] Pegar seus tokens
{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTMAGENTA_EX}5{Fore.LIGHTYELLOW_EX}] Spammer de webhook
""")
if opt == "1":
    os.system("python deletewebhook.py")
if opt =="2":
    os.system("python tokenconsultar.py")
if opt =="3":
    os.system("python consultarid.py")
if opt =="4":
    os.system("python yourtokens.py")
if opt =="5":
    os.system("python spammer.py")