NUMBER_OF_DISKS = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def move(n, source, auxiliary, target):
    # displaying starting configuration
    print(rods)
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            print(f'Move {i + 1} allowed between {source} and {target}')
            forward = False
            if not rods[target]:
                forward = True
            elif rods[source] and rods[source][-1] < rods[target][-1]:
                forward = True
            if forward == True:
                print(f'Moving disk {rods[source][-1]} from {source} to {target}')
                rods[target].append(rods[source].pop())
            else:
                print(f'Moving disk {rods[target][-1]} from {target} to {source}')
                rods[source],append(rods[target].pop())
        elif remainder == 2:
            print(f'Move {i + 1} allowed between {source} and {auxiliary}')
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')


# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')
