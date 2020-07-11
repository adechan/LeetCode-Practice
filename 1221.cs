using System;
using System.Collections.Generic;

namespace PracticeProblemsCode
{
    /*
    Balanced strings are those who have equal quantity of 'L' and 'R' characters.
    Given a balanced string s split it in the maximum amount of balanced strings.
    Return the maximum amount of splitted balanced strings.
    */
    public class Program
    {
        public static int BalancedStringSplit(string s)
        {
            int countL = 0;
            int countR = 0;

            int balanced = 0;

            foreach(char character in s)
            {
                if (character == 'L')
                    countL++;
                else
                    countR++;


                if (countL == countR)
                {
                    balanced++;
                    countR = 0;
                    countL = 0;
                }
            }

            return balanced;
        }

        public static void Main(string[] args)
        {
            string s = "LLLLRRRR";
            //int count = CountedChars(s, 6);
            //Console.WriteLine(count);

            int result = BalancedStringSplit(s);

            Console.WriteLine(result);

        }

    }
}
