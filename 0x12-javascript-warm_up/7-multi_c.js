#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (!isNaN(number) && number > 0) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Invalid number of occurrences');
}
