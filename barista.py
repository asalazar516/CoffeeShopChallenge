import time
from datetime import datetime
import sched
import coffeeShop
import threading

queue = list()

def work(item):
    queue.append(item)
    print(queue)
    if(queue[0] == '1'):
        print(f"Cafe is here")
        threading.Timer(4.0, complete, args=(queue)).start()

    elif(queue[0] == '2'):
        print(f"Cappuccino is here")
        threading.Timer(10.0, complete, args=(queue)).start()
        
    elif(queue[0] == '3'):
        print(f"Espresso is here")
        threading.Timer(15.0, complete, args=(queue)).start()

    complete(queue)
    

def complete(queue):
    if (len(queue) > 1):
        print(f"Order #{queue[0]} is ready!")
        queue.pop(0)
        checkout()
        

def checkout():
    threading.Timer(3.0, checkout).start()
    print(f"Order has been picked up!")
