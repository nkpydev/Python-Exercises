'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

def check_character_type(sentence):
    result_dict = {'LETTERS':0,'DIGITS':0}
    for x in sentence:
        if str(x).isdigit():                # To get Digits
            result_dict['DIGITS'] += 1      
        elif str(x).isalpha():              # To get Characters
            result_dict['LETTERS'] += 1
        else:
            pass                            # To ignore Spaces
    return result_dict

if __name__ == '__main__':
    user_input = input('\nEnter any sentence:\t')
    final_output = check_character_type(user_input)
    print('\nLETTERS:\t',final_output['LETTERS'])
    print('\nDIGITS:\t',final_output['DIGITS'])