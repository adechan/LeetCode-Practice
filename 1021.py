# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B,
# with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are
# primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

def descomposeS(S):
    """
    :param S: string
    :return: List[string]
    """
    countLeft = 0
    countRight = 0
    descomposedS = []

    while len(S) != 0:
        new_string = ""

        for i in range (0, len(S)):
            if (S[i] == "("):
                countLeft = countLeft + 1
                new_string += S[i]

            if (S[i] == ")"):
                countRight = countRight + 1
                new_string += S[i]

            if (countLeft == countRight):
                descomposedS.append(new_string)
                S = S[i + 1: len(S)]
                print("S " + S)
                break

    return descomposedS

def removeOuterParentheses(S):
    """
    :type S: str
    :rtype: str
    """
    new_string = ""
    descomposedS = descomposeS(S)

    for element in descomposedS:
        modified_element = element[1: len(element) - 1]
        new_string += modified_element

    return new_string

S = "()()()()(())"
new_string = removeOuterParentheses(S)
print(new_string)