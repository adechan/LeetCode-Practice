# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def decompose(self, number):
        result = []
        while number:
            result.append(number % 10)
            number //= 10

        reverse = []
        for i in range(len(result) - 1, -1, -1):
            reverse.append(result[i])
        return reverse

    def plusOne(self, digits: list) -> list:
        number = 0
        size = len(digits) - 1
        for i in range(0, len(digits)):
            number += digits[i] * (10 ** (size - i))

        number += 1

        result = self.decompose(number)
        while len(result) < len(digits):
            result.insert(0, 0)
        return result


s = Solution()
digits = [3, 2, 3, 9]
# digits = [0, 0]
print(s.plusOne(digits))
