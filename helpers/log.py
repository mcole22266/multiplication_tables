# log.py
# Michael Cole (mcole042891@gmail.com)
#
# Logs stuff
# =====================================

from Config import Config

config = Config()

def log(string):

    if config.logging:
        print(string)
