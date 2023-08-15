#!/usr/bin/node
// Square class
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint(c = 'X') {
    const line = c.repeat(this.width);
    for (let y = 0; y < this.height; y++) {
      console.log(line);
    }
  }
}

module.exports = Square;
