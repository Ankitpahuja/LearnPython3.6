#Read from a file and parse all the phone numbers from the file using reg expressions!
import re

with open("extract.txt","r") as n:
    fp=n.readlines()
    pattern=re.compile("\+\d\d-\d{10,10}") #This is a reg expression.
    for a in fp:
        matchObject = pattern.findall(a)
        if (matchObject):
            print(matchObject)
            
        
