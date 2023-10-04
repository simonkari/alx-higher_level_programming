'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    if (!$('header').hasClass('red')) {
      // Add the class "red" to the header element
      $('header').addClass('red');
    }
  });
});
