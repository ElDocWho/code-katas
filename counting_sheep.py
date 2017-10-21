"""Kata: Counting Sheep - Return The number of sheep in the array

#1 Best Practices Solution by jhoffner, mortonfox, zmoses, f331a, misuburlacu, MatthiasLenz (plus 671 more warriors)

bareable = lambda x,y : False if x > 35 or y > 0.5 else True if x < 36 and y < 0.5 else False
"""

def count_sheeps(arrayOfSheeps):
    num_sheep = arrayOfSheeps.count(True)
    return num_sheep

