"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

x = input("Insert your integer: ")
x1 = x+x
x2 = x+x+x

y = int(x)+int(x1)+int(x2)

print (y)
