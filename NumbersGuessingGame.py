import random
import os
from threading import Timer

#how many guesses you get A.L
MAX_GUESS = 10

def getSecretNum(NUM_DIGITS):#NUM_DIGITS is how many digits the user wants A.L
    numbers = list(range(10))
    random.shuffle(numbers)#shuffles numbers 0 to 9 as given by the numbers list A.L
    secretNum = ''#initializes secretNum as empty A.L
    for i in range(NUM_DIGITS):#fills up the list according to number of digits, which is inputed by the user A.L
         secretNum += str(numbers[i])
    return secretNum#returns the secert number that is generated A.L
    
def getClues(guess, secretNum):#Function to inform the user of the correctness of their guess C.K
    if guess == secretNum: #User guess equals computer generated number then the user wins and the game concludes C.K
        return 'You got it!'
    clues = []#initalize an empty list C.K
    for i in range(len(guess)):#runs for loop for the amount of digits that the computer generated number has C.K
        if guess[i] == secretNum[i]:#if index value of guess equals index value of computer generated number, then it gives clue Goal A.L
            clues.append('Goal')#adds Goal to the empty list C.K
        elif guess[i] in secretNum:#if index value of guess is inside computer generated number, then it gives clue Assist A.L
            clues.append('Assist')#adds Assist to the empty list C.K
    if len(clues) == 0:#clues list is empty meaning that none of the digits were in the right place or even in the computer generated number A.L
        return 'Ratio'
    clues.sort()#puts the clues in chronological order C.K
    return ' '.join(clues)#adds a blank in between the clues C.K

def isOnlyDigits(num):#function to determine if user guess is a number A.L
    if num == '':#returns false if user guess is empty, thus not a valid guess C.K
        return False
    for i in num:#returns false if there is a non valid value C.K
         if i not in '0 1 2 3 4 5 6 7 8 9'.split():
             return False 
    return True#number is only digits

def exitTimer():#timer function that exits game after certain time A.L
    print ("Time's up")
    os._exit(0)

#printing instructions for the game A.L
print('The clues I give are...')
print('When I say:    That means:')
print(' Ratio        None of the digits is correct.')
print(' Assist          One digit is correct but in the wrong position.')
print(' Goal         One digit is correct and in the right position.')

while True:#runs continously unless there is a break A.L
    print('How many digits would you like to have. 1 to 5')
    #added User gets to choose number of guesses and number of digits up to 5 A.L
    usernumber = int(input())
    
    if 1<=usernumber<=5:#confines accepted digits as values 1 to 5 A.L
        usernumber = usernumber
    else:
        while usernumber not in range(1,5):#will continue to ask user for a valid value until it is provided A.L
            print('Please input valid value')
            usernumber = int(input())#makes the input an integer C.K
    secretNum = getSecretNum(usernumber) #generates a secret number C.K
    
    print('Set timer limit, from 1s to 60s')#ask user for a time limit A.L
    usertimer = float(input())
    if 1<=usertimer<=60:#confines accepted digits A.L
        usertimer = usertimer
    else:
        while usertimer not in range(1,60):#will continue to ask user for a valid value until it is provided A.L
            print('Please input valid value')
            usertimer = float(input())#sets input as user timer A.L

    print('I have thought up a number. You have %s guesses to get it.' %
          (MAX_GUESS))#max guesses the user has is set to 10 A.L
    guessesTaken = 1#intializes guess taken as 1 C.K
    while guessesTaken <= MAX_GUESS:#loop keeps running if guess taken is less than or equal to the max guess available A.L
         guess = ''
         while len(guess) != usernumber or not isOnlyDigits(guess):#keeps asking the user for a valid guess until provided A.L
             print('Guess #%s: ' % (guessesTaken))
             guess = input()#asks a user for a guess C.K
         Timer(usertimer, exitTimer).start() # runs timer function with specified time limit A.L
         print(getClues(guess, secretNum))#takes user guess a puts it into the getClues function which returns and prints a clue A.L
         guessesTaken += 1#adds 1 to the loop and reruns C.K
         
         if guess == secretNum:#if guess is correct close the loop C.K
             break#closes loop C.K
         if guessesTaken > MAX_GUESS:#if guesses exceed the guess limit then you lose C.K
             print('You ran out of guesses. The answer was %s.' %
                  (secretNum))#prints out correct answer A.L
             
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):#if the input isn't yes then stop the program
        break