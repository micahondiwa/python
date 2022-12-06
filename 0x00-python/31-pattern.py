def pattern(n):
    for row in range(n-1, -1, -1):
        for col in range(n):
            if row == col:
                print('X', end='')
            else:
                print('0', end='')
        print()
pattern(3)
