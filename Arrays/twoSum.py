# [QUESTION] Given an array of integers, return the indices of the two numbers that add up to a given target.


# Edge cases
# [] -- Empty array
# [*] -- Single element in an array
#  expected inputs - array, -target
# expected output -- indices

def findTwoSum(arr, target):
    # edge cases
    if (len(arr) < 2):
        return 'undefined'
    
    for i in range(len(arr)):
        lookUpValue = target - arr[i]
        # print("lookup", lookUpValue)
        for j in range(i+1, len(arr)):
            if arr[j] == lookUpValue:    
                return [i, j]
    
    return "Not Found"


arr = [1, 3, 9, 5, 2]
target = 11
result = findTwoSum(arr, target)
print(result)
