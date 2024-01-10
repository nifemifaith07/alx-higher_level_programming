#!/usr/bin/node
// prints x times “C is fun”, x is the 1st argument of the script
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
