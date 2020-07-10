using System;

namespace PracticeProblemsCode
{
    /*
     *
     Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
     That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
     Return the answer in an array.
     */
    public class Program
    {
        public static int CountSmallerNumbers(int number, int[] list)
        {
            int count = 0;

            foreach (int element in list)
            {
                if (number > element)
                    count++;
            }

            return count;
        }

        public static int[] SmallerNumbersThanCurrent(int[] nums)
        {
            int[] new_list = new int[nums.Length];
            
            for (int i = 0; i < nums.Length; i++)
            {
                int count = CountSmallerNumbers(nums[i], nums);

                new_list[i] = count;
            }

            return new_list;
        }

        public static void Main(string[] args)
        {
            int[] nums = new int[4] { 6, 5, 4, 8 };

            int[] result = SmallerNumbersThanCurrent(nums);

            foreach (int element in result)
            {
                Console.WriteLine(element + " ");
            }
        }

    }
}
