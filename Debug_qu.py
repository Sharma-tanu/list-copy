# Suppose, you have marks in a given list. We have written a code below in which we have calculated 
# total marks as the sum of markst this. But this code doesn't runs.
# Debug this code and then submit it.



marks = [10, 32, 42, 65, 67, 89, 76, 38, 67]

total_marks = 0
i = 0
counter=0

while i <  len(marks):
    total_marks =(total_marks + marks[counter])
    counter = counter+1
    print(counter)
i=i+1
