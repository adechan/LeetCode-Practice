// Create a custom type CountIterator such that iterating over
// an object of this type will return consecutive numbers starting from 0.
// That is, it will first return 0, then 1, then 2, and so on (i iterates from 0 indefinitely).

const customIterator = {};
customIterator[Symbol.iterator] = function () {
  let i = -1;

  return {
    next: () => {
      while (true) {
        i += 1;
        return {
          value: i,
          done: false,
        };
      }
      return { done: true };
    },
  };
};

for (let i of customIterator) {
  console.log(i);
}
