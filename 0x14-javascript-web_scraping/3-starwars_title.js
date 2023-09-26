#!/usr/bin/node
// Shebang line specifying the interpreter

const request = require('request');
// Import the 'request' module to make HTTP requests

const BASE_URL = 'https://swapi-api.hbtn.io/api';
// Define the base URL of the Star Wars API

if (process.argv.length > 2) {
  // Check if a command-line argument (movie ID) is provided

  request(`${BASE_URL}/films/${process.argv[2]}/`, (err, res, body) => {
    // Make a GET request to the specified movie endpoint in the Star Wars API

    if (err) {
      // Handle any errors that may occur during the request
      console.log(err);
    }
    console.log(JSON.parse(body).title);
    // Parse the JSON response and print the movie title
  });
}
