#!/usr/bin/node
// prints theaddition of two numbers
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(process.argv[2], process.argv[3]);
