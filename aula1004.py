#você é isso, uma beleza imensa, toda recompensa de um amor sem fim, você é isso uma nuvem calma do céu de minh'alma que aquece em mim
#teste

# Prog_Ex3_Thread.py

import threading
import time
import random

def minhathread(n):
    global numthreads
    print("Sou Thread {0}, vou dormir.\n".format(n))
    t = random.randint(1,3)
    time.sleep(t)
    numthreads += 1
    print("Thread {0} depois de {1}s\n".format(n, t))
    
numthreads = 0
threads = [ ]
for i in range(10):
    t = threading.Thread(target=minhathread, args=(i,))
    threads.append(t)
    t.start()

for x in threads:
    x.join()

print("{0} threads executadas!".format(numthreads))