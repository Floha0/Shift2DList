# Shift the 2D array through all values. Set the first value custom

# Creating a 2D array
two_dimensional_array = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]

# Print func
def Print2DArray(array):
    for row in array:
        for element in row:
            print(element, end=" ")
        print()


print("Before shifting:")
Print2DArray(two_dimensional_array)

print("*" * 5)

def ShiftArray(array, firstValue):
    shiftedArray = [[0] * len(array[0]) for _ in range(len(array))]
    shiftedArray.append([0])

    for rowIndex in range(len(array)):
        for columnIndex in range(len(array[rowIndex])):
            if columnIndex < len(array[rowIndex]) - 1:
                shiftedArray[rowIndex][columnIndex + 1] = array[rowIndex][columnIndex]
            else:
                if rowIndex < len(array):
                    shiftedArray[rowIndex + 1][0] = array[rowIndex][columnIndex]

    shiftedArray[0][0] = firstValue
    return shiftedArray


# Printing the shifted 2D array
print("After shifting:")
Print2DArray(ShiftArray(two_dimensional_array, 1))