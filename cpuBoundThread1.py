from queue import Queue
from threading import Thread

inQ = Queue()
outQ = Queue()

def worker():
    while True:
        l = inQ.get()
        sumL = sum(l)
        outQ.put(sumL)

numWorkers = 10
ts = [Thread(target=worker) for i in range(numWorkers)]

for t in ts:
    t.start()