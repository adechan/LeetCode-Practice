# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

def xorOperation(n, start):
    """
    :type n: int
    :type start: int
    :rtype: int
    """

    nums = []
    for i in range (0, n):
        nums.append(start + 2 * i)

    xor = 0
    for element in nums:
        xor ^= element

    return xor

n = 5
start = 0
result = xorOperation(5, 0)
print(result)
