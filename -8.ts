// You have an array of user objects, each one has name, surname and id.
// Write the code to create another array from it, of objects with id and fullName, 
// where fullName is generated from name and surname.

type User = {
  name: string,
  surname: string,
  id: number,
}

type MappedUsers = {
  fullName: string,
  id: number,
}

const mapUsers = (users: User[]): MappedUsers[] => {
  const mappedUsers = users
  .slice()
  .map(user => ({
    id: user.id,
    fullName: `${user.name} ${user.surname}`
  }));

  return mappedUsers;
}


let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [ john, pete, mary ];

const usersMapped = mapUsers(users);

console.log( usersMapped[0].id ) // 1
console.log( usersMapped[0].fullName ) // John Smith

export {}