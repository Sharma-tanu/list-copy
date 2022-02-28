# b=["ram",10,"shyam",12.5]
# print(b[-2])

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# for i in (numbers):
#     count+=1
# print(count)

# a=["Amisha",12,"Vipine",12.7]
# print(a[:3])

# a=[]
# for i in range(5):
#     x=input("Enter value")
#     a.append(x)
# x=input("Enter valueto to count frequency:")
# f=a.count(x)
# print("frequency of",x,"=",f)

# a=[10,20,-56,21.5]

# n=len(a)
# i=0
# while i<n:
#     print (a[i])
#     i=i+1

# a=[1,2,5,8,9]
# count=0
# for i in a:
#     count+=1
# print(count)

# Name["Rhutuja","Shitu","Veda","Minu"]
# i=0
# length=len(name)
# while i < len(name):
    # print(name[i],":",length)
    # i=i+1
 

# list=[4,5,8,-3,9,-1,6]
# i=0
# a=[]
# while i < len(list):
#     if list[i] < 0:
#         a.append(0)
#     else:
#         a.append(list[i])
#     i=i+1
# print(a)

# [1,2,3,4,5,6,7,8,9,10]
# i=1
# a=[]
# while (i<=10):
#     j=i
#     a.append(j)
#     i=i+1
# print(a)

# a=[1,2,3,4,5,6]
# i=0
# sum=0
# while(i<len(a)):
#     sum=sum+a[i]
#     i=i+1
# print(sum)


# [1,2,3,4,5]
# i=1
# while i<=5:
    # print(i,end=" ")
    # i=i+1



# a=[]
# size=int(input("Enter size of the list:"))
# for i in range(size):
#     val=int(input("Enter number:"))
#     a.append(val)
# a.sort()
# print("Max number=",a[0])
# # print("Second Max number=",a[1])

   
# places=["delhi","gujrat","punjab","kerala","raja"]
# print(places[0])

# Write a Code that finds second maximum element from the list and print

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers.sort()
# print(numbers[-2])

# Write a code, that counts the numbers between 20 and 40 and then print its count.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# l=len(numbers)
# i=1
# k=0
# while i<l:
#     c=numbers[i]
#     if c<40 and c>20:
#      k=k+1
#     i=i+1
# print(k)


# Write a code that the reverses the order of the items means in opposite order.

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# l= len(places)
# i=1
# while i<=l:
    # rev= places[-i]
    # i=i+1
    # print(rev)


# n=int(input("ent"))
# s=0
# i=1
# while i<=n:
#     s=s+i
#     i=i+1
# print(s)

# use the extend () method to add list2 at 
# the end of list1

# list1=['a','b','c']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)

# print all items by referring to their index number..

# list=[0,1,2]
# for i in range(len(list)):
#     print(list[i])


# list1=[10,20,30,40]
# list2=[100,200,300,400]
# i = 0 
# j = 1
# while i < len(list1):
#     print(list1[i], list2[-j])
#     j+=1
#     i+=1


# magic_square = [

#     [8, 3, 4]

#     [1, 5, 9]

#     [6, 7, 2]

# ]
# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         j=int(input("Enter number:"))
#         b.append(j)
#     a.append(b)
# print("matrix is")
# for i in range(3):
#     for j in range(3):
#         print (a[i][j],end=" ")
#     print()
# sumd1=0
# sumd2=0
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             sumd1=sumd1+a[i][j]
#         if i+j==3-1:
#             sumd2=sumd2+a[i][j]
# if sumd1!=sumd2:
#     f=1
# else:
#     for i in range(3):
#         sumr=0
#         sumc=0
#         for j in range(3):
#             sumr=sumr+a[i][j]
#             sumc=sumc+a[j][i]
#         if sumr!=sumd1:
#             f=1
#         elif sumc!=sumd1:
#             f=1
#         else:
#             f=0
# if f==0:
#     print("Matrix is magic square")
# else:
#     print("Matrix is not magic square")


# For the time being you can use the list given below for writing the code.

# name=[ 'n', 'i', 't', 'i', 'n' ]

# name= input("Enter the a text:")
# a= name[::-1]
# if a == name:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# number = input("Enter the a number:")
# a = number[::-1]
# if a == number:
#     print("Palindrome number")
# else:
#     ("Not palindrome number")


# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.

# list = [1,2,3,4,5,6]
# list1 = [2,3,1,0,6,7]
# list2 = []
# for i in range (len(list)):
#     if list[i] not in list1:
#         list2.append(list[i])
#         print(list[i])


# This is the list of marks of a student for the last three years.
# You have to calculate the average marks for each year.
# Like, for the above list, the output should be as follows:-
# Average of 1 year - 84 Average of 2 year - 80 Average of 3 year - 63

# marks = [

# [78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78],
# [87, 67, 49, 68, 88]

# ]
# index =0
# sum=0
# while index < len(marks):
#     j=0
#     while j<len(marks[index]):
#         sum=sum+marks[index][j]
#         j=j+1
#     index=index+1
# print(sum)




# Q: How to find all pairs in an array of integers whose 
# sum is equal to the given number?

# number = 30

# n = [10, 11, 12, 13, 14, 17, 18, 19]
# index =0
# v=n[index]
# m=[]
# while index<len(n):
#     b=n[index]
#     if v+b==number:
#         m.append(n)
#     index+=1
# print(m)


# Write a code that works for any list, it shows the two averages as the output.
# One is the average of even numbers and 
# the other is the average of odd numbers from the given list.


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index = 0
# k=0
# j=0
# s=0
# n=0
# while index <len(elements):
#     if elements[index]% 2==0:
#         s=s+ elements[index]
#         k=k+1
#         a=s//k
#     if elements[index]%2!=0:
#         j=j+ elements[index]
#         n =n +1
#         b= j//n
#     index = index +1
# print("Even number in elements are",a)
# print("Odd number in elements are",b)



# Write a code that works for any list, it should give two sums as outputs,
# one is the sum of odd numbers present in 
# the list and the other is the sum of even numbers present in the list.


# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# index =0
# k=0
# j=0
# s=0
# n=0
# while index <len(elements):
#     if elements[index]%2==0:
#         s=s+elements[index]
#         k=k+1
#     if elements[index]%2!=0:
#         j=j+elements[index]
#         n=n+1
#     index=index+1
# print("Even number in elements are:",s)
# print("Odd number in elements are:",j)


# Write a code that works for all lists. 
# It should print the output as the following like for all 
# the odd numbers and all the even numbers and for all the numbers in the given list,
# it should calculate the following :

# count
# sum
# average
# and then print it.

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# Index = 0
# k=0
# j=0
# s=0
# n=0
# while Index < len(elements):
#     if elements[index]%2==0:
#         s=s+elements[Index]
#         k=k+1
#         a=s//k
#     if elements[Index]%2!=0:
#         j=j+elements[Index]
#         n=n+1
#         b=j//n
#     i=i+1
# print("Even number count",k,"sum",s,"averages",a)
# print("Odd number count",n, "sum",j,"averages",b)


# question_list = [ "How many continents are there?",   "What is the capital of India?", "NG mei kaun se course padhaya jaata hai?"
# ]


# options_list = [

    #pehle question ke liye options

#     ["Four", "Nine", "Seven", "Eight"],

#     #second question ke liye options

#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],

#     #third question ke liye options

#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]

# ]


# har ek question ke liye, uski solution key (yeh index nahi hai)

# solution_list = [3, 4, 1]

# i=0
# while i<len(question_list):
#     print(i+1,question_list[i])   
#     j=0
#     while j<=len(options_list):
#         print(j+1,options_list[i][j])
#         j+=1
#     n=int(input("Enter the number"))
#     if n==solution_list[i]:
#         print("ur ans is correct ")
#     else:
#         print("ur ans is wrong game is over!")
#         break
#     i+=1


# list=["Amisha",1,2,3,2.4]
# count=0
# for i in list:
#     count=count+1
# print(count)


# list=[1,2,3,4,5,7,9,2,5,]
# count=0
# for i in list:
#     count=count+1
# print(count)


# len=[2,1,3,4,5,6,"amisha",12.3]
# count=0
# for i in len:
#     count=count+1
# print(count)


# len=["pooja",12,90,23,"Pooja",675,13]
# count=0
# for i in len:
#     count=count+1
#     print(count)


# Write a program that tells how many elements are there in a given list.
# It is similar to len() function, so in order to implement this program we will
# not use len() function but we will try to understand that how did any programmer 
# implemented this len() function.

# list=[50, 40, 23, 70, 56, 12, 5, 10, 7]

# i=1
# count=1
# for i in (numbers):
#     print(count)
#     count=count+1


# count=0
# for i in (list):
#     print(count)
#     count=count+1

# i=1
# count=2
# for i in range(count):
    # print(count)


# list = ["apple", "banana", "cherry"]
# list.remove("apple")
# print(list)




# Suppose, you have marks in a given list. We have written a code below in which we have calculated 
# total marks as the sum of markst this. But this code doesn't runs.
# Debug this code and then submit it.



# marks = [10, 32, 42, 65, 67, 89, 76, 38, 67]
# total = 0
# counter = 0
# while total < len(marks):
#     total = total + marks[counter]
#     print(total)
# counter = counter + 1


# name = ["Savitri", "Phule", "26"]

# Ab hum iss list ko use karke poora naam (full name) print karna chaste hai

# print (name[1]+name[2])
# Code mei dekhiye naam theek se print kyu nahi ho raha



# name = ["Savitri", "Phule", "26"]
# print (name[0]+name[1]+name[2])

# i=0
# while i<=100:
#     num=int(input("Enter the number:"))
#     a=num%100
#     print(a)
#     i=i+1

# n=int(input("Enter the number:"))
# count=0
# i=1
# while (i<=n) :
#     if (n%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print("prime number")
# else:
#     print("not prime number")
