# Write a code that the reverses the order of the items means in opposite order.

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# l= len(places)
# i=1
# while i<=l:
#     rev= places[-i]
#     i=i+1
#     print(rev)


# word= "pinke is a good girl"
# l=len(word)
# i=1
# while i<=l:
#     split=word[-i]
#     i=i+1
#     print(rev)

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
count=0
count1=0
count2=0
count3=0
count4=0
count5=0
while i<len(char_list):
    if char_list[i]=="a":
        count=count+1
    elif char_list[i]=="n":
        count1=count1+1
    elif char_list[i]=="t":
        count2=count2+1
    elif char_list[i]=="x":
        count3=count3+1
    elif char_list[i]=="u`":
        count4=count4+1
    elif char_list[i]=="g":
        count5=count5+1
    i=i+1

print(count)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)



# a=["mom","dad","non","savita","memane","pooja"]
# i=0
# count=0
# while i<len(a[i]):
#     b=a[i]
#     if b[0:]==b[::1]:
#         print(count)
#     count=count+1
#     i=i+1


    















