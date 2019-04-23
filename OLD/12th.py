'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def if_even_digits(y):
    input_list = str(y)
    return_list = []
    for j in input_list:
        if int(j)%2 == 0: # Check if every digit is divisible by 2
            return_list.append(j)
        if len(return_list) == 4: # If all digits match criteria, the final number should be 4 digits
            return ''.join(return_list)

if __name__ == '__main__':
    data_set = [x for x in range(1000,3001)]
    final_output = []
    for data in data_set:
        tmp_check = if_even_digits(data)
        if tmp_check != None:
            final_output.append(tmp_check)
    print(','.join(final_output))