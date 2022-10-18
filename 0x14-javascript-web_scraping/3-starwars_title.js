#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (error, outcome, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(content).title);
  }
});
