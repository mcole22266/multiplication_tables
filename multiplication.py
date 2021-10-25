# multiplication.py
# Michael Cole (mcole042891@gmail.com)
#
# Generates multiplication question, presents it, and says if right or not
# ======================================================================== 
from helpers.log import log
from models.Prompt import Prompt


def main():
    '''
    Run the program logic
    '''
    prompt = Prompt()    

    # Ask questions until time is complete
    while not prompt.timeIsUp():
        response = prompt.presentQuestion()    
        if response == 'Q':
            break
        if response == 'T':
            print("True")
        else:
            print("False")
        log('=======================================')
        currentScore = prompt.accumilateTotalScore(response)
        log(f'Current Average Score: {currentScore}')
    prompt.printStats()

if __name__ == '__main__':
    # Run the program
    main()
