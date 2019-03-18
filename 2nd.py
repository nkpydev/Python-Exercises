'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

def get_factorial(x):
    if x == 0:
        return 1
    return x * get_factorial(x-1)



get_input = int(input('Enter no. of which you want Factorial:\t'))

print(get_factorial(get_input))