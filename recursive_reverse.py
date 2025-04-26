#Reverse a string recusivesly
#base case : when the postion is same sa the araay length
def recursiveRev(message, postion):
    if postion >= len(message):
        return ""
    return str(recursiveRev(message, postion + 1)) + str(message[postion])
   
    
def reverse(message):
    return recursiveRev(message, 0)

print(reverse("boom"))
