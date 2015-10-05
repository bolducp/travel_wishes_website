var main = function() {
    $("h4").hover(function() {
        $(this).toggleClass("highlighted");
     });
});


$(document).ready(main);