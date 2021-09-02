import socket
import threading

HEADER = 64
PORT = 80
FORMAT = 'utf-8'
CONNECT_MESSAGE = "CONNECT"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "put your public IP"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def recive():
    while(enSesion):
        print("OTRO: " + client.recv(2048).decode(FORMAT))

def sesion():
    global enSesion
    enSesion = True
    send(CONNECT_MESSAGE)
    print("ESCRIBI UN MENSAJE Y ENTER")
    print("0 - SALIR")

    #hilo para responder mensajes
    thread = threading.Thread(target=recive, args=())
    thread.start()

    while(enSesion):
        message = input()
        if message == "0":
            send(DISCONNECT_MESSAGE)
            client.close()
            enSesion = False
        else:
            send(message)


sesion()