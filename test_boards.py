"""Test boards for Connect383

Place test boards in this module to help test your code.  Note that since connect383.GameState
stores board contents as a 0-based list of lists, these boards are reversed to they can be written
right side up here.

"""

boards = {}  # dictionary with label, test board key-value pairs

boards['test_1'] = reversed([  
    [  0,  0 ],                       
    [  1, -1 ],
    [  1, -1 ] 
])

boards['test_2'] = reversed([  
    [ -1,   0,  0, -1, -1 ],  
    [ -1,   1, -1,  1,  1 ],
    [  1,  -1,  1, -1,  1 ],
    [  1,   1, -1,  1, -1 ] 
])

boards['writeup_1'] = reversed([
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0, -1,  0,  0,  0 ],
    [  0,  0,  0,  1,  0,  0,  0 ],
    [  0,  1,  0, -1,  0,  1,  0 ]
])

boards['writeup_2'] = reversed([  
    [ -1,  1, -1, -1 ],                       
    [  1, -1,  1, -1 ],
    [  1, -2, -1,  1 ],
    [  1, -2,  1, -1 ] 
])
#test if it immediately goes to block or finds more optimal move
boards['your_test'] = reversed([
    [0, 0,0,0],
    [-1,0,-1,-1],
    [1,0,1,1]
])
boards['your_test2'] = reversed([
    [1, 0,0,-1],
    [-1,0,0,1],
    [-1,1,-1,-1]
])

boards['tie'] = reversed([
    [1,1,0,-1],
    [1,-1,0,-1],
    [1,1,0,-1]
])

boards['test_11'] = reversed([
    [0,0,0,0,0],
    [0,0,0,0,1],
    [-1,1,-1,1,-1]
])
# put something here!
# Player 2 wins! 9 - 16
# Player 1 generated 2370001 states
# Player 2 generated 585826 states
# Player 2 wins! 9 - 16
# Player 1 generated 113439 states
# Player 2 generated 44518 states

