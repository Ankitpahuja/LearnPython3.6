#Q1: From a number for eg 3245 display in words "Three Two Four Five"

lists = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
input_num = input("Etner the number and i will give you the desired output: ")

for i in range(len(input_num)):
    print(lists[int(input_num[i])])
    


#Q2: Get a list of unique words from a string

input_string = input("Enter a string please: ")
print(input_string)
into_set = set (input_string.split())
print(into_set)


#Q3: Build a list of unique words and a corresponding list of freq

s="A CAT RAN AFTER A DOG WHO RAN"
L1 = s.split()
unique_L1 = set(L1)
frq = []

for w in unique_L1:
    frq.append(L1.count(w))
print(unique_L1)
print(frq)

#q4: Display all prime numbers between two limits

l_limit = int(input("Enter the lower limit: "))
u_limit = int(input("Enter the upper limit: "))


for num in range(l_limit,u_limit + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

#q5: Store the prime numbers of question 4 into a list


l_limit = int(input("Enter the lower limit: "))
u_limit = int(input("Enter the upper limit: "))
lists = []

for num in range(l_limit,u_limit + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           lists.append(num)            
print(lists)


#q6: We need to store factorials of 0 to 9 in a list called F

u_num = int(10)
lists = [1]

for a in range(1,u_num):
    fact = int(1)
    for i in range(1,a+1):
        fact*=i
    lists.append(fact)
print(lists)


#q7:

#Q8:

#Q9:  Break a string into fields using a field separator.

s="101:Deepak Taneja:2001:A"
l = s.split(":")
print(l)

#Q10: Translation of a DNA strand containing ATGC characters. A is converted to T, T to A, C to G and G to C. ---REDO

D = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
S="ATGCATGGCCC"
lists=list(S)
for i,j in enumerate(lists):
    lists[i]=D[j]

print(lists)


#Q11:  From a string build a list of all words that start with a particular alphabet

s="I am a dude of all trades"
lists_1 = list(s)
lists_2 = []
for i,j in enumerate(lists_1):
    if (lists_1[i] == ' '):
        continue
    else:
        lists_2.append(lists_1[i][0])

print(lists_2)



