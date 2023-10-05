// Given a list const l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
// make l iterable such that it will return only odd numbers
// Use iterables.

Array.prototype[Symbol.iterator] = function () {
  const current = this;
  return {
    // Returns the next element of the iterator
    next: () => {
      while (current.length > 0) {
        const value = current.pop();
        if (value % 2 !== 0) {
          return { value, done: false };
        }
      }

      return { done: true };
    },
  };
};

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];
for (let i of l) {
  console.log(i);
}
