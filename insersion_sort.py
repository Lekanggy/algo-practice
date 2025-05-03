def insertion_sort(arr):
    end = len(arr)
    endSorted = 1
    while endSorted < end:
        currentValue = arr[endSorted]
        index = endSorted
        while index > 0 and currentValue < arr[index - 1]:
            arr[index] = arr[index - 1]
            index = index - 1
        arr[index] = currentValue
        endSorted = endSorted + 1


arr = [43, 24, 45, 27, 35, 47, 22, 48]

insertion_sort(arr)

#print(arr)