#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const argList = process.argv.slice(2).map(Number).sort((x, y) => x - y);
  const secondHighest = argList[argList.length - 2];
  console.log(secondHighest);
}
