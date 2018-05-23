'''
Part 1:
Write a function revString(mystr) that uses a stack to reverse the characters of a string. (5 Points)
    revString(“apple”) # should return “leppa”

Part 2:
Additional Bonus: Manage to pass the sent string and the returned string (revString) to another function testEqual() and let the user know if those are exact reverse
or not! (5 Points)
    testEqual(revString(‘apple’),’leppa’) # should return “TEST PASS”


'''

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

'''
Or, Use the following line:

from Stack_ADT_Imp import Stack

'''
def revString(mystr):
    mystack = Stack()
    revstr = str()
    for ch in mystr:
        mystack.push(ch)
    while not mystack.isEmpty():
        revstr = revstr + mystack.pop()
    return revstr


# Main Program Proceeds
t = revString('apple')
print(t)

'''
TestEqual() function is for another 5 points. :)
'''

def testEqual(str1,str2):
    if str1 == str2:
        return "Pass"
    else:
        return "Fail"

u = testEqual(revString("apple"),"elppa")
print(u)
    
