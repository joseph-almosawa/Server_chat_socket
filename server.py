import socket 
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
FORMATE = 'utf-8'
DISCONNECT_MESSSAGE = "exit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) 


def handle_client(conn, addr):   # here will handle the indvidual connection between the client and the server
    print(f"[NEW CONNECTION] {addr} Connected.")

    while True:
        msg_length = conn.recv(HEADER).decode(FORMATE)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMATE)
            if msg == DISCONNECT_MESSSAGE:
                break

        print(f"[{addr}] {msg}")

    conn.close()


def start():   # to handle new conncections and distribute those to where they need to go 
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()        # this line will wait for new connection to the server to store the adress of that connaction what IP adress and what port it came
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections]{threading.activeCount() -1}")
        

print("[STARTING] server is starting...")
start()
