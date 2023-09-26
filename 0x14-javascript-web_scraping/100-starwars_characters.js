#!/usr/bin/node
const request = require('request');

// Function to fetch characters from a Star Wars movie
function fetchCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('API Request Failed with Status Code:', response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);
    console.log(`Characters in ${movieData.title}:`);

    // Loop through characters and print their names
    movieData.characters.forEach(characterUrl => {
      request(characterUrl, (error, response, characterBody) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('API Request Failed with Status Code:', response.statusCode);
          return;
        }

        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
      });
    });
  });
}

// Check if a movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Please provide a movie ID as a command-line argument.');
} else {
  const movieId = process.argv[2];
  fetchCharacters(movieId);
}
