import threading

from pprint import pprint
import time

def new_func():
    
    pprint(threading.active_count())
    print()
    pprint(threading.enumerate())
    print()
    pprint(threading.current_thread())
    

def greetings_1():
    for i in range(6):
        print("Hello")
        time.sleep(1)
        
def greetings_2():
    for i in range(6):
        print("World")
        time.sleep(1)

start_time = time.time()

t1 = threading.Thread(target = greetings_1)
t2 = threading.Thread(target = greetings_2)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()

print("Total time:", end_time-start_time)

#greeting_1()
#greeting_2()  one thread processing the 12 calls

#Hello
#Hello
#Hello
#Hello
#Hello
#Hello
#World
#World
#World
#World
#World
#Total time: 12.062554121017456

# with 2 threads we halve the time it takes

#Hello
#World
#HelloWorld
#
#Hello
#WorldHello
##
#World
#Hello
#World
#World
#Hello
#Total time: 6.080993175506592