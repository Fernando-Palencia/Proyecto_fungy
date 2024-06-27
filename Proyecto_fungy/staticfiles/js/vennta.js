$(document).ready(function(){
    $("#miBoton").click(function(){
      $('html, body').animate({
        scrollTop: $("#miSeccion").offset().top
      }, 2000);
      $("#miSeccion").slideToggle("slow");
    });
  });