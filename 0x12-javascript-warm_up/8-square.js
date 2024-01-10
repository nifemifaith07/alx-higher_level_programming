#!/usr/bin/node
// prints a square, 1st argument is the size of the square
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size) === true) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < size; i++) {
    line += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(line);
  }
}
