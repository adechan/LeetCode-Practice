// Write a function filterRangeInPlace(arr, a, b) that gets an array arr and removes from it all values except those that 
// are between a and b. The test is: a ≤ arr[i] ≤ b.

// The function should only modify the array. It should not return anything.

let arr = [5, 3, 8, 1];
const filterRangeInPlace = (arr: number[], a: number, b: number): void => { 
  const numbersToDelete = arr.filter(value => a > value || value > b);

  numbersToDelete.forEach(element => {
    const index = arr.findIndex(arrElement => element === arrElement);
    arr.splice(index, 1)
  });
}

filterRangeInPlace(arr, 1, 4); // removed the numbers except from 1 to 4
console.log( arr ); // [3, 1]


export {}