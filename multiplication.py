# multiplication.py
# Michael Cole (mcole042891@gmail.com)
#
# Generates multiplication question, presents it, and says if right or not
# ======================================================================== 

from models.Prompt import Prompt


def main():
    '''
    Run the program logic
    '''
    prompt = Prompt()

    # Ask questions until time is complete
    while not prompt.timeIsUp():
        response = prompt.presentQuestion()
        print(response)
        print('===================')

if __name__ == '__main__':
    # Run the program
    main()
