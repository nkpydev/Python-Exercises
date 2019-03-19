'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class UserInputOutput(object):
    def __init__(self):
        self.user_input = ''
    
    def getUserInput(self):
        self.user_input = input('Enter any string:\t')
    
    def outUserInput(self):
        print(self.user_input.upper())

if __name__ == '__main__':

    keto = UserInputOutput()
    keto.getUserInput()
    keto.outUserInput()
