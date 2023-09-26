#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node countWedgeAntillesMovies.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Status Code ${response.statusCode}`);
    process.exit(1);
  }

  const movies = JSON.parse(body).results;
  const wedgeAntillesMovies = movies.filter(movie =>
    movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );

  console.log(`Number of movies with Wedge Antilles: ${wedgeAntillesMovies.length}`);
});
