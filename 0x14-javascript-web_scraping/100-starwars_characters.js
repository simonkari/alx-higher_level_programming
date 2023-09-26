#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.hbtn.io/api';

// Check if there is at least one command-line argument
if (process.argv.length > 2) {
  // Make an HTTP GET request to retrieve movie information using the provided movie ID
  request(`${BASE_URL}/films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.error('Error:', err);
      return;
    }

    // Parse the JSON response to extract character URLs
    const charactersURL = JSON.parse(body).characters;

    // Loop through character URLs and fetch each character's data
    charactersURL.forEach(characterUrl => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          console.error('Error:', err);
          return;
        }

        // Parse the JSON response to extract and print the character's name
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
} else {
  console.error('Please provide a movie ID as a command-line argument.');
}
