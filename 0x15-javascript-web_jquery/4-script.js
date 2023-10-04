'use strict';
$(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      if (!$('header').hasClass('green')) {
        $('header').addClass('green');
      }
    // If the <header> element has the class "green" (but not "red").
    } else if ($('header').hasClass('green')) {
      // Remove the class "green."
      $('header').removeClass('green');
      if (!$('header').hasClass('red')) {
        $('header').addClass('red');
      }
    } else {
      // Add the class "red" to the <header> element.
      $('header').addClass('red');
    }
  });
});
