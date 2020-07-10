using System;
using System.Collections.Generic;

namespace PracticeProblemsCode
{
    /*
     Given an integer number n, return the difference between the product of its digits and the sum of its digits.
     */
    public class Program
    {

        public static List<int> GetDigits(int n)
        {
            List<int> digits = new List<int>();

            while (n != 0)
            {
                digits.Add(n % 10);
                n = n / 10;
            }

            return digits;
        }

        public static int Product(List<int> digits)
        {
            int product = 1;

            foreach (int digit in digits)
                product *= digit;

            Console.WriteLine(product);

            return product;
        }

        public static int Sum(List<int> digits)
        {
            int sum = 0;

            foreach (int digit in digits)
                sum += digit;

            Console.WriteLine(sum);
            return sum;
        }

        public static int SubtractProductAndSum(int n)
        {
            List<int> digits = GetDigits(n);

            int product = Product(digits);
            int sum = Sum(digits);

            return product - sum;
        }

        public static void Main(string[] args)
        {

            int n = 234;
            Console.WriteLine(SubtractProductAndSum(n));

        }

    }
}
