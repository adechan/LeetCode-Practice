// Write the function camelize(str) that changes dash-separated words like “my-short-string” into camel-cased “myShortString”.

// That is: removes all dashes, each word after dash becomes uppercase.

const camelize = (str: string): string => {
  const split = str.split('-');
  console.log(split);

  let transformed = '';

  split.forEach((element, index) => {
    if (index == 0) {
      transformed += element;
    }
    else { 
      transformed += element.substring(0, 1).toUpperCase() + element.substring(1).toLocaleLowerCase();
    }
  });
  
  return transformed
}

const camelizeV2 = (str: string): string => {
  return str
  .split('-')
  .map(
    (word, index) => index == 0 ? word : word[0].toUpperCase() + word.slice(1)
  )
  .join('');
}

console.log(camelizeV2("background-color") == 'backgroundColor');
console.log(camelizeV2("list-style-image") == 'listStyleImage');
console.log(camelizeV2("-webkit-transition") == 'WebkitTransition');