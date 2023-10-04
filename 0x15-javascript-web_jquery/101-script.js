'use strict';
$(() => {
   // This part of the code adds a click event
   //listener to a <div> element with the id
   //"add_item" using jQuery.
  $('DIV#add_item').click(() => {
    // Find the last child element within the unordered list 
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    const lastEl = $('UL.my_list').children().last();
    if (lastEl) {
      lastEl.remove();
    }
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
