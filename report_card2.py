# This is the list of marks of a student for the last three years. You have to calculate the average marks for each year.
# Like, for the above list, the output should be as follows:- 
# Average of 1 year - 84 Average of 2 year - 80 Average of 3 year - 63


marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65, 76],

    [95, 45, 78, 52, 49]

]

index=0
m=0
while index<len(marks):
    j=0
    sum=0
    while j<len(marks[index]):
        sum = sum+ marks[index][j]
        j+=1
    m=m+sum
    index+=1
    print(m)