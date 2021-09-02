import socket 
import threading

HEADER = 64
PORT = 80
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "put your router IP"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr, clients):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length != "":
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            for i in clients:
                if i != conn:
                    print(f"[{addr}] {msg}")
                    print("Mensaje enviado a: ")
                    i.send(msg.encode(FORMAT))
    
    conn.close()

def start():
    server.listen()
    print("[LISTENING] server is listening on "+SERVER)
    clients = []
    while True:
        conn, addr = server.accept()
        if (addr) not in clients:
            clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr, clients))
        thread.start()
        print(f"[ACIVE CONNECTION] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()