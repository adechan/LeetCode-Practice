# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).

def maxFromList(nums):
    """
    :param nums: List[int]
    :return: int
    """
    maximum = 0
    for element in nums:
        if element > maximum:
            maximum = element
    return maximum

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    products = []
    for i in range (0, len(nums)):
        for j in range (i + 1, len(nums)):
            products.append((nums[i] - 1) * (nums[j] - 1))

    maximum = maxFromList(products)
    return maximum

nums = [3, 4, 5, 2]
maximum = maxProduct(nums)
print(maximum)