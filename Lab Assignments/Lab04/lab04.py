with open("temp.txt","r") as temp:
    temperature = []
    temperature = temp.readlines()
    count,summ = 0,0
    for a in temperature:
        summ = summ + float(a)
        count+=1
    avg = summ/count

print(avg)
