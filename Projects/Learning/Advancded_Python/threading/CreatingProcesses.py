import threading
from pprint import pprint
import time
import queue
import os
from multiprocessing import Process, current_process

def square(number):
    
    time.sleep(1)
    result = number * number
    
#    process_id = os.getpid()
    process_id = os.getpid()
    process_name = current_process().name
    
    print("Process ID", process_id)
    print("Process Name", process_name)
    
numbers = [1, 2, 3, 4]

start_time = time.time()

for i, number in enumerate(numbers):
    
    if __name__ =='__main__':
    
        process = Process(target=square, args=(number,))
        process.start()
    
        process.join()
    
end_time = time.time()
total_time = end_time - start_time
print(total_time)
