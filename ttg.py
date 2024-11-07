import string

negation = "~"
conjunction = "."
disjuction = "v"
implies = ">"
equality = "="

argument = "((~A.B)vC)>(D=~F)"

#get variables
variables=[]
for letter in argument:
    if letter in string.ascii_uppercase:
        variables.append(letter)

#get negations
negations = []
for i in range(len(argument)):
    if argument[i] == negation:
        negations.append(argument[i+1])

print("Variables: ",end='')
print(variables)

print("Negations: ",end='')
print(negations)





#make table
'''
+---+---+----+---+---
| A | B | ~A |
+---+---+----+
| T | T |  F |
+---+---+----+
| T | F |
+---+---+---
| F | T |
+---+---+---
| F | F |
+---+---+---

'''