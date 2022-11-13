import random
import math


BOT_NAME = "Kenta"


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def __init__(self, sd=None):
        if sd is None:
            self.st = None
        else:
            random.seed(sd)
            self.st = random.getstate()

    def get_move(self, state):
        if self.st is not None:
            random.setstate(self.st)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state):
        """Determine the minimax utility value of the given state.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the exact minimax utility value of the state
        """
        #
        # Fill this in!
        #
        if state.is_full():
            return state.utility()
        if state.next_player() == 1:
            m = self.maxV(state)
        else:
            m = self.minV(state)
        return m

    def maxV(self, state):
        if state.is_full():
            return state.utility()
        m = -math.inf
        for s in state.successors():
            cur = self.minV(s[1])
            if cur > m:
                m = cur
        return m
    def minV(self, state):
        if state.is_full():
            return state.utility()
        m = math.inf
        for s in state.successors():
            cur = self.maxV(s[1])
            if cur < m:
                m = cur
        return m

class MinimaxHeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

        # if len(state.successors()) == 0:
        #     return state.utility()
        # m = -math.inf
        # for s in state.successors():
        #     cur = self.minV(s[1])
        #     if cur > m:
        #         m = cur
        # return m

    def maxE(self, state, i):
        if state.is_full():
            return state.utility()
        if i == self.depth_limit:
            return self.evaluation(state)
        m = -math.inf
        for s in state.successors():
            cur = self.minE(s[1], i+1)
            if cur > m:
                m = cur
        return m

    def minE(self, state, i):
        if state.is_full():
            return state.utility()
        if i == self.depth_limit:
            return self.evaluation(state)
        m = math.inf
        for s in state.successors():
            cur = self.maxE(s[1], i+1)
            if cur < m:
                m = cur
        return m

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.

        The depth data member (set in the constructor) determines the maximum depth of the game 
        tree that gets explored before estimating the state utilities using the evaluation() 
        function.  If depth is 0, no traversal is performed, and minimax returns the results of 
        a call to evaluation().  If depth is None, the entire game tree is traversed.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        #
        # Fill this in!
        #
        moves = 0
        for r in state.board:
            for c in r:
                if c == 0:
                    moves += 1
        print(moves)
        if self.depth_limit > moves:
            return super().minimax(state)

        if self.depth_limit == 0:
            return self.evaluation(state)

        else:
            if state.next_player() == 1:
                m = self.maxE(state, 0)
            else:
                m = self.minE(state, 0)
            return m

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in constant time for all states!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heuristic estimate of the utility value of the state
        """
        #Based on scores method in connect383, but counts enemy 2 in a rows
        p1_score = 0
        p2_score = 0
        for run in state.get_rows() + state.get_cols():
            #elt is next player, length is length of streak
            for elt, length in streaks(run):
                if (elt == 1) and (length >= 3):
                    p1_score += length ** 2
                # count enemy two in a rows but weight them less than normal streaks
                if (elt == -1) and (length >= 3):
                    if length == 2:
                        p1_score -= 1
                    else:
                        p2_score += length ** 2
        for d in state.get_diags():
            for elt, length in streaks(d):
                if (elt == 1) and (length >= 3):
                    p1_score += length ** 1.5
                # count enemy two in a rows but weight them less than normal streaks
                elif (elt == -1) and (length >= 2):
                    if length == 2:
                        p1_score -= length
                    else:
                        p2_score += length ** 1.5
        return p1_score - p2_score

def streaks(lst):
    """Get the lengths of all the streaks of the same element in a sequence."""
    rets = []  # list of (element, length) tuples
    prev = lst[0]
    curr_len = 1
    for curr in lst[1:]:
        if curr == prev:
            curr_len += 1
        else:
            rets.append((prev, curr_len))
            prev = curr
            curr_len = 1
    rets.append((prev, curr_len))
    return rets
def get_rows(state):
    """Return a list of rows for the board."""
    return [[c for c in r] for r in state.board]

def get_cols(state):
    """Return a list of columns for the board."""
    return list(zip(*state.board))

def get_diags(state):
    """Return a list of all the diagonals for the board."""
    b = [None] * (len(state.board) - 1)
    grid_forward = [b[i:] + r + b[:i] for i, r in enumerate(state.get_rows())]
    forwards = [[c for c in r if c is not None] for r in zip(*grid_forward)]
    grid_back = [b[:i] + r + b[i:] for i, r in enumerate(state.get_rows())]
    backs = [[c for c in r if c is not None] for r in zip(*grid_back)]
    return forwards + backs

class MinimaxPruneAgent(MinimaxAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by MinimaxAgent.minimax(), but the 
        algorithm should do less work.  You can check this by inspecting the value of the class 
        variable GameState.state_count, which keeps track of how many GameState objects have been 
        created over time.  This agent does not use a depth limit like MinimaxHeuristicAgent.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: 
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        #
        # Fill this in!
        #
        if state.is_full():
            return state.utility()
        if state.next_player() == 1:
            m = self.maxAB(state, -math.inf, math.inf)
        else:
            m = self.minAB(state, -math.inf, math.inf)
        return m

    def maxAB(self, state, a, b):
        if state.is_full():
            return state.utility()
        m = -math.inf
        for s in state.successors():
            m = max(m, self.minAB(s[1], a, b))
            if m >= b:
                return m
            a = max(a, m)
        return m
    def minAB(self, state, a, b):
        if state.is_full():
            return state.utility()
        m = math.inf
        for s in state.successors():
            m = min(m, self.maxAB(s[1], a, b))
            if m <= a:
                return m
            b = min(b, m)
        return m

# N.B.: The following class is provided for convenience only; you do not need to implement it!

class OtherMinimaxHeuristicAgent(MinimaxAgent):
    """Alternative heursitic agent used for testing."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state."""
        #
        # Fill this in, if it pleases you.
        #
        return 26  # Change this line, unless you have something better to do.

# Player 2 wins! 9 - 18
# Player 1 generated 10645 states
# Player 2 generated 46391 states

# Player 2 wins! 9 - 18
# Player 1 generated 3031 states
# Player 2 generated 7771 states