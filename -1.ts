// A maximal subarray
// The input is an array of numbers, e.g. arr = [1, -2, 3, 4, -9, 6].
// The task is: find the contiguous subarray of arr with the maximal sum of items.
// Write the function getMaxSubSum(arr) that will return that sum.

// Kadane's Algorithm: very efficient

const getMaxSubSum = (arr: number[]): number => {
  let currentSum = 0;
  let maxSum = 0;

  for (let i = 0; i < arr.length; i++) {
    currentSum += arr[i];

    if (currentSum < 0) {
      currentSum = 0;
    }

    if (currentSum > maxSum) {
      maxSum = currentSum
    }
  } 


  return maxSum;
}


console.log(getMaxSubSum([-1, 2, 3, -9]) == 5); // 2, 3
console.log(getMaxSubSum([2, -1, 2, 3, -9]) == 6); // 2, -1, 2, 3
console.log(getMaxSubSum([-1, 2, 3, -9, 11]) == 11); // 11
console.log(getMaxSubSum([-2, -1, 1, 2]) == 3); // 1, 2
console.log(getMaxSubSum([100, -9, 2, -3, 5]) == 100); // 100
console.log(getMaxSubSum([1, 2, 3]) == 6); // 1, 2, 3
console.log(getMaxSubSum([-1, -2, -3])); // 0;