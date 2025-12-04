import socket 

target = input("Ip da scansionare: ")

portrange = input("Range di porte (es: 20-100 porta min e porta massima): ") #inserire range di porte da vedere 

lowport = int(portrange.split('-')[0]) #splitto e trovo il minimo in posizione [0]

highport = int(portrange.split('-')[1]) #splitto e trovo il max in posizione [1]

print(f"Scannerizzo l'Ip {target} dalla porta minima {lowport} alla porta massima {highport}")

for port in range (lowport, highport + 1) : #parte dalla porta piu bassa e arriva a quella piu alta includendola 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #indico che è IPv4 e che la porta è TCP 

    status = s.connect_ex((target, port)) #prima info è target seconda è la porta poresa dal ciclo 

    if (status == 0 ) : #se il risultato dello status è 0 vuol dire che la porta è aperta se no è chiusa 
        
        print(f"Porta {port} : Aperta ")
    else:
        print(f"Porta {port}: Chiusa")
    s.close()