#!/usr/bin/node

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

const add = (a, b) => {
  console.log(a + b);
};

add(num1, num2);
