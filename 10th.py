'''
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

if __name__ == '__main__':
    final_output = []
    user_input = [word for word in input('\nEnter words [seperated by "space"]:\t').split(' ')]
    for aword in user_input:
        if aword not in final_output:
            final_output.append(aword)
    final_output.sort()
    print(final_output)