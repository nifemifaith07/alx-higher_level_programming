#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  const item = dict[key];

  if (!newDict[item]) {
    newDict[item] = [];
  }
  newDict[item].push(key);
}
console.log(newDict);
