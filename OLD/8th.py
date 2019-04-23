'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

if __name__ == '__main__':
    input_list = [item for item in input('\nEnter a list of words ["," seperated]:\t').split(',')]
    print('\nOriginal Input, before Sorting:\t',','.join(input_list))
    input_list.sort()
    print('\nAfter Sorting, Final output:\t',','.join(input_list))