// Create a constructor function Calculator that creates “extendable” calculator objects.
// The task consists of two parts.

// 1. First, implement the method calculate(str) that takes a string like "1 + 2" 
// in the format “NUMBER operator NUMBER” (space-delimited) and returns the result. Should understand plus + and minus -.

// Usage example:
// let calc = new Calculator;
// alert( calc.calculate("3 + 7") ); // 10

// 2. Then add the method addMethod(name, func) that teaches the calculator a new operation. 
// It takes the operator name and the two-argument function func(a,b) that implements it.

// For instance, let’s add the multiplication *, division / and power **:
// let powerCalc = new Calculator;
// powerCalc.addMethod("*", (a, b) => a * b);
// powerCalc.addMethod("/", (a, b) => a / b);
// powerCalc.addMethod("**", (a, b) => a ** b);
// let result = powerCalc.calculate("2 ** 3");
// alert( result ); // 8

// No parentheses or complex expressions in this task.
// The numbers and the operator are delimited with exactly one space.
// There may be error handling if you’d like to add it.

function Calculator() {
  this.methods = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
  };

  this.addMethod = function(name, func) {
    if (!this.methods.hasOwnProperty(name)) {
      this.methods[name] = func;
    }
  }

  this.calculate = function(str) {
    // str: NUMBER operator NUMBER
    const elements = str.split(' ');
    const a = +elements[0];
    const operator = elements[1];
    const b = +elements[2];
    
    if (this.methods[operator] !== undefined) { // or use this.methods.hasOwnProperty(operator)
      return this.methods[operator](a, b);
    }
  }
}

const calculator = new Calculator();
console.log(calculator.calculate("1 + 2"));

calculator.addMethod("*", (a, b) => a * b);
calculator.addMethod("/", (a, b) => a / b);
calculator.addMethod("**", (a, b) => a ** b);

console.log(calculator.calculate("2 ** 3"))

export {}