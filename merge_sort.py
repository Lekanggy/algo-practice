#starting from the merge function
# 
import sys

def merge(array, startLeft, endLeft, end):
    sizeLeft = endLeft - startLeft + 1
    sizeRight = end - endLeft
    startRight = endLeft + 1

    # create a new temporary storage for size n
    arrLeft = [None] * (sizeLeft + 1)
    arrRight = [None] * (sizeRight + 1)

    #copy the array into the temporary storage
    for i in range(sizeLeft):
        arrLeft[i] = array[startLeft + i]
    arrLeft[sizeLeft] = sys.maxsize # set the sentinel

    for i in range(sizeRight):
        arrRight[i] = array[startRight + i]
    arrRight[sizeRight] = sys.maxsize

    #Merge the array by taking the smallest first
    indexLeft = 0
    indexRight = 0
    for i in range(startLeft, end + 1):
        if arrLeft[indexLeft] <= arrRight[indexRight]:
            array[i] = arrLeft[indexLeft]
            indexLeft = indexLeft + 1
        else:
            array[i] = arrRight[indexRight]
            indexRight = indexRight + 1
            
    pass

#Develop the merge sort alog
def mergeSort(array, start, end):
    if(start < end):
        endLeft = (start + end) // 2
        mergeSort(array, start, endLeft)
        mergeSort(array, endLeft + 1, end)
        merge(array, start, endLeft, end)

#Develop the user Interface for merge sort
def mergeSortWrapper(array):
    size = len(array)
    mergeSort(array, 0, size - 1)
   

arr = [43, 24, 45, 27, 35, 47, 22, 48]

#merge(arr, 0, 3, 7)
mergeSortWrapper(arr)
print(arr)
  