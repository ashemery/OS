from socket import *
from threading import Thread
import time
import datetime
import itertools

def fibonacci1(n):
    '''fibonacci using recursive method'''
    if n <= 2:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n):
    '''fibonacci using iterative method '''
    a, b = 0, 1
    for item in range(n):
        a, b = b, a + b
    return a

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("[+] Connection started with: ", addr)
        #Thread(target=fib_handler, args=(client,), daemon=True).start()
        Thread(target=fib_handler_yield, args=(client,), daemon=True).start()

def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        result = fibonacci(n)   # using the unefficient fibo
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print("[+] Connection Closed !!!")

def fibonacci_yield(n):
    l1=1; yield 1
    l2=1; yield 1
    for i in range(2,n):
       l=l1+l2;
       yield l
       l1, l2 = l2, l

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

#for i in itertools.islice(l, 100):
#    print (i)
fib_server(('',25001))

#x = fibonacci_yield(n)
#print(x.__next__())