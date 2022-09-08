#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
      let j = 0;
      for (j; j < this.height; j++) { console.log(c.repeat(this.width)); }
    } else {
      let j = 0;
      for (j; j < this.height; j++) { console.log(c.repeat(this.width)); }
    }
  }
};
