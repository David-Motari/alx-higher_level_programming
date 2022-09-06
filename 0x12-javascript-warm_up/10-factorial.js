#!/usr/bin/node

const factor = parseInt(process.argv[2]);

if (isNaN(factor) === true) {
  console.log(1);
} else {
  let ans = 0;
  ans = factorial(factor);
  console.log(ans);
}

function factorial (x) {
  if (x === 0 || x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
