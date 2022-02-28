# Write a code that works for any list, it should give two sums as outputs,
# one is the sum of odd numbers present in the list and the other is the
# sum of even numbers present in the list.


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
k=0
j=0
s= 0
n= 0
while i<len(elements):
    if elements[i]%2==0:
        s=s + elements[i]
        k=k+1
    if elements[i]%2!=0:
        j=j+elements
        n=n+1
    i=i+1
print("even number ")