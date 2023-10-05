// Build an iterator that iterates over the characters of a given string.

function createStringIterator(str) {
  let index = 0;

  return {
    [Symbol.iterator]: function () {
      return {
        next: () => {
          if (index >= str.length) {
            return { done: true };
          }

          const currentValue = str[index];
          index += 1;
          return {
            value: currentValue,
            done: false,
          };
        },
      };
    },
  };
}

const stringIterator = createStringIterator("CustomStringHere");

for (char of stringIterator) {
  console.log(char);
}
