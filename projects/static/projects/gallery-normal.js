// Adapted from W3 schools tutorial into jQuery
// https://www.w3schools.com/w3css/w3css_slideshow.asp

jQuery(function($) {
  // Listens for clicks on each chevron and shows the pic before/after of
  // class 'change'. Also changes counter to indicate where we are in the
  // collection.

  $(document).ready(function() {

    // Initialise starting index
    let index = parseInt($('.controls').attr('index'));

    // Pin to picture index
    $('#picture-index').html(index);

    // Define function to show & hide each image
    let showDivs = (orderToShow) => {
      // Input n defines which index of img to show, and implicitly
      // hide the rest

      // Get all items of class to hide
      let imgs = $('.change');
      let descs = $('.desc');

      // Looping mechanism
      // Reset i if i is too big
      if (orderToShow > imgs.length){
        index = 1;
      }

      // Reset i is i is too small
      if (orderToShow < 1) {
        index = imgs.length;
      }

      // Loop through all imgs and hide them
      for (let iterator = 0; iterator < imgs.length; iterator++) {
        $(imgs[iterator]).addClass('hide');
        $(descs[iterator]).addClass('hide');
      }

      // Show the one we want
      $(imgs[index-1]).removeClass('hide');
      $(descs[index-1]).removeClass('hide');
    };

    // Initialise by showing the first image
    showDivs(index);

    // Shift by given direction n
    let adjust = (step) => {
      showDivs(index += step);
      // Pin to picture index
      $('#picture-index').html(index);
    };

    // Shift back if left button is clicked
    $('#gallery-back').click(function() {
      adjust(-1);
    });

    // Shift forth if left button is clicked
    $('#gallery-next').click(function() {
      adjust(1);
    });
  });
});

jQuery(function($) {
  // Use arrow keys to navigate gallery
  $(document).keydown(function(e) {
    // Listen for key press
    if (e.which == 37) {
      // If left arrow, go back
      $('#gallery-back').trigger('click');
    } else if (e.which == 39) {
      // If right, go forth
      $('#gallery-next').trigger('click');
    }
  });
});
