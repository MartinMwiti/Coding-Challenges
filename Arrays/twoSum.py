# [QUESTION] Given an array of integers, return the indices of the two numbers that add up to a given target.


# Edge cases
# [] -- Empty array
# [*] -- Single element in an array
#  expected inputs - array, -target
# expected output -- indices

# expect an int for both arr and target inputs
class Solution:
    def findTwoSum(self, arr: int, target: int):
        # edge cases
        # if (len(arr) < 2):
        #     return 'undefined'

        for i in range(len(arr)):
            lookUpValue = target - arr[i]
            # print("lookup", lookUpValue)
            for j in range(i+1, len(arr)):
                if arr[j] == lookUpValue:
                    return [i, j]

        return "Not Found"


# Optimize(recursion) -- METHOD 2
class Solution:
    def findTwoSum(self, arr: int, target: int, x=0):
        if len(arr) == 0:
            return None
        for i in range(len(arr) - 1):
            if (arr[x] + arr[i+1] == target) and x != i+1:
                return [x, i+1]
        return self.findTwoSum(arr, target, x+1)


# Optimize(hash map) -- METHOD 3
class Solution:
    def findTwoSum(self, arr: int, target: int):
        mylist = {}
        for i in range(len(arr)):
            if arr[i] in mylist.keys():
                return [arr.index(target-arr[i]), i]

            mylist.update({target-arr[i]: i})

        return "Not Found"


arr = [1, 3, 1, 9, 2]  # [3, 4]
target = 11
func = Solution()
result = func.findTwoSum(arr, target)
print(result)
