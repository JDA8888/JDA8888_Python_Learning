# Arithmetic Formatter project. 


def arithmetic_arranger(problems, show_answers=True):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line_problem = []
    second_line_problem = []
    dash_line = []
    answer_line = []

    for prob in problems:
        parts = prob.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        left, op, right = parts

        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (left.isdigit() and right.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(left), len(right)) + 2

        first_line_problem.append(left.rjust(width))
        second_line_problem.append(op + right.rjust(width - 1))
        dash_line.append("-" * width)

        if show_answers:
            if op == '+':
                answer = str(int(left) + int(right))
            else:
                answer = str(int(left) - int(right))
            answer_line.append(answer.rjust(width))
    
    arranged = "    ".join(first_line_problem) + "\n" + "    ".join(second_line_problem) + "\n" + "    ".join(dash_line)

    if show_answers:
        arranged += "\n" + "    ".join(answer_line)
    return arranged

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')