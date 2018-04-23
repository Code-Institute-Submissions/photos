$(document).ready(function(){
    
    
    $(".photo_gallery").mouseenter(function() {
    $(this).children(".photo_list_content").fadeIn(1);
    });
    
    $(".photo_gallery").mouseleave(function() {
	    $(".photo_list_content").fadeOut(1);
    });
    
    
    $(".photo_gallery").mouseenter(function() {
        $(this).children(".ratings").fadeIn(1);
    });
    
    $(".photo_gallery").mouseleave(function() {
	    $("ratings").fadeOut(1);
    });
    
     $(".circles").hover(function() {
        let x = 1;
        let y = $(this).attr('id');
        let z = parseInt(y) + 1;
        for(x; x <= y; x++) {
        $(".c"+x).css("background-color", "#80ff80");
        $(".c"+x).css("color", "green");
        }
        for(z; z <= 5; z++) {
        $(".c"+z).css("background-color", "white");
        $(".c"+z).css("color", "dimgray");
        }
        
    });

});

