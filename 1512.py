# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

def numIdenticalPairs(nums):
    result = []

    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if (i < j and nums[i] == nums[j]):
                result.append((i, j))

    return result


list = [1, 2, 3, 1, 1, 3]
result = numIdenticalPairs(list)
for element in result:
    print(element)