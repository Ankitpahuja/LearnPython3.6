'''

This snippet of code will make implementations of a queue.

We need to decide which end of the list to use as the rear and which to use as the front. The implementation assumes  that the rear is at position -1(last) in the list.
This allows us to use the append function on lists to add new elements to the rear of the queue. The pop operation can be used to remove the front element
(the first element of the list). Recall that this also means that enqueue will be O(1) and dequeue will be O(n). Another approach is discussed in the last.

'''


class Queue:
    def __init__(self):
        self.items = list()
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        if len(self.items)>0:
            return False
        else:
            return True
    def size(self):
        return len(self.items)

# Main Program Proceeds
'''
q=Queue()
q.enqueue(21)
print(q.isEmpty())
print (q.size())
print (q.dequeue())
print (q.size())
'''        
    
'''

Another approach:

We need to decide which end of the list to use as the rear and which to use as the front. The implementation assumes that the rear is at position 0 in the list.
This allows us to use the insert function on lists to add new elements to the rear of the queue. The pop operation can be used to remove the front element
(the last element of the list). Recall that this also means that enqueue will be O(n) and dequeue will be O(1).

'''
