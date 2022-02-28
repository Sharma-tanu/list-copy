# Write a code that works for any list, and that tells
# how many odd numbers and how many even numbers are there in a given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

i=0
k=0
n=0
while i<len(elements):
    if elements[i]% 2==0:
        k=k+1
    if elements[i]%2!=0:
        n=n+1
    i=i+1
print("even numbers in elements are:",k)
print("odd number in elements are:",n)
