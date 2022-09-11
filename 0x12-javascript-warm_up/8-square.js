#!/usr/bin/node

const multi = parseInt(process.argv[2]);

if (isNaN(multi) === true) {
  console.log('Missing size');
} else {
  let j = 0;
  for (j; j < multi; j++) {
    const char = 'X';
    const str = char.repeat(multi);
    console.log(str);
  }
}
