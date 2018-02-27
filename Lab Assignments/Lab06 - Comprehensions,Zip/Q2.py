"""  We have a CSV file of following format:
rollno, name, marks1, marks2, marks3
Make this CSV file before attempting this solution, with at least 8-10 rows of student data as above

We have to build a dictionary using comprehension that should have rollno as key and the average marks as the value.
Note that when you read a file the data would come as strings, so appropriate mathematical conversion may be needed. """

fp = open("stu_details.csv","r")
marks_list = []
avg_list = []
n=-1
for line in fp:
    marks_list.append((line.rstrip().split(",")[2:]))
    avg_list.append(marks_list[n+1][0]+marks_list[n+1][1]+marks_list[n+1][2])
    n+=1
print(avg_list)
