# Q: How to find all pairs in an array of
# integers whose sum is equal to the given number?



# number = 30

# n = [10, 11, 12, 13, 14, 17, 18, 19]

# m=[]
# i=0
# while i<len(n):
#     if i==4:
#         break
#     j=0
#     while j< len(n):
#         a=n[i]+n[j]
#         s=[n[i],n[j]]
#         if number==a:
#             m.append(s)
#         j=j+1
#     i=i+1
#     print(m)
    
m=[]
i=0
while i<len(m):
    j=0
    while j<len(m):
        a=m[i]+m[j]
        s=[m[i],m[j]]
        if number==a:
            m.append(s)
        j=j+1
    i=i+1
print(m)