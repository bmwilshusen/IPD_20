import random


team_name = 'Brett W'
strategy_name = 'Modified Tit-for-Tat'
team_name = 'Brett'
strategy_description = '''\
Starts colluding and then transitions for possible forgiveness'''
'''

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
'''

def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
      return 'c'
  else:
    if my_history[-1] == 'c' and their_history[-1] == 'c':
      return 'c'
    if my_history[-1] == 'c' and their_history[-1] == 'b':
      return 'b'
    if my_history[-1] == 'b' and their_history[-1] == 'c':
      return 'b'
    if my_history[-1] == 'b' and their_history[-1] == 'b':
      if random.randint(1,7) == random.randint(1,7):
        return 'c'
      else:
        return 'b'