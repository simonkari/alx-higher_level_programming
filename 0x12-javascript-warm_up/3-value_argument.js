#!/usr/bin/node

const [, , argument] = process.argv;

console.log(argument ? argument : 'No argument');
