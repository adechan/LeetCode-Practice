// Make a number iterable

Number.prototype[Symbol.iterator] = function () {
  let current = this;
  return {
    next: () => {
      if (current) {
        let value = current % 10;
        current = parseInt(current / 10);
        return { value, done: false };
      } else {
        return { done: true };
      }
    },
  };
};

for (let i of 12345) {
  console.log(i);
}
// 5 4 3 2 1
