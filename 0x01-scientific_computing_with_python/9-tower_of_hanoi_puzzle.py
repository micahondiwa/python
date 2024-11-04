'''9-tower_of_hanoi_puzzle.py module'''

NUMBER_OF_DISKS  = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A':[list(range(NUMBER_OF_DISKS, 0, -1))],
    'B':[],
    'C':[]
}

def move(n, source, auxiliary, target):
    print(rods)

move()