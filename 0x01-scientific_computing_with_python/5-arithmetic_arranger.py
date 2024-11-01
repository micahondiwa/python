'''5-arithmetic_arranger.py module'''

""" 
Receives a list of strings which are arithmetic problmes,
and returns the problems arranged vertically and side-by-side.
The function should optionally take a second argument. When 
the second argument is set to True, the answers should be 
displayed.
    inputs: 
    problems: A list of strings of arithmetic problems.
    show_answers: Tuple (True or)
"""

def arithmetic_arranger(problems, show_answers=False):
    # Checking if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Variables for storing each line of the arranged problem
    first_operand = ""
    operator_and_second_operand = ""
    underline = ""
    answers= ""

    # Remove white space
    for problem in problems:
        problem = problem.replace(" ", "")

        # Check if operator is supported
        if "+" in problem:
            problem = problem.split("+")
            operator = "+"
        elif "-" in problem:
            problem = problem.split("-")
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Check if operands are digits only
        if not (problem[0].isdigit() and problem[1].isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Check if operands have more than 4 digits
        if len(problem[0]) > 4 or len(problem[1]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Width for formatting
        width = max([len(problem[0]), len(problem[1])]) + 2

        # Calculating answers if show_answers = True
        if show_answers:
            anwer = str(eval(problem[0] + operator + problem[1]))
            answers += anwer.rjust(width) + "    "
        
        # The first three lines 
        first_operand += problem[0].rjust(width) + "    "
        operator_and_second_operand += operator + problem[1].rjust(width - 1) + "    "
        underline += "-" * (width) + "    "
    
    # Removing trailing white spaces
    first_operand = first_operand.rstrip()
    operator_and_second_operand = operator_and_second_operand.rstrip()
    underline = underline.rstrip()

    # Combining the 3 lines
    arranged = "\n".join([first_operand, operator_and_second_operand, underline])

    # Adding answers if show_answers = True
    if show_answers:
        answers = answers.rstrip()
        arranged += "\n" + answers + "\n" + underline
    
    return arranged

# Example implentation
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
