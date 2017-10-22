"""Kata: Money, money, money - Return the number of years we need to achieve desired amount

#1 Best Practices Solution by hchokshi, jonathan-j-lee, Cronokirby, Robbentheking, tiffanydu31, curlew77 (plus 3 more warriors)

def calculate_years(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years
"""

def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal = (principal * (1 + interest)) - ((principal * interest) * tax)
        year = year + 1
    return year