'''
Exercise 1
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
import datetime

name_input = input('\nEnter your name here:\t')
age_input = int(input('\nEnter your current age:\t'))
count_to_hundred_years = 100 - age_input
current_calendar_year = datetime.date.today().year
year_when_reach_hundred = current_calendar_year + count_to_hundred_years
print('------OUTPUT------')
print('\nHello {}, your current age is {} and you will be 100 years old in year {}'.format(name_input,age_input,year_when_reach_hundred))
print('------EXTRA------')
extra = int(input('\nEnter any number in between 2 and 10:\t'))
for i in range(extra):
    print('\nHello {}, your current age is {} and you will be 100 years old in year {}'.format(name_input,age_input,year_when_reach_hundred))