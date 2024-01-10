#!/usr/bin/node
// prints My number: <first argument converted in integer>
const numb = process.argv[2];
if (isNaN(numb) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numb);
}
