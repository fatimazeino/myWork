# queuelist.py
# This program reads on a queue
# Author: Fatima Zeino

import random
queue = []
numberofNumbers = 10
rangeTo = 100

for n in range(0,numberofNumbers):
    queue.append(random.randint(0,rangeTo))

print("queue is {}".format(queue))

while len(queue)!= 0:
    currentNumber = queue.pop(0)
    print("Current number is {} and the queue is {}".format(currentNumber,queue))
print("the queue is now empty")