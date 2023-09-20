// You have an array of user objects, each one has user.name. Write the code that converts it into an array of names.

type User = {
  name: string,
  age: number,
};

const getNamesV1 = (users: User[]): string[] => {
  const names: string[] = [];

  for (const user of users) {
    names.push(user.name)
  }

  return names;
}

const getNamesV2 = (users: User[]): string[] => {
  return users.map(user => user.name)
}

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let users = [ john, pete, mary ];
let names = getNamesV2(users);

console.log( names ); // John, Pete, Mary

export {}