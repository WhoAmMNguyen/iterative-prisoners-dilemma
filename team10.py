####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E10'
strategy_name = 'Beating your code'
strategy_description = 'Always win.'
import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    First three rounds random choice
    Analyze last three rounds and make choice
    '''
    
    #First three rounds
    if len(my_history) < 3:
        choice = random.randint(0,1)
        if choice == 0:
            return 'b'
        if choice == 1:
            return 'c'
    if len(my_history) % 7 == 0:
        if my_score <= their_score:
            return 'b'
        else:
            return 'c'
    else:
        if my_score == their_score:
            return 'b'
        if their_history[-7:] == 'bbbbbbb' and my_history[-7:] == 'bbbbbbb':
            return 'c'
        if my_history[-3:] == 'bcb' and their_history[-3:] == 'cbc':
                    return 'b'
        if their_history[-7:] == 'ccccccc' and my_history[-7:] == 'ccccccc':
            return 'b'
            
        choice = random.randint(0,1)
        if choice == 0:
            return 'b'
        if choice == 1:
            return 'c'
    
