'''

Understanding HotPotato Game:
One of the typical applications for showing a queue in action is to simulate a real situation that requires data to be managed in a FIFO manner.
To begin, let’s consider the children’s game Hot Potato. In this game, children line up in a circle and pass an item from neighbor to neighbor as
fast as they can. At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle.
Play continues until only one child is left.

To simulate the circle, we will use a queue. Assume that the child holding the potato will be at the front of the queue. Upon passing the potato,
the simulation will simply dequeue and then immediately enqueue that child, putting her at the end of the line. She will then wait until all the others
have been at the front before it will be her turn again. After num dequeue/enqueue operations, the child at the front will be removed permanently and another
cycle will begin. This process will continue until only one name remains (the size of the queue is 1).

'''
from Queue_ADT_Imp import Queue

def hotPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue() # At last queue is empty reurning the last man standing.

print(hotPotato(["Ankit","Asmita","Shweta","Brad"],3))
    
