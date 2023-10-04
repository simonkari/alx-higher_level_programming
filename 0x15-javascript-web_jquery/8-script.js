'use strict';
$(() => {
  // Define a constant variable BASE_URL
  const BASE_URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${BASE_URL}/films/?format=json`, (data, status) => {
    data.results.forEach(film => {
      // For each film, create an <li> (list item) element
      //append this <li> element to the <ul> (unordered list) element
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});
