# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.'
# For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> list:
        result = []
        for number in range(1, n + 1):
            if number % 15 == 0:
                result.append("FizzBuzz")
            elif number % 3 == 0:
                result.append("Fizz")
            elif number % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(number))

        return result


s = Solution()
print(s.fizzBuzz(15))