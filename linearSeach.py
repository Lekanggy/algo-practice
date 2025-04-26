# Start the algorithm by taking both the array and the query as input
# Create a position variable to 0
# Search the array for the query position:
#     Increment the postion by 1
#     Check if the item is the same as the query 
#         a. if it does return the postion 
#         b. if does not return -1

def locate_data(arr, query):
    position = 0
    for i in arr:
        if i == query:
            return position
        position+=1
    return -1


data = [2, 4, 6, 10, 5, 7,8]
query = 8

print(locate_data(data, query))

