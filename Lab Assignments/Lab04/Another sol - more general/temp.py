import re
with open("file.txt","r") as fp:
    temp = fp.read()
    l = re.findall(r"[\w']+", temp)
    sample = list()
    for a in set(l):
        word = a
        freq = l.count(a)
        sample.append((word,freq))

data_with_sorted_freq =(sorted(sample,key=lambda x:x[1]))
for data in data_with_sorted_freq:
    print(data[0],":",data[1])
