# Prompt.py
# Michael Cole (mcole042891@gmail.com)
#
# Prompt Object
# ========================= 

from random import randint
from datetime import datetime, timedelta

from helpers.log import log

class Prompt:

    def __init__(self):
        self.start = datetime.now()
        self.elapsed = self.start - self.start

        self.correct = 0
        self.incorrect = 0

    def timeIsUp(self):
        '''
        Given the Start Time, returns True if the current time has exceeded
        30 minutes

        Returns: Boolean
        '''
        # Get elapsed time since start time
        self.elapsed = datetime.now() - self.start

        # Return True if time exceeds 30 minutes, else False
        return self.elapsed > timedelta(minutes=30)

    def presentQuestion(self):
        '''
        This function takes no inputs but returns T or F if a given answer
        (which is taken from the user in a prompt) matches the product of two values
        Added option to enter "Q" to exit before timer is up.
        
        Returns: String
        '''
        # Generate two random values
        val1 = randint(0, 10)
        val2 = randint(0, 10)

        # Create the answer
        answer = val1 * val2
        
        # Calculates Time Remaining
        timeRemaining = timedelta(minutes = 30) - self.elapsed
        print(f'Time Remaining: {timeRemaining.seconds//60} Minutes and {timeRemaining.seconds%60} Seconds')   
        print(f'{val1} x {val2}')

        # Prompt user for their answer
        userAnswer = input('>> ')
        response = "F"
        if userAnswer.lower() == "q":
            response = 'Q'
        if str(answer) == userAnswer:
            response = "T"

        # If user's answer correct, return T, else return F
        return response

    def accumilateTotalScore(self,userAnswer):
        '''
        This function counts how many you get "Correct" and "Incorrect". 

        Returns: Integer
        '''
        self.userAnswer = "userAnswer"

        if userAnswer == "T":
            self.correct +=1
        else:
            self.incorrect += 1
        
        return (self.correct / (self.correct + self.incorrect)) * 100

    def printStats(self):
        '''
        This function prints total "Correct", "Incorrect","Average", and total questions presented.
        '''
        if self.correct + self.incorrect > 0:                        
            averageScore = (self.correct / (self.correct + self.incorrect) * 100)
        else:averageScore = 0

        print('\n \n \n \n \n \n \n \n')
        print('========================================')
        print(f'Total Math Time: {self.elapsed.seconds//60} Minutes and {self.elapsed.seconds%60} Seconds')   
        print(f'Total Questions Presented: {self.correct + self.incorrect}')
        print(f'Correct: {self.correct}')
        print(f'Incorrect: {self.incorrect}')
        print(f'Average Score: {averageScore}')        