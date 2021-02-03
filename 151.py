# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
import re

class Solution:
    def getWords(self, string: str):
        r = re.compile("\\w+")
        matches = re.findall(r, string)
        return matches

    def reverseWords(self, s: str) -> str:
        words = self.getWords(s)
        words.reverse()

        reversedString = ""
        for word in words:
            reversedString += word + " "

        return reversedString.rstrip()

input = ' s       pokEfM9Smb     CkB   I YR6mlSb  NMUjwXO1zT      1jYFIj5     3yKuOFv   VUgEc     SDj4      X9 yxJ7m1MFQ3     2czWYkN   mcn7t UQB      0uz   gWR  6cqWMJTboG  kc     qvpXw   Vemp     ckiI8Gnj GDgyIK7e    kJ       HNuW      G6axXAKZ     mrdlIlUz    1ei  4uriBAE       uBq     iP3V       tgn1 tcp4    OQkssUH3     Cu       JRvD YUUr0K   5NfLPJLii    EBWEJ    99q    Gw    f AkEwlaJJ12  NjygVYQxZt       o GWxAguB    gBxLKLnO   Fz2y    B   Exih2X  Ob9Z6m8o  Ko   t6      QBR     a1Lq  AU35   QN  UIRFK   PEOn4      5JQvOh jmOL42    Xd9lK1  Rmh D    PzSeb   MPh     7 b5tC6     niT    54w3VPhy  h3w5esv  5       B     gUQ     Ggi2T 4IIX84       MUfe      sgzWdNZ      yYIKbONI8U    uvZOd4d  ne0oMp     LJTF       p  6       Tu6BaSwM AUFHHl       H    kimskH9s      VdwSz     b  6M xVeFv6DNN       5M64     aT9x5LF9     vO   epjgc     isAROwj2A      0hAFVXt  nyZd5ISv  XKcRG      71J    7e9K 4P9dpRW       VAfA Rmy4M9sF       GX7Cv  k8      8yilzwDHO   J   Ljq3C      CP5096AS       Fw8  0FARKi6x1v      LUT5UeJeU  GBjxE LpF1cyNa   X9ceJx  Q2YX3r dMpdX       K Ij  Q2cOu     wg   PBvcVYz  93zgWnXC       0u   of7mdXO     I6xRvT     Ao Y9e   4l  TVi   s    1tckz5O     oJAM8y bI6ppw    h   ICtUeokj  hNooLvzq Edx1I      o   yJ0ebu   V7 60h      clMtNMYjx yuIxtWb     6    94YHa8c    YT1aXn  je06     6xV5eVX7ug  z6r   U1   6x  ss  0PZAfLVjEi  pdZJmxA9   Qy17QwX MA     Nv   j Fap3X    Lme1mm rlusXgLD     f7aX0mEs0n   RkB    tA       h8   Dli FxsVvNgq  qAb8qUO'

s = Solution()
print(s.getWords(input))
print(s.reverseWords(input))
