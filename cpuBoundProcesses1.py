from multiprocessing import Process, Queue

def worker(inQ, outQ):
    while True:
        l = inQ.get()
        sumL = sum(l)
        outQ.put( sumL )


inQ = Queue()
outQ = Queue()

#creating a single new process
#p = Process(target=worker, args=(inQ, outQ))
#p.start()

#Creating 10 new processes
#use ps -eLf to show them with grep for sure :)
numWorkers = 10
processList = [Process(target=worker, args=(inQ, outQ)) for i in range(numWorkers)]

for process in processList:
    process.start()