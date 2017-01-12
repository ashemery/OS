from socket import *
from threading import Thread

def clientHandler():
    conn, addr = s.accept()
    print (addr, " is connected")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received the message: ", repr(data))
        conn.send(data)

HOST=''
PORT = 9091

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(5)

print ("The server is now running!")

for i in range(5):
    Thread(target=clientHandler(), daemon=True).start()

# while True:
#    clientSock, addr = s.accept()
#    print (addr, " is connected")
#    Thread(clientHandler, args=(clientSock,), daemon=True).start()

s.close()
