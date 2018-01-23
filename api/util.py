"""
General utility functions
"""

import math, sys, os
import traceback
import importlib
from api import Deck
import numpy as np

def other(
        player_id # type: int
        ):
    # type: () -> int
    """
    Returns the index of the opposite player to the one given: ie. 1 if the argument is 2 and 2 if the argument is 1.
    :param player:
    :return:
    """
    return 1 if player_id == 2 else 2 # type: int

def get_suit(card_index):
    """
    Returns the suit of a card
    :param card_index:
    :return:
    """
    return Deck.get_suit(card_index)

def get_rank(card_index):
    """
    Returns the rank of a card
    :param card_index:
    :return:
    """
    return Deck.get_rank(card_index)

def get_card_name(card_index):
    # type: () -> int
    """
    Returns the rank and the suit of a card. Maps card indices as stored in memory to actual cards
    :param card_index:
    :return:
    """
    return get_rank(card_index), get_suit(card_index)


def load_player(name, classname='Bot'):
    #
    """
    Accepts a string representing a bot and returns an instance of that bot. If the name is 'random'
    this function will load the file ./bots/random/random.py and instantiate the class "Bot"
    from that file.

    :param name: The name of a bot
    :return: An instantiated Bot
    """
    name = name.lower()
    path = './bots/{}/{}.py'.format(name, name)

    # Load the python file (making it a _module_)
    try:
        module = importlib.import_module('bots.{}.{}'.format(name, name))
    except:
        print('ERROR: Could not load the python file {}, for player with name {}. Are you sure your Bot has the right '
              'filename in the right place? Does your python file have any syntax errors?'.format(path, name))
        traceback.print_exc()
        sys.exit(1)

    # Get a reference to the class
    try:
        cls = getattr(module, classname)
        player = cls() # Instantiate the class
        player.__init__()
    except:
        print('ERROR: Could not load the class "Bot" {} from file {}.'.format(classname, path))
        traceback.print_exc()
        sys.exit()

    return player

def ratio_points(state, player):
	if state.get_points(player) + state.get_points(other(player)) != 0:
		return state.get_points(player) / float((state.get_points(player) + state.get_points(other(player))))
	return 0

def difference_points(state, player):
    return state.get_points(player) - state.get_points(other(player))

"""
def difference_to_win(state, player):
    difference = 66 - float(state.get_points(player))
    #print(difference)
    return difference if difference <= 66 else 0
"""
def ratio_difference_points(state, player):
    return float(difference_points(state,player)/float((state.get_points(player) + state.get_points(other(player)))))

    '''
    return ratio_points(state, player) - ratio_points(state,player)*(difference_points(state,player)/float((state.get_points(player) + state.get_points(other(player)))))
    '''
    '''
    if state.get_points(player) >= state.get_points(other(player)):
        return pow(float(difference_points(state,player)/float(66)), ratio_points(state, player))
    return 0 - pow((0 - float(difference_points(state,player))/float(66)), ratio_points(state, player))
    '''

    '''
    if state.get_points(player) >= state.get_points(other(player)):
        return float(pow(ratio_points(state,player), float(difference_points(state, player)/float(66))))
    return float(pow(ratio_points(state, player), 0 - float(difference_points(state, player)/float(66))) - 1)
    '''

    '''
    if state.get_points(player) >= state.get_points(other(player)):
        return ratio_points(state, player) + ratio_points(state,player)*(difference_points(state,player)/float((state.get_points(player) + state.get_points(other(player)))))
    return ratio_points(state, other(player)) + ratio_points(state, other(player))*(difference_points(state, player)/float((state.get_points(player) + state.get_points(other(player)))))
    '''