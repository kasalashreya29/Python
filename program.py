import threading
import time

def f_square(n):
    for i in n:
        time.sleep(0.5)
        print("square=",n*n)

def f_cube(m):
    for i in n:
        time.sleep(0.7)
        print("cube=",n*n*n)
a=[1,2,3,4]
t1=threading.Thread(target=f_square,args=(a1))
t2=threading.Thread(target=f_cube,args=(a1))
t1.start()
t2.start()
t1.join()
t2.join()