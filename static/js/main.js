$(document).ready(function(){
  $('#getHtmlButton').on('click', function(event) {
    event.preventDefault();
    url = $(event.target.parentElement).find('input').val();
    window.location.href = "/?query=" + url;
  });

  $('.tag-anchor').on('click', function(event) {
    event.preventDefault();
    // Remove all possible active tags and highlights
    $('li.active').removeClass('active');
    $('pre').removeHighlight();
    
    // Add active menu item and highlights
    tag = event.target.name;
    tags_to_mark = ["<"+tag, "</"+tag+">", "<"+tag+">"];
    tags_to_mark.forEach(function(tag) {
      $('pre').highlight(tag);
    });
    $(event.target.parentElement).addClass('active');
  });
});