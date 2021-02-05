# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first_half = s[:len(s) // 2]
        first_half.reverse()

        for i in range(0, len(s) // 2):
            s[i] = s[len(s) - 1 - i]

        if len(s) % 2 == 0:
            s[(len(s) // 2):] = first_half
        else:
            s[(len(s) // 2) + 1:] = first_half

        return s

    def reverseString1(self, s):
        return s.reverse()

s = Solution()
list = ["1", "2", "3", "4", "5", "6"]
# list = ["1", "2", "3", "4", "5"]
print(s.reverseString(list))
