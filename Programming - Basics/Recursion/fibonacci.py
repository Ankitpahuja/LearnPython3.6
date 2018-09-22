def fibo(num):
    if (num<=0):
        return "incorrect input" #num>0
    elif (num==1):
        return 0 #1st term in fibo sequence is 0
    elif (num==2):
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


# Main Program Starts
print(fibo(21))
