#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body).reduce((completed, todos) => {
    if (!completed[todos.userId]) {
      if (todos.completed) {
        completed[todos.userId] = 1;
      }
    } else {
      if (todos.completed) {
        completed[todos.userId] += 1;
      }
    }
    return completed;
  }, {});
  console.log(dict);
});
