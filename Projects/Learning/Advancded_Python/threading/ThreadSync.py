import threading
from pprint import pprint
import time

amount = 0

def deposit(dep_amount, dep_lock):
    
    global amount
    for i in range(dep_amount):
        dep_lock.acquire() #added to add lock to thread
        amount += 1
        dep_lock.release() #release lock

def two_deposit_threads(dep_amount):
    
    lock = threading.Lock()
    
    t1 = threading.Thread(target = deposit, args=(dep_amount, lock))#PASSING same lock to both threads thats the sync
    t2 = threading.Thread(target = deposit, args=(dep_amount, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

#two_deposit_threads(10) this had no problem updating to 20
#two_deposit_threads(1000) no sync problems
two_deposit_threads(1000000) # this gives problems the value Balance amount = 1493853 when no locks

print("Balance amount = {0}".format(amount)) # successful 2Million output with lock

semaphore = threading.Semaphore(value = 3)#with no associated value it works like a lock one at a time

def my_func():
    
    semaphore.acquire()
    
    time.sleep(0.1)
    print(threading.current_thread().name, " acquired the semaphore. ")
    print("Semaphore value after acquire:", semaphore._value)
    
    time.sleep(5)
    
    semaphore.release()
    
    print("Semaphore value after release:", semaphore._value)
    
t3 = threading.Thread(target=my_func)
t4 = threading.Thread(target=my_func)
t5 = threading.Thread(target=my_func)
t6 = threading.Thread(target=my_func)
t7 = threading.Thread(target=my_func)
t8 = threading.Thread(target=my_func)
t9 = threading.Thread(target=my_func)
t10 = threading.Thread(target=my_func)

print("Initial semaphore value", semaphore._value)

start_time = time.time()

t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

end_time = time.time()

print("Total time:", end_time-start_time)