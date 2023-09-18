// Write a function filterRange(arr, a, b) that gets an array arr, looks for elements with 
// values higher or equal to a and lower or equal to b and return a result as an array.

// The function should not modify the array. It should return the new array.

// Doesn't modify the original array
const filterRange = (arr: number[], a: number, b: number) => {
  // elements >= a && <= b

  return arr.filter((value) => value >= a && value <= b);
}

let arr = [5, 3, 8, 1];
let filtered = filterRange(arr, 1, 4);

console.log( filtered ); // 3,1 (matching values)
console.log( arr ); // 5,3,8,1 (not modified)