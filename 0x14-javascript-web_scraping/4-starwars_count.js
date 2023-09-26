#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  // Check if a command-line argument (API URL) is provided

  request(`${process.argv[2]}`, (err, res, body) => {
    // Make a GET request to the specified API URL

    if (err) {
      // Handle any errors that may occur during the request
      console.log(err);
    } else if (body) {
      // Check if the response body is not empty

      const charFilms = JSON.parse(body).results.filter(
        x => x.characters.find(y => y.match(/\/people\/18\/?$/))
      );

      // Parse the JSON response, filter movies with Wedge Antilles, and count them
      console.log(charFilms.length);
    }
  });
}
