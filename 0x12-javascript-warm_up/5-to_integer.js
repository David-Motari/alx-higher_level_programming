#!/usr/bin/node

const temp = parseInt(process.argv[2]);

if (isNaN(temp) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + temp);
}
