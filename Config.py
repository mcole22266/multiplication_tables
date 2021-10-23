# Config.py
# Michael Cole (mcole042891@gmail.com)
#
# This stores the project settings to be used across the entire project
# =====================================================================


class Config:

    def __init__(self):
        '''
        Initialize the Config Object with Attributes/Settings
        '''
        self.logging = False  # Set True to print Logs for testing
        self.timer_minutes = 30  # Number of minutes until program ends

        # Values to be used in multiplication. "randint" will choose any
        #   random integer between "_low" and "_high" for each value
        #       val1
        self.val1_low = 0
        self.val1_high = 10
        #       val2
        self.val2_low = 0
        self.val2_high = 10
