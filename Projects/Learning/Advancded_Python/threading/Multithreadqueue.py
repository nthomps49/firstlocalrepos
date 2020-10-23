import threading
from pprint import pprint
import time
import random
import queue

counter = 1
more_to_come = True
q = queue.Queue()

class Producer(threading.Thread):
    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        
        global counter
        global more_to_come
        
        for i in range(5):
            
            time.sleep(random.randrange(2, 5))
            item = "News item #" + str(counter)
            
            self.queue.put(item)
            counter += 1
            
            print("\nProduced:", item)
            
        more_to_come = False
        
class Consumer(threading.Thread):
    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        
        while (more_to_come):
            item = self.queue.get(timeout=10)
            time.sleep(random.random())
            print(threading.current_thread().getName(), "popper: ", item)
            
        print(threading.current_thread().getName(), "exiting...")
        

producer_thread = Producer(q)
consumer_thread = Consumer(q)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
