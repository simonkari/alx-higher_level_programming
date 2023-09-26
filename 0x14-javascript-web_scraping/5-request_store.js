#!/usr/bin/node

// Import the 'fs' (file system) and 'request' modules
const fs = require('fs');
const request = require('request');

// Check if there are at least 4 command line arguments
if (process.argv.length > 3) {
  // Use the 'request' module to make an HTTP GET request to
  //the URL specified as the first command line argument
  request
    .get(`${process.argv[2]}`)
    // Pipe the response of the HTTP request to create
    //a writable stream
    .pipe(fs.createWriteStream(process.argv[3]));
}
