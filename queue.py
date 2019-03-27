class Queue():

    def __init__(self):
        self.queue = list()

    def addtoqueue(self,value):
        #add element to the queue
        if value not in self.queue:
            self.queue.insert(0,value)
            return True
        return False   

    def removetoqueue(self):
        #remove element from the queue
        if len(self.queue) > 0:
            print('Length of the queue {}'.format(len(self.queue)))
            return self.queue.pop()
            

        return "There is no element on the queue"     
AQueue = Queue()
AQueue.addtoqueue(10)
AQueue.addtoqueue("4")
print('Removed {} from queue'.format(AQueue.removetoqueue()))  #removes element from the first (FIFO feature)
AQueue.addtoqueue("Godfather")
print('Removed {} from queue'.format(AQueue.removetoqueue()))
print('Removed {} from queue'.format(AQueue.removetoqueue()))
