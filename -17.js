// Implement iterable that splits into chunks of 4.
// That is, each element that is returned from the for loop should be 4
// integers from the above array: [0, 1, 2, 3], then the next element is [4, 5, 6, 7], and so on.

Array.prototype[Symbol.iterator] = function () {
  const current = this;
  let index = 0;
  return {
    next: () => {
      if (index >= current.length) {
        return { done: true };
      }

      const elements = [];
      for (let i = 0; i < 4; i++) {
        elements.push(current[index] || 0);
        index += 1;
      }

      return { value: elements, done: false };
    },
  };
};

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];
for (let i of l) {
  console.log(i);
}
