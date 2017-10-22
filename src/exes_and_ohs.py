"""Kata: Exes and Ohs - Return True if its the same amount of x and o and false otherwise

#1 Best Practices Solution by jolaf, Beast, Tgc, MMMAAANNN, SquishyStrawberry, Devilart (plus 274 more warriors)

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
"""

def xo(s):
    s = s.lower()
    countx = s.count('x')
    counto = s.count('o')
    if countx == counto:
        return True
    else:
        return False
    