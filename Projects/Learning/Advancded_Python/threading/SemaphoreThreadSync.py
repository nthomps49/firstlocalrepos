import threading
from pprint import pprint
import time

semaphore = threading.Semaphore(0)

order_num = 0

def place_order():
    print("Order Placed. ")
    semaphore.acquire()
    print("Customer order number is:", order_num)
    
def prepare_order():
    
    global order_num
    time.sleep(3)
    order_num +=1
    
    print("Preparing order number", order_num)
    semaphore.release()

for i in range(0, 6):
    
    t1 = threading.Thread(target=place_order)
    t2 = threading.Thread(target=prepare_order)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
print("Program terminated")

#there are also bounded semaphores with strict upper limit on value of threads that can access it
#semaphore = threading.BoundedSemaphore(1) - now calling release over and over will not increase the free available. It stays at the bound

