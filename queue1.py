from queue import Queue


my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print (my_list.pop(0))
# Outputs: 1

print (my_list)


my_queue = Queue(maxsize=0)
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)
print (my_queue.get())
my_queue.task_done()
# Outputs: 1

#print (my_queue.)

for i in my_queue._get():
    print (i)