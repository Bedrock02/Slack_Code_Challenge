$(document).ready(function(){
  $('#getHtmlButton').on('click', function(event) {
    event.preventDefault()
    url = $(event.target.parentElement).find('input').val()
    window.location.href = "/?query=" + url
  });
});