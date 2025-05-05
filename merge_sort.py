#starting from the merge function
# 
import sys

def merge(array, startLeft, endLeft, end):
    sizeLeft = endLeft - startLeft + 1
    sizeRight = end - endLeft
    startRight = endLeft + 1

    # create a new temporary storage
    arrLeft = []
    arrRight = []

    #copy the array into the temporary storage
    for i in range(sizeLeft):
        print(i)
        arrLeft[i] = array[startLeft]
    #arrLeft[sizeLeft] = sys.maxsize

    for i in range(sizeRight):
        print("aa", i)
        #arrRight[i] = array[startRight + i]

    #arrRight[sizeRight] = sys.maxsize
    pass
   

arr = [43, 24, 45, 27, 35, 47, 22, 48]

merge(arr, 0, 3, 7)
  