#!/usr/bin/node

if (process.argv === 'undefined' && process.argv === 'null') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
