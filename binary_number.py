# In this program, if we are given any number in binary form, 
# then we will learn to convert that number in decimal form.xx
# content.


a = [1, 0, 0, 1, 1, 0, 1, 1]

i=1
c=0
sum=0
while i<=len(a):
    b=a[-i]
    sum+=(a[-i]*(2**c))
    c=c+1
    i=i+1
    print(sum)





