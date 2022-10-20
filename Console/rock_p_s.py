#Imports
import random,logging,datetime
#Others
class Player:
    def __init__(self) -> None:
        pass
    def choose(self,choices)->str:
        return ''

class Computer(Player):
    def __init__(self) -> None:
        pass
    def choose(self,choices):
        return random.choice(choices)

class Game:
    def __init__(self,versus:Player) -> None:
        self.opponent = versus
        self.rounds_left = 3
        self.victory_Li = ['','','']
        self.choices = ['r','p','s']

        self.start()

    def start(self):
        logging.basicConfig(filename='./Logs/R_P_S.log',level=logging.DEBUG)
        logging.debug(f'Starting game at {datetime.datetime.now()}')

        while self.rounds_left != 0:
            computer_C = self.opponent.choose(self.choices)
            user_C = input('Enter your choice(R,P,S):')[0].lower()

            decided = self.decide(user_C,computer_C)
            logging.info('User:{},Computer:{}'.format(user_C,computer_C))

            if decided[0] == True:
                print(decided[1],end='\n\n')
                self.victory_Li[3 - self.rounds_left] = decided[2]
                logging.debug('Round {}-{}'.format(3 - self.rounds_left,decided[1]))
                self.rounds_left -= 1
            else:
                print(decided[1],end='\n\n')
        print('Victory Score:')
        for count in range(len(self.victory_Li)):
            print(' ',end='');print('Round{}.'.format(count+1),end='');print(self.victory_Li[count])

        logging.debug(f'Ending at {datetime.datetime.now()}')


    def decide(self,user_C,computer_C) -> tuple:
        returnTuple = ()
        if user_C == 'r' and computer_C == 'p':
            returnTuple = True,'Computer wins!!💻','Computer💻'
        elif user_C == 'p' and computer_C == 's':
            returnTuple = True,'Computer wins!!💻','Computer💻'
        elif user_C == 's' and computer_C == 'r':
            returnTuple = True,'Computer wins!!💻','Computer💻'
        elif user_C == 'r' and computer_C == 's':
            returnTuple = True,'Player wins!!🧑','Player🧑'
        elif user_C == 'p' and computer_C == 'r':
            returnTuple = True,'Player wins!!🧑','Player🧑'
        elif user_C == 's' and computer_C == 'p':
            returnTuple = True,'Player wins!!🧑','Player🧑'
        elif user_C == computer_C:
            returnTuple = False,'Its a tie!!🎗️'
        return returnTuple

#Main Function
def Main():
    opponent = input('Whom do you want to play with(C for computer):')
    if opponent[0].lower() == 'c':
        Game(Computer())

#Entry Point
if __name__ == '__main__':
    Main()
