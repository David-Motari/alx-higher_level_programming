#!/usr/bin/node

const array1 = require('./100-data').list;
console.log(array1);
let i = 0;
const map1 = array1.map(x => x * i++);

console.log(map1);
