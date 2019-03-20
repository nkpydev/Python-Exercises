'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
def mutiplier_addition_function_from_string(x):
    return int( '%s' % x) + int('%s%s' %(x,x)) + int('%s%s%s' %(x,x,x)) + int('%s%s%s%s' %(x,x,x,x))
     
if __name__ == '__main__':
    user_input_number = input('\nEnter any Number:\t')
    print(mutiplier_addition_function_from_string(user_input_number))