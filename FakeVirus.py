import os
import sys

def fake_destroy():
    print("""
If this script were real, it would delete all your files.
But don't worry, this is just an educational example.
The command that would be executed is this command:
rm -rf /
And your phone will say goodbye, and all your files are gone.    
""")
    
def main():
    print("Amoory Fake virus tool")
    print("This tool is an educated tool and do not harm anyone")   
    choice=input("start?(y/n):")
    if choice.lower()=='y':
        fake_destroy()
    else:
        print("Cancel,Done")        

if __name__=="__main__":

    main()
