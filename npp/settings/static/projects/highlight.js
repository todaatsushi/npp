jQuery(function($) {
  $(document).ready(function($) {
    // Get & highlight current project
    // Get current project from url
    let url = document.location.href;
    url = decodeURIComponent(url.split('/')[3]);

    $('.project-links').each(function(i, v) {
      if ($(this).html() == url) {
        $(this).css("font-style", "italic");
      }
    });
  });
});
