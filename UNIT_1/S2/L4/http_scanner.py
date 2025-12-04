import http.client

host = input("Inserire IP: ")
port = input ("Inserire porta(default 80): ")

if(port == ''): #se non mi da nulla di dafult la porta 80

    port = 80 

else:

    port = int(port)#se non è 80 la converto in un intero 
try: #esegue codice 

    connection = http.client.HTTPConnection(host, port) #creo connessione 

    connection.request("OPTIONS", "/") #se è accettato ti dice cio che è supportato e ciò che non è supportato, in questo caso faccio la richiesta sulla home dato dallo /

    response = connection.getresponse() #risposta dal server, sta in attesa fino ache non arriva 

    print(response)

    print("status: ", response.status)

    body_bytes = response.read() #prendo body bytes leggo e dopo lo decodifico in utf 8 
    body_string = body_bytes.decode("utf-8")

    print(body_string)

    connection.close()

except ConnectionRefusedError: #invece di scoppiare il codice da errore

    print("Connessione fallita")


#per provarlo usare ad esempio 2a00:1450:4002:415::200e che è l'ip v6 di goggle e da output ma va solo sulla porta 80 non 443 poichè manca modulo 