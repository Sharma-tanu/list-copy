
# Write a code that works for all lists. 
# It should print the output as the following like for all 
# the odd numbers and all the even numbers and for all the numbers in the given list,
# it should calculate the following :

# count
# sum
# average
# and then print it.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
Index = 0
k=0
j=0
s=0
n=0
while Index < len(elements):
    if elements[index]%2==0:
        s=s+elements[Index]
        k=k+1
        a=s//k
    if elements[Index]%2!=0:
        j=j+elements[Index]
        n=n+1
        b=j//n
    i=i+1
print("Even number count",k,"sum",s,"averages",a)
print("Odd number count",n, "sum",j,"averages",b)