#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node getStarWarsMovieTitle.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status Code ${response.statusCode}`);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  console.log(`Title: ${movieData.title}`);
});
