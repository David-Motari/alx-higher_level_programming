#!/usr/bin/node

exports.converter = function (base) {
  return function (count) {
    return count.toString(base);
  };
};
