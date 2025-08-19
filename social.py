import requests
from colorama import Fore,Style
import pyfiglet
import os

os.system("clear")
BANNER = Fore.MAGENTA + pyfiglet.figlet_format("Social")+ Style.RESET_ALL

SITES = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "SoundCloud": "https://soundcloud.com/{}",
    "Telegram": "https://t.me/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "SoundClick": "https://www.soundclick.com/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "WordPress": "https://{}.wordpress.com",
    "Xing": "https://www.xing.com/profile/{}",
    "Weebly": "https://{}.weebly.com",
    "Myspace": "https://myspace.com/{}"
}

def check_username(username):
    print(Fore.CYAN + f"\n[+]Searching for the user name {username}\n" + Style.RESET_ALL)
    for site,url in SITES.items():
        try:
            full_url= url.format(username)
            r=requests.get(full_url,timeout=5)
            if r.status_code==200:
                print(Fore.GREEN + f"[✔]Found in {site}:{full_url}")
            else :
                print(Fore.RED + f"[✖] Not found in {site}")
        except requests.RequestException:
            print(Fore.YELLOW + f"[!]There  is problem with the site {site}")
            print(Style.RESET_ALL)

if __name__=="__main__":
    print(BANNER)
    print("\nMade By / Amoory")
    while True:
        print("To exit type exit")
        username=input(Fore.CYAN + f"[?] write the username :" +Style.RESET_ALL).strip()
        if username.lower()=="exit":
            print(Fore.MAGENTA + "The Tool is closing now,Thanks for visiting!" +Style.RESET_ALL)
            break
        wrong=[""," ","  ","*","&","^","$","#","@","!",'/','+','-','.',]
        if username in wrong or username.isnumeric():
            print(Fore.YELLOW + "[!] please enter valid username" + Style.RESET_ALL)
            continue
        check_username(username)     

