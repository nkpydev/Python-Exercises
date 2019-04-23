'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

if __name__ == '__main__':
    transaction_list = []
    result_dict = {'D':0,'W':0}
    while True:
        user_input = input('\nEnter your Transaction Log:\t')
        if user_input != '':
            transaction_list.append(user_input)
        if not user_input:
            break
    for transaction in transaction_list:
        tmp_list = transaction.split(' ')
        if tmp_list[0] == 'D':
            result_dict['D'] += int(tmp_list[1])
        elif tmp_list[0] == 'W':
            result_dict['W'] += int(tmp_list[1])
    print('\n========================')
    print('\nNet Balance:\t',int(result_dict['D'])-int(result_dict['W']))
    print('\n========================')
    