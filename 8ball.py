import numpy as np
import sys
import time


def intro():
    print('')
    print('##############################')
    print('#        Magic 8 Ball        #')
    print('#          for Mike          #')
    print('##############################')
    print('')

def ballresponse():
    fortunes_list = ['It is certain',
                    'It is decidedly so',
                    'Without a doubt',
                    'Yes, definitely',
                    'You may rely on it',
                    'As I see it, yes',
                    'Most likely',
                    'Outlook good',
                    'Yes',
                    'Signs point to yes',
                    'Reply hazy try again',
                    'Ask again later',
                    'Better not tell you now',
                    'Cannot predict now',
                    'Concentrate and ask again',
                    'Don\'t count on it',
                    'My reply is no',
                    'My sources say no',
                    'Outlook not so good',
                    'Very doubtful']
    list_indices = len(fortunes_list)
    fortune_index = np.random.randint(0, list_indices)
    thinking()
    print('\n' + '\n' + 'The Elders of the Internet have replied!')
    print('Elders:  "{}"').format(fortunes_list[fortune_index])

def askquestion():
    print('\n' + 'Hello. Please ask your question aloud in a solemn tone. ')
    ready = raw_input('When ready to seek the wisdom of the internet, ' \
                      'press return.')

def again():
    print('\n' + 'Would you like to invoke the wisdom of the internet again?')
    answer = raw_input('(y or n):  ').lower()
    if answer in ['y', 'yes']:
        return True
    else:
        return False

def thinking():
    sleep = 1
    sleepfast = 0.25
    print('\n' + 'Opening connection with The Elders of the Internet.')
    time.sleep(sleep)
    print('Connection successful.')
    phrase = 'Submitting question'
    sys.stdout.write(phrase)
    for i in range(11):
        sys.stdout.write('\r')
        #sys.stdout.write('Submitting question[%-10s] %d%% ' % ('='*i, 10*i))
        sys.stdout.write('Submitting question[{:<10}]' \
                         '{:.0f}% '.format('=' * i, 10 * i))
        sys.stdout.flush()
        time.sleep(sleepfast)
    sys.stdout.write('Complete.')

def ballmain():
    intro()
    repeat = True
    while repeat == True:
        askquestion()
        ballresponse()
        repeat = again()
    print('\n' + 'See you later!' + '\n')

ballmain()
