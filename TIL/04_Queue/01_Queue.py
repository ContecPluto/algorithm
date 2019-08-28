from queue import Queue

q = Queue()
for i in range(1, 4):
    q.put(i)

while q.qsize():
    print(q.get())