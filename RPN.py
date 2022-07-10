#User Input
Input = input("Enter Your RPN Calculation: ").split(" ")

#Error Checking
Operators = ["+", "-", "/", "*"]

if len(Input) < 3:
    result = "Error Please enter at least two numbers and an operator. For Example  '10 20 +'"
elif len(Input) > 6:
    result = "Error Maximum calculation Number Number Operator Number Number Operator. For Example 10 20 * 5 2 *"


if len(Input) >= 3:
    if not Input[0].isdigit() or not Input[1].isdigit() or not Input[2] in Operators:
        result = "Error Please enter the calculation in the format: Number Number Operator... For Example 10 20 +..."
        Input = []

if len(Input)  == 5:
    if not Input[3].isdigit() or not Input[4] in Operators:
        result = "Error Please enter the calculation in the format: Number Number Operator Number Operator. For Example 10 20 + 2 -"
        Input = []

if len(Input) == 6:
    if not Input[3].isdigit() or not Input[4].isdigit() or not Input[5] in Operators:
        result = "Error Please enter the calculation in the format: Number Number Operator Number Number Operator. For Example 10 20 * 5 2 *"
        Input = []

#Two Number Calculator
def Calculate(firstNum, secondNum, operator):
    if operator == "+":
        result = int(firstNum) + int(secondNum)

    elif operator == "-":
        result = int(firstNum) - int(secondNum)

    elif operator == "*":
        result = int(firstNum) * int(secondNum)

    elif operator == "/":
        result = int(firstNum) / int(secondNum)

    elif operator == "%":
        result = int(firstNum) % int(secondNum)
        
    else: 
        result = "Error Operator Not in Parameters(+ - * /)"

    result = str(result)

    return result

#Check length of calcuations
if len(Input) == 3:
    result = Calculate(Input[0], Input[1], Input[2])
elif len(Input) == 5:
    result = Calculate(Calculate(Input[0], Input[1], Input[2]), Input[3], Input[4])
elif len(Input) == 6:
    result = str(int(Calculate(Input[0], Input[1], Input[2])) + int(Calculate(Input[3], Input[4], Input[5])))

#Output
print("Result: " + result)