'''
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

if __name__ == '__main__':
    final_result = []
    user_input = [b for b in input('\nEnter binary numbers [seperated by ","]:\t').split(',')]
    for b_no in user_input:
        int_no = int(b_no,2) # base 2
        if int_no % 5 == 0:
            final_result.append(b_no)
    print(','.join(final_result))