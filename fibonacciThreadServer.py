from socket import *
from threading import Thread
import datetime

def FibonacciTCPServer(address):
    '''Main Fibonacci TCP Server'''
    ServerSocket = socket(AF_INET, SOCK_STREAM)
    ServerSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    ServerSocket.bind(address)
    ServerSocket.listen(5)
    while True:
        ClientSocket, ClientAddress = ServerSocket.accept()
        print("\n[+] New Connection Started With: ", ClientAddress)
        Thread(target=FibonacciThreadHandler, args=(ClientSocket,), daemon=True).start()

def FibonacciGenerator(iterations):
    '''Fibonacci Series Generator'''
    l1=1; yield 1
    l2=1; yield 1
    for i in range(2,iterations):
       l=l1+l2
       yield l
       l1, l2 = l2, l

def FibonacciThreadHandler(ClientSock):
    '''Fibonacci Thread Handler'''
    while True:
        ClientRequest = ClientSock.recv(100)
        if not ClientRequest:
            break
        intClientRequest = int(ClientRequest)
        TimeBeforeGenerator = datetime.datetime.now()
        results=list(FibonacciGenerator(intClientRequest))
        TimeAfterGenerator = datetime.datetime.now()
        TimeDifference = TimeAfterGenerator - TimeBeforeGenerator
        print("[+]")
        print("[+] The calculation of fibonacci(%d) took the following:" % intClientRequest)
        print("[+] \t%d days" % TimeDifference.days)
        print("[+] \t%d seconds" % TimeDifference.seconds)
        print("[+] \t%d microseconds" % TimeDifference.microseconds)
        print("[+] =====================================================")
        response = str(results[intClientRequest-1]).encode('ascii') + b'\n'
        ClientSock.send(response)
    print("[+] Connection Closed !!!")

# Main Python Program
if __name__ == "__main__":
    ListeningPort = 30001
    print("[+] =====================================================")
    print("[+] \tStarting Fibonacci Multi-Threading Server")
    print("[+] \tListening for New Connections on Port %d" % ListeningPort)
    print("[+] ")
    print("[+] \tUse netcat/ncat to Connect to Server")
    print("[+] \tExample (Windows Version) --> nc.exe 127.0.0.1 %d" % ListeningPort)
    print("[+] \tExample (Linux Version)   --> nc 127.0.0.1 %d" % ListeningPort)
    print("[+] =====================================================")
    FibonacciTCPServer(('',ListeningPort))
