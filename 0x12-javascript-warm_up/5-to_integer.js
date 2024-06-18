#!/usr/bin/node
const process = require('process');
const x = parseFloat(process.argv[2]);
if (!isNaN(x)) {
  console.log(x);
}
else {
  console.log("Not a number");
}
