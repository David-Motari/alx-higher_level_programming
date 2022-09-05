#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x) === true) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  for (i; i < x; i++) {
    console.log('C is fun ');
  }
}
