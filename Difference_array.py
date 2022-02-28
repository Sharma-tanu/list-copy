# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 
# find which numbers are not present in the second array.

l = [1,2,3,4,5,6]
l1 = [2,3,1,0,6,7]
l2=[]
for i in range(len(l)):
    if l[i] not in l1:
        l2.append(l[i])

print(l2)