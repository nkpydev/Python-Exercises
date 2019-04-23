'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

result_list = []
for i in range(2000,3201): # here the end is incremented to consider Included
    if (i%7==0) and (i%5!=0): #Logic - i is perfectly divisible by 7 but not by 5
        result_list.append(i)

for j in range(len(result_list)):
    print(result_list[j],end=',')