import operator
import sys

# list = ["2", "a", "/"]
newList = []

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv, 
    '%' : operator.mod,
    '^' : operator.xor,
}
        
def polishCalculator():
    result = 0
    
    while len(newList) < 2:
        print(len(newList))
        input_user = input("Entrez votre chiffre: ")

        try:
            elemToFloat = float(input_user)
        except ValueError:
            print(input_user + " is not a number! ")
            sys.exit()
        else:
            newList.append(elemToFloat)
    
    if len(newList) == 2:
        input_user = input("Entrez votre operateur: ")
        if input_user in operators.keys():
            op1 = newList.pop()
            op2 = newList.pop()
            result = operators[input_user](op2, op1)
            newList.append(result) 
            
            print(result)
        

polishCalculator()

"""
OTHER WAY
"""

# def evaluate(expression):
#   # splitting expression at whitespaces
#   expression = expression.split()
#   print(expression)
    
#   # stack
#   stack = []
    
#   # iterating expression
#   for ele in expression:
      
#     # ele is a number
#     if ele not in '/*+-':
#       stack.append(int(ele))
      
#     # ele is an operator
#     else:
#       # getting operands
#       right = stack.pop()
#       left = stack.pop()
        
#       # performing operation according to operator
#       if ele == '+':
#         stack.append(left + right)
          
#       elif ele == '-':
#         stack.append(left - right)
          
#       elif ele == '*':
#         stack.append(left * right)
          
#       elif ele == '/':
#         stack.append(int(left / right))
    
#   # return final answer.
#   return stack.pop()
  
# # input expression
# arr = "10 6 9 3 + -11 * / * 17 + 5 +"
  
# # calling evaluate()
# answer = evaluate(arr)
# # printing final value of the expression
# print(f"Value of given expression'{arr}' = {answer}")
          