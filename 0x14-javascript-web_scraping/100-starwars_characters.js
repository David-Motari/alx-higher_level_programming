#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const request2 = require('request');
request('https://swapi-api.hbtn.io/api/' + process.argv[2], function (error, response, content) {
  if (error) {
    console.log(error);
  } else {
    const dict = JSON.parse(content).characters;
    for (const d in dict) {
      const chars = dict[d];
      request2(chars, function (error, response, content2) {
        if (error) {
          console.log(error);
        } else {
          const actor = JSON.parse(content2).name;
          console.log(actor);
        }
      });
    }
  }
});
