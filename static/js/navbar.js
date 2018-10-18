$(function () {
  $(document).scroll(function () {
	  var $nav = $(".navbar-fixed-top");
    var $nav_brand = $(".navbar-brand")
	  $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    $nav_brand.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
	});
});
