#!/usr/bin/node
const request = require('request');

// Function to fetch characters from a Star Wars movie by ID
function getCharactersFromMovie(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
  
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      console.log(`Characters from Star Wars Episode ${movieData.episode_id}: ${movieData.title}`);
      console.log("====================================");

      characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(`- ${characterData.name}`);
          } else {
            console.error(`Error fetching character: ${charError}`);
          }
        });
      });
    } else {
      console.error(`Error fetching movie data: ${error}`);
    }
  });
}

// Usage: Replace '3' with the movie ID you want to fetch characters for
getCharactersFromMovie(3);
