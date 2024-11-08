import string
import math

negation = "~"
conjunction = "."
disjuction = "v"
implies = ">"
equality = "="

argument = "A=B"

#get variables
variables=[]
for letter in argument:
    if letter in string.ascii_uppercase:
        variables.append(letter)

n = len(variables)

#Translation from formal language to python
translatedArg = ""
for char in argument:
    if char == "(" or char==")":
        translatedArg += char+" "
    elif char in variables:
        translatedArg += char+" "
    elif char == "~":
        translatedArg += "not "
    elif char == ".":
        translatedArg += "and "
    elif char == "v":
        translatedArg += "or "
    elif char == "=":
        translatedArg += "== "
#HOW TO HANDLE IMPLICATION

#populate matrix with truth combinations
table = []
for row in range(2**n):
    r = []
    for col in range(n):
        print(f"{(row,col)} {row//(2**(n-col-1))%2}")
        if row//(2**(n-col-1))%2 == 0:
            r.append(True)
        else:
            r.append(False)
    table.append(r)
for row in table:
    row.append(None)

#matrix print
def printM(matrix):
    for row in matrix:
        print(row)

printM(table)


"""
EX. 2 variables
T T
T F
F T
F F
"""