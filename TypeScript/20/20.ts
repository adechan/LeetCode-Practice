const isEven = (n: number) => n % 2 === 0; 

const matchParentheses = (s: string) => s === ")" ? true: false
const matchCurly = (s: string) => s === "}" ? true: false
const matchSquare = (s: string) => s === "]" ? true: false

const getCloseBracketBasedOnOpen = (s: string) => {
  if (s === "(") return ")";
  if (s === "{") return "}"
  if (s === "[") return "]";

  return '';
}

const checkIfParenthesesMatchInNumbers = (s: string) => {
  const counters = {
      parentheses: {
        open: 0,
        close: 0,
    },
    curly: {
        open: 0,
        close: 0,
    }, 
    square: {
        open: 0,
        close: 0,
    }
  }  

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") { 
        counters.parentheses.open += 1;
    }

      if (s[i] === ")") { 
        counters.parentheses.close += 1;
    }

      if (s[i] === "{") { 
        counters.curly.open += 1;
    }

      if (s[i] === "}") { 
        counters.curly.close += 1;
    }

      if (s[i] === "[") { 
        counters.square.open += 1;
    }

      if (s[i] === "]") { 
        counters.square.close += 1;
    }
  }

  const sameParentheses = counters.parentheses.open === counters.parentheses.close
  const sameCurly = counters.curly.open === counters.curly.close
  const sameSquares = counters.square.open === counters.square.close
  
  if (!sameParentheses || !sameCurly || !sameSquares) {
    return false;
  }

  return true;
}

const OPEN_BRACKETS: string[] = ["(", "[", "{"]
const CLOSE_BRACKETS: string[] = [")", "]", "}"]

const isValid = (s: string): boolean => {
  // Something is missing
  if (!(isEven(s.length))) {
    return false;
  }

  if (!checkIfParenthesesMatchInNumbers(s)) {
    return false;
  }

  const openBrackets: string[] = []

  for (let i = 0; i < s.length; i++) {
    if (OPEN_BRACKETS.includes(s[i])) { 
      openBrackets.push(s[i]);
    }
    if (CLOSE_BRACKETS.includes(s[i])) {
      const lastValueInOpens = openBrackets.pop() ?? ''
      if (getCloseBracketBasedOnOpen(lastValueInOpens) !== s[i]) {
        return false;
      }
    }
  }

  return true;
}

// console.log(isValid("([)]"))
// console.log(isValid('([])'))
// console.log(isValid("([()])"))
