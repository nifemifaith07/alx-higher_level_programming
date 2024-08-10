#!/usr/bin/node
const fs = require('fs');
const dataA = fs.readFileSync(process.argv[2], 'utf8');
const dataB = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], dataA + dataB);
