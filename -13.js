// Let’s say we received an array of users in the form {id:..., name:..., age:... }.
// Create a function groupById(arr) that creates an object from it, with id as the key, and array items as values.
// Such function is really handy when working with server data.
// In this task we assume that id is unique. There may be no two array items with the same id.
// Please use array .reduce method in the solution.

const groupById = (arr) => {
  return arr.reduce((finalObj, value) => {
    finalObj[value.id] = value;
    return finalObj;
  }, {})
}

let users = [
  {id: 'john', name: "John Smith", age: 20},
  {id: 'ann', name: "Ann Smith", age: 24},
  {id: 'pete', name: "Pete Peterson", age: 31},
];

let usersById = groupById(users);
console.log(usersById);

export {}