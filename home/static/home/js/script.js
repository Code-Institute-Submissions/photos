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
    
   

});

