import re
pattern = re.compile(r"[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+)\.[a-zA-Z0-9-.]+")

'''
# Using findall Method for RE
with open("file.txt","r") as fp:
    data = fp.read()
    found = pattern.findall(data) #findall() returns a list
    print(found)

'''


'''
# Using a match object
fp=open("file.txt","r")
for s in fp:
    matchObject = pattern.match(s)
    if (matchObject):
        print(matchObject.group(1)) #prints all gmail/mail delivery 

'''
