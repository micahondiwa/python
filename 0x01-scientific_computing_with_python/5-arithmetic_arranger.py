problem = ["3801 - 2", "123 + 49"]

# print("3801      123\n-    2    +  49\n------    -----.")

def extract_elements(lists):
    result = []
    for item in lists:
        part1, sep, part2 = item.partition('+' if '+' in item else '-')
        result.append([part1, sep, part2])
    return result
#problem1 = print(extract_elements(problem))


def extracts(problem):
    return problem.partition(('+' if '+' in problem else '-') for problem in problem)

print(extracts(problem))