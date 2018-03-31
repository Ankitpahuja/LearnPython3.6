'''
anurag = "Anurag"
f=open("Anurag.txt")
s = f.readlines()
for i in s:
    if anurag in i:
        print(i)
'''
anurag="Anurag"  
L = [i for i in (open("Anurag.txt").readlines()) if(anurag in i)]
for p in L:
    print (p)
