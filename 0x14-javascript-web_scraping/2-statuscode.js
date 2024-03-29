#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node getStatusCode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }

  console.log(`code: ${response.statusCode}`);
});
