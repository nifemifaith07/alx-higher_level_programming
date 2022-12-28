#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      console.log('x');
    }
  }
}
