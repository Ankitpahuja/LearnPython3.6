# Includes all the functions relationg to learnt DS & Algorithms.

def LinearSearch(list,item):
    position = 0
    found = False
    while position<len(list) and not found:
        if list[position] == item:
            found = True
            return position
        position+=1


#def BinarySearch(list,item):
