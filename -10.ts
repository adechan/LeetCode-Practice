// Write the function shuffle(array) that shuffles (randomly reorders) elements of the array.
// Multiple runs of shuffle may lead to different orders of elements. 

// Won't work all the time because of the JS engine
const shuffle = (arr: number[]): number[] => {
  return arr.sort(() => Math.random() - 0.5);
}

const shuffleFisherYates = (arr: number[]): number[] => {
  // walk the array in the reverse order and swap each element with a random one before it
  for (let i = arr.length - 1; i >= 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));  // random index from 0 to i

    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return []
}

let arr = [1, 2, 3];

shuffle(arr);
console.log(arr);

shuffle(arr);
console.log(arr);

shuffle(arr);
console.log(arr);

export {}