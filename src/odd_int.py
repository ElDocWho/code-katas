"""Find the odd int - Return the number in a list that is on it an odd number of times
#1 Best Practices Solution by cerealdinner, ynnake, sfr, netpsychosis, VadimPopov, user7514902 (plus 291 more warriors)

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""

def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 == 1:
            return x
