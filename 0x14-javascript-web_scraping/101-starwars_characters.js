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

    // Use map to create an array of Promises for fetching character names
    const charactersNamePromises = charactersURL.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      });
    });

    // Use Promise.all to wait for all character names to be fetched
    Promise.all(charactersNamePromises)
      .then(names => {
        // Print the character names, separated by newlines
        console.log(names.join('\n'));
      })
      .catch(err => {
        console.error('Error:', err);
      });
  });
} else {
  console.error('Please provide a movie ID as a command-line argument.');
}
