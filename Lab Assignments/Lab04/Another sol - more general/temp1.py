import re
fp=open("file.txt","r")
l=list()
for s in fp:
    l.append(s.rstrip('\n'))
print(l)
fp.close()
