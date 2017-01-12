from queue import Queue
from threading import Thread
import requests

inQ = Queue()
outQ = Queue()

def worker():
    while True:
        url = inQ.get()
        resp = requests.get(url)
        outQ.put((url, resp.status_code, resp.text))

numWorkers = 10
ts = [Thread(target=worker) for i in range(numWorkers)]

for t in ts:
    t.start()