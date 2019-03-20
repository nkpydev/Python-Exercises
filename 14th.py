'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

def check_character_case(sentence):
    result_dict = {'LOWERCASE':0,'UPPERCASE':0}
    for x in sentence:
        if str(x).islower():                # To get Lowercase
            result_dict['LOWERCASE'] += 1      
        elif str(x).isupper():              # To get Uppercase
            result_dict['UPPERCASE'] += 1
        else:
            pass                            # To ignore Spaces
    return result_dict

if __name__ == '__main__':
    user_input = input('\nEnter any sentence:\t')
    final_output = check_character_case(user_input)
    print('\nLOWERCASE:\t',final_output['LOWERCASE'])
    print('\nUPPERCASE:\t',final_output['UPPERCASE'])