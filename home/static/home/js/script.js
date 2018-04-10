$(document).ready(function(){
    
    
    $(".photo_gallery").mouseenter(function() {
    $(this).children(".photo_list_content").fadeIn(1000);
    });
    
    $(".photo_gallery").mouseleave(function() {
	    $(".photo_list_content").fadeOut(1);
    });
    
    
    
    $('.specific_photo').scroll(function() { 
        $('.full_picture').animate({top:$(this).scrollTop()});
    });
    
   
});

