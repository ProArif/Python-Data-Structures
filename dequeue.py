# A double-ended queue, or deque, has the feature of adding and removing elements from either end.

import collections

#Create a dequeue
doubleEndedDequeue = collections.deque(['Sun','Mon'])

#Append to the right
doubleEndedDequeue.append('Tue')

print(doubleEndedDequeue)

#Append to the left
doubleEndedDequeue.appendleft("Sat")
print(doubleEndedDequeue)

#remove from the right
doubleEndedDequeue.pop()
print(doubleEndedDequeue)

#remove from the left
doubleEndedDequeue.popleft()
print(doubleEndedDequeue)

#reverse the dequeue
doubleEndedDequeue.reverse()
print(doubleEndedDequeue)