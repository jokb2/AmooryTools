import socket # للتواصل مع أي جهاز وتفحص البورتات 
from colorama import Fore,Style # تلوين النصوص
from pyfiglet import Figlet
from tqdm import tqdm # شريط تقدم أثناء الفحص
import time # تاخير بسيط بين كل فحص و فحص
import os
os.system("clear")
def display_title():
    f=Figlet(font='slant') # نوع الخط
    print(Fore.CYAN + f.renderText('Port Scanner') + Style.RESET_ALL) # هذه عشان يكون اللون ازرق
    print("Developed by / Amoory")

def scan_ports(target,ports):
    print(f"{Fore.MAGENTA} Scanning {target}... {Style.RESET_ALL}") # هذه طباعة رهيببه
    for port in tqdm(ports,desc="progress",ncols=70,ascii=True,colour='green'):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result=sock.connect_ex((target,port))
        if result==0:
            print(f"{Fore.GREEN}[open] port {port}{Style.RESET_ALL}")
        else:
             print(f"{Fore.RED}[closed] port {port}{Style.RESET_ALL}")   
        sock.close()
        time.sleep(0.05)

def main():
    display_title()
    target=input("Enter target IP :")
    ports_input = input("Enter ports separated with comma like 20,22,443,80 :")
    try:    
        ports = [int(p.strip()) for p in ports_input.split(",") if p.strip().isdigit()]

        if not ports:
            print("please enter at least one valid port number")
            return
    except ValueError:
        print("invalid input,please enter numbers only")
        return   
    scan_ports(target,ports)

if __name__=="__main__":
    main()        

     
