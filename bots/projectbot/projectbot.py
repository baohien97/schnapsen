"""
This bot serves as the foundation for other bots in the project. It implements the MINMAX strategy and defines basic
variables for possible features.
"""
#!/usr/bin/env python

from api import State, util, Deck
import random
import numpy as np

class Bot:

    __randomize = True

    def __init__(self, randomize=True):
        """
        :param randomize: Whether to select randomly from moves of equal value (or to select the first always)
        :param depth: how deep we are in the tree
        """
        self.__randomize = randomize

    def get_move(self, state):
        # type: (State) -> tuple[int, int]

        if state.get_stock_size() > 2:              # round 1 through 4
            move = random.choice(state.moves())     # place-holder strategy
        elif state.get_stock_size() in [2,1]:       # round 5
            move = self.max_estimated_utility(state)
        else:                                       # last 5 rounds (phase 2)
            val, move = self.value(state)           # simple minmax strategy (add alpha-beta pruning)
        return move

    def max_estimated_utility(self, state):
        # returns the move with highest estimated utility
        moves = state.moves()
        utilities = []
        for m in moves:
            if m[0] == None: #Trump-Jack exchange
                return m
            values, ms = self.simulated_minmax(state.next(m))
            avg_values = sum(values) / float(len(values))
            utilities.append(avg_values)
        move = moves[np.argmax(utilities)]
        return move

    def simulated_minmax(self, state):
        # returns two of lists a_values
        deck = state.__deck
        unknown_cards = len(deck.get_player_hand(2)) + 1
        a_values = [] # list with best moves and values for each possible state
        a_moves = [] # list of best moves according to possible state
        for i in range(unknown_cards):
            key = i
            #create simulated state with one of the possible distributions of unknown cards on stock and opponents hand
            a_state = deck.clone(signature=state.whose_turn())
            card_state = a_state.__card_state
            # ith unknown card is set to be last card in stock, others set to opponents cards
            for card in range(20):
                if card == 0: #don't change the open trump-card in stock
                    pass
                if card_state[card] == "S" or card_state[card] == "P2H": #consider all cards with unknown state
                    card_state[card] = "P2H" if key != 0 else "S"
                    key -= 1
            a_val, a_move = self.value(a_state)
            a_values.append(a_val)
            a_moves.append(a_move)
        return a_values, a_moves

    def value(self, state):
        # type: (State, int) -> tuple[float, tuple[int, int]]
        """
        Return the value of this state and the associated move
        :param state:
        :param depth:
        :return: A tuple containing the value of this state, and the best move for the player currently to move
        """

        if state.finished():
            winner, points = state.winner()
            return (points, None) if winner == 1 else (-points, None)

        #if depth == self.__max_depth:
         #   return heuristic(state)

        moves = state.moves()

        if self.__randomize:
            random.shuffle(moves)

        best_value = float('-inf') if maximizing(state) else float('inf')
        best_move = None

        for move in moves:

            next_state = state.next(move)
            # minimax value of 'next_state'
            value, _ = self.value(next_state)

            if maximizing(state):
                if value > best_value:
                    best_value = value
                    best_move = move
            else:
                if value < best_value:
                    best_value = value
                    best_move = move

        return best_value, best_move




def maximizing(state):
    # type: (State) -> bool
    """
    Whether we're the maximizing player (1) or the minimizing player (2).

    :param state:
    :return:
    """
    return state.whose_turn() == 1

def heuristic(state):
    # type: (State) -> float
    """
    Estimate the value of this state: -1.0 is a certain win for player 2, 1.0 is a certain win for player 1

    :param state:
    :return: A heuristic evaluation for the given state (between -1.0 and 1.0)
    """
    return util.ratio_points(state, 1) * 2.0 - 1.0, None



