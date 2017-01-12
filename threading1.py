import threading

mydata = threading.local()
mydata.x = 1

def ThreadFunction(x):
    print ('running thread function: ', x)
    return

if __name__ == '__main__':
    for i in range(5):
        #t = threading.Thread(target=ThreadFunction(i))
        # Another way of passing arguments
        t = threading.Thread(target=ThreadFunction, args=(i,))
        t.start()

    import matplotlib.pyplot as plt
    vals = [3,2,5,0,1]
    plt.plot(vals)