// Let arr be an array.
// Create a function unique(arr) that should return an array with unique items of arr.

const unique2 = (arr: string[]): string[] => {
  const filtered = arr.filter((value, index, array) => {
    const indexFound = array.indexOf(value, index + 1);

    return indexFound === -1 ? true : false;
  })

  return filtered
}

/**
 * Not very performant.
 * If the array was very long, like 1_000 length, then we would need to do 1_000 x 1_000 comparisons.
 * Better use Map & Set to optimize this
 */
const unique = (arr: string[]): string[] => {
  const filtered: string[] = [];

  arr.forEach(element => {
    if (!filtered.includes(element)) {
      filtered.push(element);
    }
  });

  return filtered;
}

let strings = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

console.log( unique(strings) ); // Hare, Krishna, :-O

export {}