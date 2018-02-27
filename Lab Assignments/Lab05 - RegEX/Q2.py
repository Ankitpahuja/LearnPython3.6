#Read from a file and parse all the phone numbers from the file using reg expressions with varying length!
import re

with open("extract.txt","r") as n:
    fp=n.readlines()
    pattern=re.compile("\+\d\d") #This is a reg expression.
    pattern_2=re.compile("\+\d\d-\d{8,10}")
    pattern_3=re.compile("\+\d\d-\d{7,11}")
    pattern_4=re.compile("\+\d\d-\d{10,10}")
    for a in fp:
        matchObject = pattern.search(a)
        if (matchObject.group() == '+91'):
            matchObjects = pattern_2.search(a)
            if matchObjects:
                print(matchObjects.group())
        elif (matchObject.group() == '+92'):
            matchObjects = pattern_3.search(a)
            if matchObjects:
                print(matchObjects.group())
        elif (matchObject.group() == '+93'):
            matchObjects = pattern_4.search(a)
            if matchObjects:
                print(matchObjects.group())
        
        
