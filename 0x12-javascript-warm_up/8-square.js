#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (NaN(size) === true) {
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
