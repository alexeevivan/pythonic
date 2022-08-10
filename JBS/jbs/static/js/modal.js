var modal = $('#myModal'),
    span = document.getElementsByClassName("closeBtn")[0],
    overlay = document.getElementById('overlay');

$(window).on('load',function(){
    var delayMs = 0; // delay in milliseconds
    
    setTimeout(function(){
        $('#myModal').modal('show') && overlay.classList.add('active');
    }, delayMs);
});

span.onclick = function() {
    $('#myModal').modal('hide') && overlay.classList.remove('active');
}

$(window).on('click', function(e) {
    var target = $(e.target);
    if(target.is(modal)) {
        overlay.classList.remove('active');
    }
})