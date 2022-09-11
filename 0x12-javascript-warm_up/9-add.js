#!/usr/bin/node

function add (x, y) {
  return x + y;
}
const add1 = Number(process.argv[2]);
const add2 = Number(process.argv[3]);
console.log(add(add1, add2));
