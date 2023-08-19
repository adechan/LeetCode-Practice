const isEven = (n) => n % 2 === 0;
const matchParentheses = (s) => s === ")" ? true : false;
const matchCurly = (s) => s === "}" ? true : false;
const matchSquare = (s) => s === "]" ? true : false;
const getCloseBracketBasedOnOpen = (s) => {
    if (s === "(")
        return ")";
    if (s === "{")
        return "}";
    if (s === "[")
        return "]";
    return '';
};
const checkIfParenthesesMatchInNumbers = (s) => {
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
    };
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
    const sameParentheses = counters.parentheses.open === counters.parentheses.close;
    const sameCurly = counters.curly.open === counters.curly.close;
    const sameSquares = counters.square.open === counters.square.close;
    if (!sameParentheses || !sameCurly || !sameSquares) {
        return false;
    }
    return true;
};
const OPEN_BRACKETS = ["(", "[", "{"];
const CLOSE_BRACKETS = [")", "]", "}"];
const isValid = (s) => {
    var _a;
    // Something is missing
    if (!(isEven(s.length))) {
        return false;
    }
    if (!checkIfParenthesesMatchInNumbers(s)) {
        return false;
    }
    const openBrackets = [];
    for (let i = 0; i < s.length; i++) {
        if (OPEN_BRACKETS.includes(s[i])) {
            openBrackets.push(s[i]);
        }
        if (CLOSE_BRACKETS.includes(s[i])) {
            const lastValueInOpens = (_a = openBrackets.pop()) !== null && _a !== void 0 ? _a : '';
            if (getCloseBracketBasedOnOpen(lastValueInOpens) !== s[i]) {
                return false;
            }
        }
    }
    return true;
};
console.log(isValid("([)]"));
// console.log(isValid('([])'))
// console.log(isValid("([()])"))
//# sourceMappingURL=20.js.map