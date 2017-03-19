import threading

def add(x):
    print(1/0)
    # print(x)

x = 1
threads = []
for i in range(5):
    p = threading.Thread(target=add, args=(x,))
    threads.append(p)
    p.start()

import time
time.sleep(5)

for p in threads:
    print(p.is_alive())
    p.join()
print('1')
