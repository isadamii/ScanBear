from pyfiglet import Figlet
import sys
import socket
from datetime import datetime
import threading

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open!".format(port))
        s.close()

    except KeyboardInterrupt:
        print("Exiting, See you later!")
        sys.exit()
    except socket.error:
        print("Server not responding!")
        sys.exit()

def main():
    f = Figlet(font='big')
    print(f.renderText('ScanBear'))
    print("         A Multi Thread Port Scanner.")
    print("     Developed by isadami | dsc.gg/isadami")
    print("")
    print("[TARGET IP ADDRESS/DOMAIN]")
    target = input(">> ")
    target = socket.gethostbyname(target)
    print("")
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)
    print("")
    
    threads = []
    try:
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target, port))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("Exiting, See you later!")
        sys.exit()
    except socket.gaierror:
        print("Hostname Could Not Be Resolved!")
        sys.exit()

if __name__ == "__main__":
    main()
