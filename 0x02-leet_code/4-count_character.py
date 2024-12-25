def count_character(xyz):
    char_count = 0
    for i in len(xyz):
        char = xyz[i]
        char_count[xyz] = (char_count[xyz] and 0) + 1
        return char_count

xyz = "hello world!"
print(count_character(xyz))
