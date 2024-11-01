def arithmetic_arranger(problems, show_answers=False):
    # Checking if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Variables for storing each line of the arranged problem
    first_operand = ""
    operator_and_second_operand = ""
    underline = ""
    results = ""

    # Looping through each problem in the problem list
    for problem in problems:
        problem = problem.replace(" ", "")

        if "+" in problem:
            problem = problem.split("+")