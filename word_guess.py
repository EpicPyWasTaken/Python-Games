import random
import logging
import datetime

def main(word_C : str,*args,**kwargs):
    word_CC = word_C #Word_C copy
    logging.basicConfig(filename='./Logs/word_guess.log',level=logging.DEBUG)
    logging.debug(f'Starting game at {datetime.datetime.now()}')
    run = args[0]
    word_L = len(word_C)#Length of the word
    word_Li = ['_' for _ in range(word_L)]#Word as a list
    logging.info(f'Word List:{word_Li},Word:{word_C},Length:{word_L}')
    gl = kwargs['GL']
    
    try:
        while run:
            if gl == 0:
                print(f'''Alas!You have 0 guesses left!
The word was {word_CC}
Better luck next time!🕛''')
                run = False;break
            if word_C == '':
                print(f'''Wow!You won with {gl} guesses left
The word was {word_CC}''')
                run = False;break
            user_input = input('Enter a letter:').lower()[0]

            if user_input in word_C:
                index = 0
                TEMP_COUNT = word_C.count(user_input)
                for _ in range(word_C.count(user_input)):
                    TEMP = word_CC.find(user_input,index,word_L)
                    word_C = word_C.replace(user_input,'')
                    word_Li[TEMP] = user_input
                    index = TEMP+1
                    logging.debug(f'Found {user_input} in {TEMP}')
                    del TEMP
            else:
                gl -= 1

            print(' '.join(word_Li))
            print(f'You have {gl} guesses left!')
    except Exception as e:
        logging.error(e)
    logging.debug(f'Ending at {datetime.datetime.now()}')

if __name__ == '__main__':
    #CONSTANT
    run = True
    guesses_left = 5
    #MAIN
    with open('./Others/words.txt','r') as word_file:
        words_NS = word_file.read()#Words not seperated
        words_S = words_NS.split(',')#Words seperated
    
    word_C = random.choice(words_S)#Word choose
    main(word_C.lower().replace(' ',''),run,'console',GL = guesses_left)