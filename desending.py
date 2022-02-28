a=[2,3,5,6,8,1,3]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[i]>a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j=j+1
    i=i+1
print(a)
