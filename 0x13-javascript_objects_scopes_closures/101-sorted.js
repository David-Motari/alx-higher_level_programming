#!/usr/bin/node

const dictionary = require('./101-data.js').dictionary;
const newdictionary = {};
for (const key in dictionary) {
  if (newdictionary[dictionary[key]] === undefined) {
    newdictionary[dictionary[key]] = [key];
  } else {
    newdictionary[dictionary[key]].push(key);
  }
}
console.log(newdictionary);
