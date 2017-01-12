import time
import itertools

def fab():
    l1=1; yield 1
    l2=1; yield 1
    while(True):
       l=l1+l2;
       yield l
       l1, l2 = l2, l

l=fab()
for i in l:
    print i
    time.sleep(1)
