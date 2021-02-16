# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

class Solution:
    def toBinary(self, n):
        binary = ""
        while n != 0:
            binary += str(n % 2)
            n = n // 2

        return binary[::-1]

    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = self.toBinary(x)
        y_bin = self.toBinary(y)

        x_bin_list = [el for el in x_bin]
        y_bin_list = [el for el in y_bin]

        if len(x_bin_list) < len(y_bin_list):
            for _ in range(len(y_bin_list) - len(x_bin_list)):
                x_bin_list.insert(0, "0")

        if len(x_bin_list) > len(y_bin_list):
            for _ in range(len(x_bin_list) - len(y_bin_list)):
                y_bin_list.insert(0, "0")

        distance = 0
        for i in range(0, len(x_bin_list)):
            if x_bin_list[i] != y_bin_list[i]:
                distance += 1
            else:
                continue

        return distance


s = Solution()
x = 1
y = 4
print(s.hammingDistance(x, y))