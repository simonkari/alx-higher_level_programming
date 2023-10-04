'use strict';
$(() => {
  // Define a constant variable BASE_URL
  const BASE_URL = 'https://fourtonfish.com';

  // Make an HTTP GET request to the URL
  $.get(`${BASE_URL}/hellosalut/?lang=fr`, (data, status) => {
    // Find the HTML element with the id "hello"
    //and set its content to the 'hello' property
    $('DIV#hello').html(data.hello);
  });
});
