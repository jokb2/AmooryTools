import os
import sys

def fake_destroy():
    print("""
لو كان هذا السكريبت حقيقي كان حذف كل ملفاتك
لكن لا تخاف هذا مجرد مثال تعليمي 
الأمر الذي كان بيتنفذ هو الأمر ذا  
rm -rf /  
وكان جهازك بيودع وكل ملفاتك تروح                                    
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