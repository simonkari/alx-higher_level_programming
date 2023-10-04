'use strict';
$(() => {
  // Define a constant variable BASE_URL
  const BASE_URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${BASE_URL}/people/5/?format=json`, (data, status) => {
    // Find the HTML element with the id "character"
    //and set its content to the 'name' property
    // from the response data.
    $('DIV#character').html(data.name);
  });
});
