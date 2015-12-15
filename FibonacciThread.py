#!/usr/bin/python3
#calculate fibonacci using Threads
from socket import *
from threading import Thread
import datetime

# Fibonacci Network Server
def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("[+] Connection started with: ", addr)
        Thread(target=fib_handler_yield, args=(client,), daemon=True).start()

#Calculating fibonacci
def fibonacci_yield(n):
    l1=1; yield 1
    l2=1; yield 1
    for i in range(2,n):
       l=l1+l2;
       yield l
       l1, l2 = l2, l

#Network fibonacci client handler
def fib_handler_yield(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        a = datetime.datetime.now()
        results=list(fibonacci_yield(n))
        #results = itertools.islice(l, n)
        b = datetime.datetime.now()
        diff = b - a
        print ("the calc took: %d days" % diff.days)
        print ("the calc took: %d seconds" % diff.seconds)
        print ("the calc took: %d microseconds" % diff.microseconds)

        resp = str(results[n-1]).encode('ascii') + str(diff.microseconds).encode('ascii') + b'\n'
        client.send(resp)
    print("[+] Connection Closed !!!")

fib_server(('',25001))

#Testing yield
#x = fibonacci_yield(n)
#print(x.__next__())
