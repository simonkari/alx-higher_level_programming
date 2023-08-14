#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (typeof x !== 'number' || !Number.isInteger(x) || x <= 0) {
    throw new Error('Invalid input: x must be a positive integer.');
  }

  if (typeof theFunction !== 'function') {
    throw new Error('Invalid input: theFunction must be a function.');
  }

  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
