#Import
import socket
import threading
import concurrent.futures
import colorama

#From-Import
from datetime import datetime
from colorama import Fore
from colorama import Style

my_ip = socket.gethostbyname(socket.gethostname())
print_lock = threading.Lock()


def portscan():
    colorama.init()
    
    print(Fore.BLUE + "INFORMACION: ")
    print(Fore.BLUE + "ip_address: " + my_ip)
    rangeport = int(input(Fore.WHITE + "Introduce el puerto maximo para Escanear: " + Fore.YELLOW + "~$ " + Style.RESET_ALL))
    ip = input(Fore.WHITE + "Introduce la IP a Escanear: " + Fore.YELLOW + "~$ " + Style.RESET_ALL)

    print("*" * 50)
    print(f"{Fore.GREEN}Escaneando a:{Style.RESET_ALL} {ip}")
    print(Fore.GREEN + "Escaneo iniciado :" + Style.RESET_ALL + str(datetime.now()))
    print("*" * 50)

    def scan(ip, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        try:
            scanner.connect((ip, port))
            scanner.close()
            with print_lock:
                print(Fore.WHITE + f"[{port}]" + Fore.GREEN + "Opened")
                
        except:
            pass
        
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(rangeport):
            executor.submit(scan, ip, port + 1)

if __name__ == '__main__':
    portscan()