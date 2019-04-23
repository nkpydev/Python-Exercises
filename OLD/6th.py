'''
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''

import math

def sq_root(d):
    c = 50
    h = 30
    q = []
    for item in d:
        x = math.sqrt((2*c*float(item)/h))
        q.append(str(int(x)))
    return q

if __name__ == '__main__':

    result = []
    d = [x for x in input('\nEnter your no. Sequence ["," seperated]:\t').split(',')]
    result = sq_root(d)
    print('\nSquare Root results are: \t',','.join(result))