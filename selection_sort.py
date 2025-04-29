#Write a selection sort to sort the algo this data [43, 24, 45, 27, 35, 47, 22, 48]
#Approach the problem using an encapsulation techiques

def exchangeItem(arr, indexA, indexB):
    temp = arr[indexA]
    arr[indexA] = arr[indexB]
    arr[indexB] = temp

def findMin(arr, startIndex):
    minVal = arr[startIndex]
    minIndx = startIndex
    for i in range(startIndex + 1, len(arr)):
        print(i)
        if minVal > arr[i]:
            minVal = arr[i]
            minIndx = i
    return minIndx

def selection_sort(arr):
 
    for i in range(len(arr)):
        minIndx = findMin(arr, i)
        exchangeItem(arr, i, minIndx )


arr = [43, 24, 45, 27, 35, 47, 22, 48]
print(findMin(arr, 4))
print(arr)