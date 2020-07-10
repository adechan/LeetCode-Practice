using System;
using System.Collections.Generic;

namespace PracticeProblemsCode
{
    /*
     We are given a list nums of integers representing a list compressed with run-length encoding.
     Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
     Return the decompressed list.
     */
    public class Program
    {
        public static int[] GenerateArray(Tuple<int, int> pair)
        {
            int length = pair.Item1;   
            int[] array = new int[length];

            for (int i = 0; i < length; i++)
                array[i] = pair.Item2;

            return array;
        }

        public static List<Tuple<int, int>> GetPairs(int[] nums)
        {
            List<Tuple<int, int>> pairs = new List<Tuple<int, int>>();

            for (int i = 0; i < nums.Length; i += 2)
            {
                pairs.Add(new Tuple<int, int>(nums[i], nums[i + 1]));
            }

            return pairs;
        }

        public static int[] DecompressRLElist(int[] nums)
        {
            List<int> result = new List<int>();

            int[] array;

            List<Tuple<int, int>> pairs = GetPairs(nums);

            foreach (Tuple<int, int> pair in pairs)
            {
                array = GenerateArray(pair);

                foreach (int element in array)
                {
                    result.Add(element);
                }

            }

            return result.ToArray();
         
        }

        public static void Main(string[] args)
        {
            int[] nums = new int[4] { 1, 1, 2, 3 };

            int[] result = DecompressRLElist(nums);

            foreach (int element in result)
            {
                Console.WriteLine(element + " ");
            }


        }

    }
}
