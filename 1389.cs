using System;

namespace PracticeProblemsCode
{
    /*
    Given two arrays of integers nums and index. Your task is to create target array under the following rules:
    Initially target array is empty.
    From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
    Repeat the previous step until there are no elements to read in nums and index.
    Return the target array.

    It is guaranteed that the insertion operations will be valid.
    */
    public class Program
    {

        public static int[] InsertAt(int[] list, int index, int element)
        {
            int[] result = new int[list.Length + 1];
        
            for (int i = 0; i < list.Length + 1; i++)
            {
                if (i < index)
                    result[i] = list[i];
                else if (i == index)
                    result[i] = element;
                else
                    result[i] = list[i - 1];
            }

            return result;
        }

        public static int[] CreateTargetArray(int[] nums, int[] index)
        {
            int[] target = new int[0];

            int i = 0;
            while(i < nums.Length)
            {
                target = InsertAt(target, index[i], nums[i]);
                i++;
            }

            return target;
        }

        public static void Main(string[] args)
        {
            int[] nums = new int[5] {1, 2, 3, 4, 0};
            int[] index = new int[5] { 0, 1, 2, 3, 0};

            int[] result = CreateTargetArray(nums, index);
            foreach (int el in result)
                Console.WriteLine(el + " ");


        }

    }
}
