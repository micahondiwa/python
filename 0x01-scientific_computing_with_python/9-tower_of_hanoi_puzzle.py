'''9-tower_of_hanoi_puzzle.py module'''

NUMBER_OF_DISKS  = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A':[list(range(NUMBER_OF_DISKS, 0, -1))],
    'B':[],
    'C':[]
}

def move(n, source, auxiliary, target):
    
    # display starting configuration
    print(rods)
    for i in range(number_of_moves):
        print(i)

# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')