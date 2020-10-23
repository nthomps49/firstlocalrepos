import queue
import time
#setup for normal add and remove FIFO from queue
#q = queue.Queue()
#
#for i in range(7):
#    q.put(i)
#    
#print(list(q.queue))
#
#print(q.empty())
#
#while not q.empty():
#   print(q.get())
#    
#print(q.empty())

#implements a stack LIFO
#q = queue.LifoQueue()
#
#for i in range(7):
#    q.put(i)
#    
#while not q.empty():
#    print(q.get())

#implement a priority queue
q= queue.PriorityQueue()

q.put(5)
q.put(4)
q.put(1)
q.put(3)
q.put(2)

while not q.empty():
    print(q.get())