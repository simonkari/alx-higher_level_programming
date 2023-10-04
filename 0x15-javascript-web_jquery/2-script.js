'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    // Change the text color of the header to red
    $('header').css('color', '#FF0000');
  });
});
