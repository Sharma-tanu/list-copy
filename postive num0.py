list=[1,-2,3,-4,5,-6,7,-8]
i=0
a=[]
while i<len(list):
    if list[i]>0:

        a.append(0)
    else:
        a.append(list[i])
    i=i+1
print(a)

