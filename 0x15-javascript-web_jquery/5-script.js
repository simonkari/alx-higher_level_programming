'use strict';
$(() => {
  $('DIV#add_item').click(() => {
    // Create a new <li> element using the plain JavaScript
    const newItem = document.createElement('li');

    newItem.textContent = 'Item';
    // using jQuery's `append` method.
    $('UL.my_list').append(newItem);
  });
});
