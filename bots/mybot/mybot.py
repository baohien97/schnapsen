"""
This bot serves as the foundation for other bots in the project. It implements the MINMAX strategy and defines basic
variables for possible features.
"""
#!/usr/bin/env python

from api import State, util
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
        elif state.get_stock_size() is 2:           # round 5
            move = self.minmax(state)
        else:                                       # last 5 rounds (phase 2)
            val, move = self.value(state)           # simple MinMax strategy (add alpha-beta pruning)
        return move

    def minmax(self, state):

        if state.get_opponents_played_card() is not None:
        # opponent leads round 5
            val, move = self.MEU_follow(state, 2)
            return move

        # player leads round 5
        move = self.MEU_lead(state)
        return move

    def MEU_lead(self, state):
        moves = state.moves()
        utilities = [] # estimated utilities of each move
        for m in moves:
            m_values = []
            #if possible do Trump-Jack exchange
            if m[0] is None:
                return m
            for index in range(6):
                a_state = simulate_state(state, index, 2)
                a_value, _ = self.MEU_follow(a_state.next(m), 1)
                m_values.append(a_value)
            utilities.append(m_values)
        move = moves[np.argmax(utilities)]
        return move

    def MEU_follow(self, state, opponent):
        # returns the move with highest estimated utility
        # opponent: 1 or 2: if 1, opponent is player 1
        if opponent == 2:
            moves = state.moves()
        else:
            moves = opponent_moves(state)
        utilities = [] #array containing utilities of moves
        deck = state.get_deck()
        unknowns = 5
        for m in moves:  #iterate over all possible moves
            m_values = [] # array containing utilities of all possible states
            for key in range(unknowns): #iterate over all possible/simulated states
                a_state = simulate_state(state, key, opponent)
                value, _ = self.value(a_state.next(m))
                m_values.append(value)
            avg_values = sum(m_values) / float(len(m_values))
            utilities.append(avg_values)
        if opponent == 2:
            a_value, a_move = max(utilities), moves[np.argmax(utilities)]
        else:
            a_value, a_move = min(utilities), moves[np.argmin(utilities)]
        return a_value, a_move

    def value(self, state, alpha=float('-inf'), beta=float('inf')):
        """
        Return the value of this state and the associated move
        :param State state:
        :param float alpha: The highest score that the maximizing player can guarantee given current knowledge
        :param float beta: The lowest score that the minimizing player can guarantee given current knowledge
        :param int depth: How deep we are in the tree
        :return val, move: the value of the state, and the best move.
        """

        if state.finished():
            winner, points = state.winner()
            return (points, None) if winner == 1 else (-points, None)

        best_value = float('-inf') if maximizing(state) else float('inf')
        best_move = None

        moves = state.moves()

        if self.__randomize:
            random.shuffle(moves)

        for move in moves:

            next_state = state.next(move)
            value, _ = self.value(next_state)

            if maximizing(state):
                if value > best_value:
                    best_value = value
                    best_move = move
                    alpha = best_value
            else:
                if value < best_value:
                    best_value = value
                    best_move = move
                    beta = best_value

            # Prune the search tree
            # We know this state will never be chosen, so we stop evaluating its children
            if beta <= alpha:
                break

        return best_value, best_move


def simulate_state(state, key, opponent):
    # creates an imaginary/ simulated state based on unknown cards of opponent
    a_state = state.clone(signature=None) #eventually set signature to None
    played_card = state.get_played_card()[opponent-1]
    string_opponent = "P" + str(opponent) + "H"

    #card_states = a_state.get_card_states()
    # 1 unknown card is set to be upper/hidden card in simulated stock,
    # remaining cards are set to be opponent's cards
    for index in range(20):
        if index == state.get_trump_card_index():  # don't change the open trump-card in stock
            pass
        elif index == played_card:
            pass
        else:
            if state.get_perspective(1 if opponent == 2 else 2)[index] is "U":
                if key is not 0:
                    a_state.set_card(index, string_opponent)
                    a_state.change_knowledge(opponent, index, string_opponent)
                else:
                    a_state.change_stock(index, 1)
                    a_state.set_card(index, "S")
                    a_state.change_knowledge(opponent, index, "U")
                key -= 1
    return a_state

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

def opponent_moves(state):
    hand = state.hand()
    moves = []
    for card in hand:
        moves.append((card, None))
    return moves




