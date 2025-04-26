#find the minimum with recursion
# Start the algo
# Get the array, position and minivalue
#basecase: terminate function if  the position is greater than or qqual lenght of the array

def recFindMin(arr, position, minVal):
    if position >= len(arr):
        return arr.index(minVal)
    currentMin = arr[position]
    if currentMin < minVal:
        return recFindMin(arr, position + 1, currentMin)
    else:
        return recFindMin(arr, position + 1, minVal)


def findMin(arr):
    minVal = arr[0]
    return recFindMin(arr, 0, minVal)

arr = [20, 10, 15, 25, 8, 12]

print(findMin(arr))