class Stack:

    def __init__(self):
        self.stack = []

    def add(self,value):
        #add value in the stack
        if value not in self.stack:
            self.stack.append(value)
            return True

        else:
            return False

    def peek(self):
        #View element at top of the stack (First element of the stack)
        return self.stack[0]

    def remove(self):
        #remove element from the stack
        if len(self.stack) <=0:
            return "There is no element in the stack"

        else:
            return self.stack.pop()   

    def size(self):
         return len(self.stack)      

Astack = Stack()
Astack.add("Sat")
Astack.add("Sun")
Astack.add('Mon')
print(Astack.peek())
print()
print(Astack.size())
Astack.add('Tue') 
print(Astack.remove())
print(Astack.remove())
print()
print(Astack.peek())
print()
print(Astack.remove())



