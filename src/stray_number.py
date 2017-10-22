"""Find the stray number - Return the stray number in a list
#1 Best Practices Solution by cvillian098, snormandeau, Mr.Child, rlqmal, compupro, jsfung83 (plus 8 more warriors)

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
"""

def stray(arr):
    for x in range(len(arr)):
        count = arr.count(arr[x])
        if count == 1:
            return(arr[x])
            