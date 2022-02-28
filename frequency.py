a=[]
for i in range(5):
    x=input("Enter value")
    a.append(x)
x=input("Enter valueto to count frequency:")
f=a.count(x)
print("frequency of",x,"=",f)