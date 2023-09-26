#!/usr/bin/node

// Import the 'fs' (file system) and 'request' modules
const fs = require('fs');
const request = require('request');

// Check if there are at least 4 command line arguments
if (process.argv.length > 3) {
  // Use the 'request' module to make an HTTP GET request to
  //the URL specified as the first command line argument (process.argv[2])
  request
    .get(`${process.argv[2]}`)
    // Pipe the response of the HTTP request to create a writable
    //stream that writes the data to a file specified as the second 
    //command line argument (process.argv[3])
    .pipe(fs.createWriteStream(process.argv[3]));
}
