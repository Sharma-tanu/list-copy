list=[2,54,7,8,9,45,3,56]
j=0
k=[]
c=[]
while j<len(list):
    i=1
    count=0
    while i<=list[j]:
        if list[j]%i==0:
            count+=1
        i+=1
    if count==2:
        k.append(list[j])
    else:
        c.append(list[j])
    j+=1
print("it is prime number:",k)
print("it is not prime number:",c)