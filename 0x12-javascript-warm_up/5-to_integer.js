#!/usr/bin/node
const count = process.argv[2];
if (isNaN(count) === true) {
  cosole.log('Not a number');
} else {
  console.log('My number: ' + count);
}
