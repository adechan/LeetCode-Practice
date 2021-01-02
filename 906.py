# Let's say a positive integer is a superpalindrome if it is a palindrome,
# and it is also the square of a palindrome.
# Now, given two positive integers L and R (represented as strings),
# return the number of superpalindromes in the inclusive range [L, R].
import math

class Solution(object):
    def isPalindrome(self, number):
        if str(number) == str(number)[::-1]:
            return True
        return False

    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        if len(L) < 1 or len(L) > 18 or len(R) < 1 or len(R) > 18:
            return 0

        if int(L) > int(R):
            return 0

        count = 0
        for number in range(int(L), int(R) + 1, 1):
            # it's palindrome, so we also check if its square is palindrome
            if self.isPalindrome(number):
                root = math.sqrt(number)

                if ".0" == str(root)[-2:]:
                    decimal_root = int(root)
                else:
                    decimal_root = root

                if self.isPalindrome(decimal_root):
                    count += 1

        return count


solution = Solution()
print(solution.superpalindromesInRange("92904622", "232747148"))
