$(document).ready(function () {

    // Active class changer

    var currentActive = $(".nav-link").eq(1);
    //console.log($(currentActive).html());

    $(".nav-link").on("click", function ( e ) {
        //alert($(this).html()); 
        $(currentActive).removeClass("active");

        currentActive = this;
        //console.log(currentActive);
        $(currentActive).addClass("active");

        $(currentActive).data("targetId");
        var targetId = $(currentActive).data("scrollid");


        var target = $("#" + targetId);
        //console.log(target.html());

        

        var navbarheight =  $(".navbar").css("height");
        //console.log(navbarheight);
        navbarheight = navbarheight.slice(0, (navbarheight.length-2));
        navbarheight = parseInt(navbarheight) + 10; //extra 10 for extra space in when scrolling  
        //console.log(navbarheight);


        e.preventDefault()
        $('html,body').animate({
            scrollTop: target.offset().top - navbarheight
        }, 500);


        
        
    })


});