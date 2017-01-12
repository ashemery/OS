from threading import Thread

def myfunc():
    print ("hello, world!")

thread1 = Thread(target=myfunc)
thread1.start()
thread1.join()

from threading import Thread

class MyThread(Thread):
    def run(self):
        print ("I am a thread!")

foobar = MyThread()
foobar.start()
foobar.join()