global R,B,C,Y,G,RT,CY,CO;CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"
import os, sys, time
# Script Name: Requiem
# https://docs.python.org/3.5/library/smtplib.html 
# http://stackoverflow.com/a/27515833/2684304
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
if __name__ == '__main__':
    os.system('clear')
    print(f'{C}[{G}!{C}] Checando Atualizações')
    run(["git", "pull"])
    system('clear')
    print(b.banner)
    time.sleep(2)
os.system('python3 encrypt_sx.cpython-39.pyc')
