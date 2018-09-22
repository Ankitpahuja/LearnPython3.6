L1 = [1,2,3,4,5,6]
L2 = ["Ankit", "Anmol", "Anjula", "Anand", "Atreja", "Deepti"]

'''

D = {}
for x in zip(L1,L2):
    D[x[0]]=x[1]
print(D)

'''

D = {k:v for (k,v) in zip(L1,L2)}
print(D)
