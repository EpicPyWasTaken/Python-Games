import random,logging,datetime

number = random.randint(1,50);guess_total = 5;guess_left = 5;run = False
#print(number)

def main():
    logging.basicConfig(filename='./Logs/number_guesser.log',level=logging.DEBUG)
    logging.debug(f'Starting game at {datetime.datetime.now()}')
    global guess_left,number,run
    while run:
        Vcontinue = True
        if guess_left == 0:
            output = f'Alas!You ran out of guesses and the number was {number}.You have 0 guesses left.'
            Vcontinue = False
            run = False
        
        if Vcontinue:
            user_input = int(input('Enter your number:'))
            output = ''
            logging.debug(f'Number:{number},User Input:{user_input},Attempts Left:{guess_left}')

            if user_input == number:
                output = f'Wow you choose the correct number! You had {guess_left} guess(es) left.'
                run = False

            elif user_input > number:
                if guess_left != 1:
                    output = f'Alas!The number is less.You have {guess_left - 1} guess(es) left.'

            elif user_input < number:
                if guess_left != 1:
                    output = f'Alas!The number is higher.You have {guess_left - 1} guess(es) left.'
            user_input = ''

        print(output)
        if run or Vcontinue:
            guess_left -= 1
    logging.debug(f'Ending at {datetime.datetime.now()}')

if __name__ == '__main__':
    #if guess_left == guess_total:
    try:
        run = True
        main()
    except:
        print('Something went wrong!Try again')