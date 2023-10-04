'use strict';
$(() => {
  $('INPUT#btn_translate').click(() => {
    // Define a constant variable BASE_URL with the URL of the API endpoint.
    const BASE_URL = 'https://fourtonfish.com';
    // Get the value entered in the <input> element with the id "language_code."
    const code = $('INPUT#language_code').val();

    // see https://www.loc.gov/standards/iso639-2/php/code_list.php
    $.get(`${BASE_URL}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
