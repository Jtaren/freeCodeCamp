def arithmetic_arranger(problems, show_answers=False):
   
# Check the length of the parameter  
    if len(problems) > 5:
        return "Error: Too many problems."
    
# Check the operand
    operators = []
    for problem in problems:
        array = problem.split() 
        operators.append(array[1])

    for operator in operators:
        if operator in ['*', '/']:
            return "Error: Operator must be '+' or '-'."

# Check for non-digits
    numbers = []
    for problem in problems:
        array = problem.split()
        numbers.append(array[0])
        numbers.append(array[2])

    for number in numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."
# Check operand length
        elif len(number) > 4:
            return "Error: Numbers cannot be more than four digits."
    
    return problems
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')