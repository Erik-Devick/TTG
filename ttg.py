import string

negation = "~"
conjunction = "."
disjuction = "v"
implies = ">"
equality = "="

test = "(A.B)vC"

letters=[]
for letter in test:
    if letter in string.ascii_uppercase:
        letters.append(letter)

print(letters)