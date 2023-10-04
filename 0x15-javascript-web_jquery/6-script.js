'use strict';
$(() => {
  $('DIV#update_header').click(() => {
    // and updates to 'New Header!!!'.
    $('header').text('New Header!!!');
  });
});
