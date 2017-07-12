$('.skills ul li').mouseleave(function(){
  $(this).children('span').stop().animate({
    opacity:0
  },200)
  $(this).children('tab').hide();
});

$('.skills ul li').mouseenter(function(){
  $(this).children('span').stop().animate({
    opacity:1
  },200)
  $(this).children('tab').show();
});
