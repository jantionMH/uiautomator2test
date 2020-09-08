import threading
import multiprocessing
import time
import random
import gevent
count=0

def login1():

       print(  'm6vip1.com')
       time.sleep(2)
time.sleep(1)
def login2():

    print('m6vip2.com')
    time.sleep(2)

def login3():

    print('m6vip3.com')
    time.sleep(2)
g1=gevent.spawn(login1)
g2=gevent.spawn(login2)
g3=gevent.spawn(login3)
gevent.joinall([g1,g2,g3])
#
# if __name__ == '__main__':
#
#   for i in range(10):
#
#      threading.Thread(target=login).start()
#      multiprocessing.Process(target=login(i)).start()
