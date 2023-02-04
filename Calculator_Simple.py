from sympy import *

x = Symbol('x')

def calculator():
    while True:
        expression = input("Enter an expression to calculate (or 'q' to quit): ")
        if expression == 'q':
            break
        try:
            result = eval(expression)
            print("Result:", simplify(result))
        except:
            print("Invalid expression. Please try again.")

if __name__ == '__main__':
    calculator()