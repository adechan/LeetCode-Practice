# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            # if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
            #     string += char.lower()
            if char.isalnum():
                string += char.lower()
            else:
                continue

        if string == string[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))