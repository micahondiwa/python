problem0 = ["3801 - 2", "123 + 49"]
problem1 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

# print("3801      123\n-    2    +  49\n------    -----.")

def extracts(problem):
    return problem.partition(('+' if '+' in problem else '-') for problem in problem)

print(extracts(problem1))