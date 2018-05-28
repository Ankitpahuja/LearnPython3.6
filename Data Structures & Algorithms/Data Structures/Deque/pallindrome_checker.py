'''

Code to implement palindrome checker!

A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam.

'''

from deque_ADT_Imp import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch) # Appending all characters into the deque

    stillEqual = True # Acting as a flag element

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
