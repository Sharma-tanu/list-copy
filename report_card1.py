# Through your code the output of the above 
# list should be as follows :

# Average of 1 year - 84
# Average of 2 year - 81
# Average of 3 year - 72





marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65],

    [95, 45, 78]

]

i = 0
sum = 0
while i<(len(marks)):
    j=0
    a=0
    while j<len(marks[i]):
        a=a+marks[i][j]
        j=j+1
    sum=sum+a
    i=i+1
print(sum)



# Through your code the solution of the above nested 
# list should be as follows :

# Average of 1 year - 84
# Average of 2 year - 81
# Average of 3 year - 72
# Average of 4 year - 71






#     [78, 76, 94, 86, 88],

#     [91, 71, 98, 65],

#     [95, 45, 78],

#     [87, 67, 49, 68, 88]

# ]

# i=0
# while i< len(marks):
#     j=0
#     s=0
#     while j<len(marks[i]):
#         s= s+marks[i][j]
#         a=s//len(marks[i])
#         j=j+1
#     i=i+1
#     print(a)

# marks = [

#     [78, 76, 94, 86, 88],

#     [91, 71, 98, 65],

#     [95, 45, 78],

#     [87, 67, 49, 68, 88]
# ]

# i=0
# s=0
# while i< len(marks):
#     j=0
#     a=0
#     while j< len(marks[i]):
#         a=a+ marks[i][j]
#         j=j+1
#     s=s+a
#     i=i+1
#     print(s)