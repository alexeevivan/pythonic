$(document).ready(function(){
    $(window).scroll(function(){
        $('.scroll').css("opacity", 1 - $(window).scrollTop() / 700)
    })
});


$(document).ready(function(){
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {
  
      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store hash
        var hash = this.hash;
  
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function(){
     
                // Add hash (#) to URL when done scrolling (default click behavior)
                window.location.hash = hash;
            });
        } // End if
    });
});


const hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
});


function myFunc() {
    var nav = document.getElementById("myNav")
    if (nav.style.height == '100%') {
        nav.style.height = '0';
        nav.style.opacity = 0;
      } else {
        nav.style.height = "100%";
        nav.style.opacity = 1;
      }
};