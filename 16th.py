'''
Question:
Use a list comprehension to [square]?? each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
[1,3,5,7,9]?? # This should be [1,9,25,49,81]
'''

if __name__ == '__main__':
    user_input_list = [int(x) for x in input('\nEnter list of numbers [seperated by ","]:\t').split(',')]
    final_output_list = []
    for x in user_input_list:
        if x % 2 != 0:
            final_output_list.append(x*x)
    print(final_output_list)