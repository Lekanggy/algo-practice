# Giving a set of sorted input and query, run BS algorithm on the input and query
# a. Start algo by getting input and query
# b. Locate the middle position
# c. Compare query to middle item,
#     If query same as middle , query found,
#     If not , discard from first item to the middle item
#     Decide the direction (left or right)
#  
#      
# d. Repeat b to c until the query is found

def binary_search(arr, query):
    firstIndex = 0
    lastIndex = len(arr) - 1
    mid = len(arr) // 2
  
    while lastIndex >= firstIndex  :
        if(arr[mid] == query):
            return mid
        if(arr[mid] > query):
            lastIndex = mid - 1
            mid = (firstIndex + lastIndex) // 2
        else:
            firstIndex = mid + 1
            mid = (firstIndex + lastIndex) // 2

    return -1


arr = [20, 28, 34, 45, 60, 69, 75, 80, 88]
query = 69
print(binary_search(arr, query))