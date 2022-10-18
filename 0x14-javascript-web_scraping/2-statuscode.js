#!/usr/bin/node
// displays the status code of a GET request.
const request = require('request');
request.get(process.argv[2], function (error, outcome) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + outcome.statusCode);
  }
});
