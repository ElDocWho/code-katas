"""Kata: Find the middle element - Return the element with the middle value from the 3 elements in the list

#1 Best Practices Solution by mortonfox, jolaf, Semaphore, alexTayanovsky, daddepledge, pnichols104 (plus 73 more warriors)

def gimme(inputArray):
    # Implement this function
    return inputArray.index(sorted(inputArray)[1])
"""
def gimme(input_array):
    if input_array[0] > input_array[1] and input_array[0] < input_array[2]:
        return 0
    elif input_array[0] < input_array[1] and input_array[0] > input_array[2]:
        return 0
    elif input_array[1] > input_array[0] and input_array[1] < input_array[2]:
        return 1
    elif input_array[1] < input_array[0] and input_array[1] > input_array[2]:
        return 1
    elif input_array[2] > input_array[1] and input_array[2] < input_array[0]:
        return 2
    elif input_array[2] < input_array[1] and input_array[2] > input_array[0]:
        return 2

    