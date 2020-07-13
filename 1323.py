# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

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

def digitsArray(num):
    """
    :param num: int
    :return: List[int]
    """
    digits = []
    while (num != 0):
        digit = num % 10
        digits.append(digit)
        num = num // 10

    digits.reverse()
    return digits

def changeDigit(digit):
    """
    :param digit: int
    :return: int
    """
    if (digit == 9):
        digit = 6
    else:
        digit = 9
    return digit

def changeToNewNumber(digits, index):
    """
    :param number: List[int], index: int
    :return: List[int]
    """
    new_number = []

    for i in range (0, len(digits)):
        if i == index:
            new_number.append(changeDigit(digits[i]))
        else:
            new_number.append(digits[i])
    return new_number

def digitsToNumber(digits):
    """
    :param digits: List[int]
    :return: int
    """
    n = ""
    for digit in digits:
         n += str(digit)
    return int(n)

def maximum69Number(num):
    """
    :type num: int
    :rtype: int
    """
    changed_numbers = []

    digits = digitsArray(num)
    count_digit_9 = 0
    for i in range (0, len(digits)):
        if digits[i] == 9:
            count_digit_9 = count_digit_9 + 1

    if count_digit_9 == len(digits):
        return num

    for i in range (0, len(digits)):
        changed_numbers.append(digitsToNumber(changeToNewNumber(digits, i)))

    maximum = maxFromList(changed_numbers)
    return maximum


num = 9669
d = maximum69Number(num)
print(d)

# n = [1, 2, 3]
# d = digitsToNumber(n)
# print(d)