import connect383
import test_boards
# def streaks(lst):
#     """Get the lengths of all the streaks of the same element in a sequence."""
#     rets = []  # list of (element, length) tuples
#     prev = lst[0]
#     curr_len = 1
#     for curr in lst[1:]:
#         if curr == prev:
#             curr_len += 1
#         else:
#             rets.append((prev, curr_len))
#             prev = curr
#             curr_len = 1
#     rets.append((prev, curr_len))
#     return rets
#
# def get_rows(state):
#     """Return a list of rows for the board."""
#     return [[c for c in r] for r in state.board]
#
# def get_cols(state):
#     """Return a list of columns for the board."""
#     return list(zip(*state.board))
#
# def get_diags(state):
#     """Return a list of all the diagonals for the board."""
#     b = [None] * (len(state.board) - 1)
#     grid_forward = [b[i:] + r + b[:i] for i, r in enumerate(state.get_rows())]
#     forwards = [[c for c in r if c is not None] for r in zip(*grid_forward)]
#     grid_back = [b[:i] + r + b[i:] for i, r in enumerate(state.get_rows())]
#     backs = [[c for c in r if c is not None] for r in zip(*grid_back)]
#     return forwards + backs

def gcd(a,b):
    # print(b)
    if a < b:
        return gcd(b, a)
    if a==b:
        return a
    if a%2 == 1 and b%2 == 1:
        return gcd((a - b) /2, b)
    if a%2==0 and b%2==0:
        return gcd(a /2, b /2) *2
    if a%2==1:
        return gcd(a, b / 2)
    return gcd(a /2, b)
    # if a==b:
    #     return c*a
    # if a%2 == 1:
    #     if b%2 == 1:
    #         return gcd((a-b)/2, b,c)
    #     else:
    #         return gcd(a,b/2,c)
    # else:
    #     if b%2 == 1:
    #         return gcd(a/2,b,c)
    #     else:
    #         return 2*gcd(a/2, b/2,c)



if __name__ == "__main__":
    print(gcd(669,9))
    # board = list(test_boards.boards['writeup_2'])
    # state = connect383.GameState(board)
    # p1_score = 0
    # p2_score = 0
    # print(len(state.board[0]) * len(state.board))
    # for r in state.board:
    #     print(r)
    #     for c in r:
    #         print(c)
    # for run in state.get_rows() + state.get_cols() + state.get_diags():
    #     print(connect383.streaks(run))
    #     for elt, length in connect383.streaks(run):
    #         if (elt == 1) and (length >= 2):
    #             p1_score += length ** 2
    #         elif (elt == -1) and (length >= 2):
    #             p2_score += length ** 2
    # for elt, length in streaks(s):
    #     print(length)
    #     if (elt == 1) and (length >= 3):
    #         print(length)
    #     elif (elt == -1) and (length >= 3):
    #         print(length)