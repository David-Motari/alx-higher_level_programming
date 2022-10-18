#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');

request(process.argv[2], function (error, response, outcome) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(outcome).results;
    const count = results.filter((elements) => {
      return elements.characters.filter((url) => { return url.includes('18'); }).length;
    }).length;
    console.log(count);
  }
});
