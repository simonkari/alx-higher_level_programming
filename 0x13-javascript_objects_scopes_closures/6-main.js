#!/usr/bin/node
const Square = require('./6-square');

function runSquarePrint(square, char = undefined) {
    square.charPrint(char);
}

const s1 = new Square(4);
runSquarePrint(s1);

runSquarePrint(s1, 'C');
