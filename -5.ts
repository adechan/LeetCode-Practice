// Sort in decreasing order 

// Sort in place
const sortDecreasing = (arr: number[]): void => {
  arr.sort((a, b) => b - a)
}

// Sort and return new array
const sortDecreasingNewArray = (arr: number[]): number[] => {
  const newArr = [...arr];
  return newArr.sort((a, b) => b - a)
}

let arr = [5, 2, 1, -10, 8];
sortDecreasing(arr);

console.log( arr ); // 8, 5, 2, 1, -10

export {}