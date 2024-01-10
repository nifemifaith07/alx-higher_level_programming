#!/usr/bin/node
// computes and prints a factorial 
function factorial (num) {
  return isNaN(num) || num === 0 ? 1 : num * factorial(num - 1);
}
console.log(factorial(Number(process.argv[2])));
