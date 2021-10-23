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
        This function takes no inputs but returns True or False if a given answer
        (which is taken from the user in a prompt) matches the product of two values

        Returns: Boolean
        '''
        # Generate two random values
        val1 = randint(0, 10)
        val2 = randint(0, 10)
        # Create the answer
        answer = val1 * val2

        # Prompt user for their answer
        print(f'{self.elapsed.seconds//60} Minutes and {self.elapsed.seconds%60} Seconds')
        print(f'{val1} x {val2}')
        userAnswer = input('>> ')

        # If user's answer correct, return True, else return False
        return str(answer) == userAnswer
