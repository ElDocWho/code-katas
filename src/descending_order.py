"""Descending order - Return a number from highest digit in decending order to lowest

#1 Best Practices Solution by laoris, jolaf, hiasen, GrimR3, Bitman, rjip (plus 878 more warriors)

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
"""

def Descending_Order(num):
    num = str(num)
    num = list(num)
    num.sort(reverse=True)
    num = ''.join(num)
    num = int(num)
    
    return num