# Write a program that tells in the above list that
# many people are there in the above list who are :

# 1 - Crorepati 
# 2 - Lakhpati 
# 3 - Dilwale

# All those who have money more than or equal to 1 crore are known as Crorepati.
# All those who have money money greater than or equal to 1 lakh, those are called Lakhpati. 
# Rest of the people are called Dilwale.

kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]

index=0
Crorepati=0
Lakhpati=0
Dilwale=0
while index<len(kitna_paisa_hai):
    a=kitna_paisa_hai[index]
    if a>=10000000:
        Crorepati+=1
    elif a>=100000 and a<1000000:
        Lakhpati+=1
    else:
        Dilwale+=1
    index+=1
print("crorepati:",Crorepati)
print("lakhpati:",Lakhpati)
print("dilvale:",Dilwale)                    