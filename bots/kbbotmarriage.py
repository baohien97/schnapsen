#!/usr/bin/env python
"""
This is a bot that applies propositional logic reasoning to determine its strategy.
The strategy it uses is determined by what is defined in load.py. Here it is to always
pick a Jack to play whenever this is a legal move.

It loads general information about the game, as well as the definition of a strategy,
from load.py.
"""
import numpy as np
from api import State, Deck, util
import random, load

from kb import KB, Boolean, Integer
from alphabeta import Bot as AlphaBeta


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):

        moves = state.moves()

        random.shuffle(moves)

        for move in moves:
            # '''apply the knowledge base for the first phase of the game.For phase two alpha beta is applied'''

            if state.get_phase() == 1:  # apply knowledge base
                # stock = np.array(Deck.get_stock())  # get card indexes still in stock
                # # alternatively this could be be also estimated with make_estimation()
                # hand = np.array(Deck.get_player_hand(1))
                # # arrays with kings and queens
                # kings = np.array([2, 7, 17, 18])
                # queens = np.array([3, 8, 13, 18])
                # # arrays with kings and queens in hand respectively
                # kings_hand = np.intersect1d(hand, kings)
                # queens_hand = np.intersect1d(hand, queens)
                #
                # # array with cards having matching partners in stock
                # kings_partner = np.intersect1d((kings_hand + 1), stock) - 1
                # queens_partner = np.intersect1d((queens_hand - 1), stock) + 1
                #
                # # stores all cards that should be saved for marriage
                # save_card = np.append(kings_partner, queens_partner)
                #
                # if move[1] in save_card:
                #     pass

                if not self.kb_consistent(state, move):
                    # Plays the first move that makes the kb inconsistent. We do not take
                    # into account that there might be other valid moves according to the strategy.
                    # Uncomment the next line if you want to see that something happens.
                    # print "Strategy Applied"
                    return move
                # If no move that is entailed by the kb is found, play random move
                return random.choice(moves)

            if state.get_phase() == 2:  # apply alphabeta
                alphabeta_bot = AlphaBeta()
                val, move = alphabeta_bot.value(state)
                return move

    # Note: In this example, the state object is not used,
    # but you might want to do it for your own strategy.
    def kb_consistent(self, state, move):
        # type: (State, move) -> bool

        # each time we check for consistency we initialise a new knowledge-base
        kb = KB()

        # Add general information about the game
        load.general_information(kb)

        # Add the necessary knowledge about the strategy
        # if state.__leads_turn:
        #     load.strategy_knowledge(kb)
        #   #  load.strategy_marriages(kb)
        # else:

        load.strategy_marriages(kb)

        # This line stores the index of the card in the deck.
        # If this doesn't make sense, refer to _deck.py for the card index mapping
        index = move[0]

        # This creates the string which is used to make the strategy_variable.
        # Note that as far as kb.py is concerned, two objects created with the same
        # string in the constructor are equivalent, and are seen as the same symbol.
        # Here we use "pj" to indicate that the card with index "index" should be played with the
        # PlayJack heuristics that was defined in class. Initialise a different variable if
        # you want to apply a different strategy (that you will have to define in load.py)
        variable_string = "pj" + str(index)
        strategy_variable = Boolean(variable_string)

        # Add the relevant clause to the loaded knowledge base
        kb.add_clause(~strategy_variable)

        # If the knowledge base is not satisfiable, the strategy variable is
        # entailed (proof by refutation)
        return kb.satisfiable()
