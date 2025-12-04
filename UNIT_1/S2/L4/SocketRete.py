import socket

SRV_ADDR = "192.168.1.101"  #indirizzo ip della kali ottenuto nel terminale tramite "ip a "

SRV_PORT = 44444 #scelgo porta non usata da altri servizi e uso il comando in terminale  " sudo lsof -i :44444"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #do  info che si tratta di ipv4 e porta tcp (SOCK_STREAM)

s.bind((SRV_ADDR, SRV_PORT)) #assegno al socket porta e indirizzo server 

s.listen(1) #per far eventualmente ascoltare piu cose una in coda all'altra 

print(f"Server in ascolto alla porta {SRV_PORT}")

connection, address = s.accept() #chide 2 risposte e rsponde con 2 cose, una per connection una per address. UNo è l'indirizzo ip di chi ci contatta e variabile con dati passati 

print(f"Siamo stati contattati da {address}") #accesso all'indirizzo di chi ci contatta 

while True : 

    data = connection.recv(8) #blocco di codice diviso ogni 8 byte 

    if data == b'exit\n': break #se scrivo exit esco 

    connection.sendall('b ricevuto\n')  

    print(data.decode("UTF-8")) #decodifica in utf 8 per renderlo leggibile  

connection.close() #chiude connessione 
        



