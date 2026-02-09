import socket
import pickle
server_socket = socket.socket()
host = '127.0.0.1'
port = 7654

try:
    f = open('utenti.dump', 'rb')
    try:
        utenti = pickle.load(f)          
    finally:
        f.close() 
except: 
    utenti = {'admin':'èsegreta'}
    
server_socket.bind((host, port))
server_socket.listen(1)
for i in range(5):
    conn, addr_p = server_socket.accept() 
    print(f"Connected by {addr_p}\n") 
    conn.sendall(b'Indicami il tuo username: ') 
    username = conn.recv(1024).decode()
    conn.sendall(b'Indicami la tua password: ')
    password = conn.recv(1024).decode()
    if username == 'admin' : 
        if utenti[username] == password:
            conn.sendall(str(utenti).encode())
        else:
            conn.close()
            continue
    else: 
        utenti[username] = password
    conn.close()
server_socket.close()
f = open('utenti.dump', 'wb')
pickle.dump(utenti, f)
f.close()
