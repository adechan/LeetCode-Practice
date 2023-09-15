// Given two strings s and t, determine if they are isomorphic.

// All occurrences of a character must be replaced with another character while preserving the order of characters. 
// No two characters may map to the same character, but a character may map to itself.

// Isomorphic: if there's a one-to-one character mapping between two strings while preserving the order of characters.

const getDistinctValues = (s: string) => {
  const distinct: string[] = [];

  for (let i = 0; i < s.length; i++) {
    if (!distinct.includes(s[i])) {
      distinct.push(s[i])
    }
  }

  return distinct;
}

const isIsomorphic = (s: string, t: string): boolean => {
  const distinctFirst = getDistinctValues(s);
  const distinctSecond = getDistinctValues(t);

  if (distinctFirst.length !== distinctSecond.length) {
    return false;
  }


};

console.log(isIsomorphic("egg", "add"))
console.log(isIsomorphic("foo", "bar"))
console.log(isIsomorphic("paper", "title"))
console.log(isIsomorphic("bbbaaaba", "aaabbbba"))