// Develop an iterator that takes an array and a chunk size as input and returns arrays of elements in chunks of the specified size.

function chunkArrayV2(array, chunkSize) {
  let index = 0;

  return {
    // iterator
    next: () => {
      if (index >= array.length) {
        return { done: true };
      }

      const chunk = array.slice(index, index + chunkSize);
      index += chunkSize;

      return { value: chunk, done: false };
    },
    // so you can iterate using for...of on this
    [Symbol.iterator]: function () {
      return this;
    },
  };
}

function chunkArray(array, chunkSize) {
  let index = 0;

  return {
    // so you can iterate using for...of on this
    [Symbol.iterator]: function () {
      return {
        // iterator
        next: () => {
          if (index >= array.length) {
            return { done: true };
          }

          const chunk = array.slice(index, index + chunkSize);
          index += chunkSize;

          return { value: chunk, done: false };
        },
      };
    },
  };
}

// Example usage:
const myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const chunkSize = 3;
const chunkIterator = chunkArray(myArray, chunkSize);

let chunk;
for (const chunk of chunkIterator) {
  console.log(chunk);
}
