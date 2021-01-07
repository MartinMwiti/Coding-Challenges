# [QUESTION] Given an array of integers, return the indices of the two numbers that add up to a given target.


# Edge cases
# [] -- Empty array
# [*] -- Single element in an array
#  expected inputs - array, -target
# expected output -- indices

def sum(arr, target):
    # edge cases
    if (len(arr) < 2):
        return 'undefined'
    
    for i in range(len(arr)-1):
        lookUpValue = target - arr[i]
        # print("lookup", lookUpValue)
        for j in range(i+1, len(arr)):
            if arr[j] == lookUpValue:    
                return list((i,j))
            else:
                j +=1

        i +=1
    
    return "Not Found"


arr = [1, 3, 5, 9, 2]
target = 11
result = sum(arr, target)
print(result)
