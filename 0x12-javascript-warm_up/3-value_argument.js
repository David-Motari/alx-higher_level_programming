#!/usr/bin/node

if (process.argv !== 'undefined' && process.argv !== 'null') {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
