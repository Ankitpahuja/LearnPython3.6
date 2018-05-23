'''
Since, we are talking about abstract data types and abstractness means more of a logical view and is theoritical in nature.
There can be multiple ways of implementing Stack and proving its abstractness with keeping principles of LIFO alive.

1st Way: Implementing it as a vertical stack and keeping top as the newest element added and base as the first element added to be popped out in the last.
2nd Way: Implementing it as a horizontal stack where all elements are added in the first place (index 0) and every previous added would shift by 1 value to a later index
        and this way, we preserve LIFO properties. 
'''

# Way 1
class Stack:
    def __init__(self):
        self.list = []
    def push(self,item):
        return self.list.append(item)
    def pop(self):
        return self.list.pop()
    def peek(self):
        return self.list[-1]
    def isEmpty(self):
        if len(self.list)>0:
            return False
        else:
            return True
    def size(self):
        return len(self.list)

# Way 2
'''
class Stack:
    def __init__(self):
        self.list=list()
    def isEmpty(self):
        return self.list == []
    def push(self,item):
        self.list.insert(0,item)
    def pop():
        self.list.pop(0)
    def peek(self):
        return self.list[0]
    def size(self):
        return len(self.list)
'''

# Main Program Proceeds
# Commenting main program since this file is used in another one!
''' 
s = Stack()
s.push(10)
print(s.peek())
s.pop()
print(s.isEmpty())
s.push([20,30,40])
print(s.peek())
print(s.size())
'''




'''
Asymptotic Analysis:

This ability to change the physical implementation of an abstract data type while maintaining the logical characteristics is an example of abstraction at work.
However, even though the stack will work either way, if we consider the performance of the two implementations, there is definitely a difference.

Recall that the append() and pop() operations were both O(1). This means that the first implementation will perform push and pop in constant time no matter
how many items are on the stack.

The performance of the second implementation suffers in that the insert(0) and pop(0) operations will both require O(n) for a stack of size n.

Clearly, even though the implementations are logically equivalent, they would have very different timings when performing benchmark testing.

'''
