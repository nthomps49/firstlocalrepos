import threading

from pprint import pprint
import time

def new_func():
    
    pprint(threading.active_count())
    print()
    pprint(threading.enumerate())
    print()
    pprint(threading.current_thread())
    

#def func():
#    print("Hello from func! \n")

def func():
    time.sleep(2)
    print("\nHello from func: My name is", threading.current_thread().getName())
    
def sleeping_func():
    time.sleep(2)
    print("\nHello from sleeping_func!")

def calc_square(n):
    result = n*n
    print(f"the number {n} squares to {result}.")
    
class DerivedThread(threading.Thread):
    
    def run(self):
        time.sleep(2)
        print("\nHello from func: My name is", threading.current_thread().getName())
        
obj = DerivedThread()

obj.start()
obj.join()

print("Control returned to", threading.current_thread().getName())
    
x = threading.Thread(target = func, name = 'brand_new_threadx')
x.start()
#.join method means wait for other threads actions to complete first. so we see sleep func print first
x.join()

print("\nThis is the Main thread. My name is", threading.current_thread().getName())



#y = threading.Thread(target= sleeping_func)
#y.start()

#print(new_func())

square_list = []
num_list = [1, 2, 3, 4]

for n in num_list:
    
    thread = threading.Thread(target=calc_square, args=(n, ))
    square_list.append(thread)
    
    thread.start()
    thread.join()

