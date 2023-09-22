// Write the function getAverageAge(users) that gets an array of objects with property age and returns the average age.
// The formula for the average is (age1 + age2 + ... + ageN) / N.

const getAverageAge = (users: {name: string, age: number}[]): number => {
  const totalAge = users.reduce((_prev, current) => {
    return _prev + current.age;
  }, 0)

  return totalAge / users.length;
}

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 29 };

let arr = [ john, pete, mary ];

console.log( getAverageAge(arr) ); // (25 + 30 + 29) / 3 = 28

export {}