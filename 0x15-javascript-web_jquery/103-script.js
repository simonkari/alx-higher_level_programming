'use strict';
$(() => {
  // Define a function called translateHello.
  const translateHello = () => {
    const BASE_URL = 'https://fourtonfish.com';
    // Get the value entered in the <input> element
    //with the id "language_code."
    const code = $('INPUT#language_code').val();

    // see https://www.loc.gov/standards/iso639-2/php/code_list.php
    $.get(`${BASE_URL}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  };

  $('INPUT#btn_translate').click(translateHello);
  // Add a keydown event listener to the "language_code" input element.
  $('INPUT#language_code').keydown((ev) => {
    // Check if the key pressed is 'Enter' (key code 13).
    if (ev.key === 'Enter') translateHello();
  });
});
