'''
Question
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

def make_capitalized(sentence):
    return sentence.upper()

if __name__ == '__main__':
    lines = []
    while True:
        sentence = input('\nEnter your sentence:\t')
        if sentence:
            lines.append(make_capitalized(sentence))
        else:
            print('Input Taken!!')
            break
    print('\nOutput is as follows:')
    for sentence in lines:
        print(sentence)