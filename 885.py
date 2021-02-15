# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                count = 1
                for j in range(1, len(needle)):
                    if i + j <= len(haystack) - 1 and haystack[i + j] == needle[j]:
                        count += 1
                    else:
                        break
                if count == len(needle):
                    return i
            else:
                continue
        return -1

    def strStr1(self, haystack: str, needle: str):
        if needle == "":
            return 0

        if len(needle) > len(haystack):
            return -1

        try:
            index = haystack.index(needle[0])
        except:
            return -1

        while index <= len(haystack):
            count = 0
            if len(needle) >= 2 and index == len(haystack) - 1:
                return -1

            for j in range(0, len(needle)):
                if index + j < len(haystack) and haystack[index + j] == needle[j]:
                    count += 1
                else:
                    break

            if count == len(needle):
                return index

            try:
                index = haystack.index(needle[0], index + 1, len(haystack))
            except:
                return -1

        return -1

    def strStr2(self, haystack: str, needle: str):
        if len(needle) == 0:
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1


s = Solution()
haystack = "mississippi"
needle = "sippia"
print(s.strStr1(haystack, needle))