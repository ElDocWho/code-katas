"""Average Scores - Returns an average without using loops
#1 Best Practices Solution by acaccia, RuiCatela, gabbek, iNovice_, ryan_891, codeRenk (plus 214 more warriors)

def average(array):
    return round(sum(array) / len(array))
"""

def average(array):
    return int(round((sum(array))/len(array)))