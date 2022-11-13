$(document).on('ready', function() {
	$("body").on("click", "#addTocart", function(event){
		var id = $(this).attr("data-book-id");
		event.preventDefault();
		$.ajax({
			url : "../cart/add/"+id,
			data : {bookid:1},
			success : function(data){

				$("#snackbar").html("Add To Cart");
				var x = document.getElementById("snackbar");
				x.className = "show";
				setTimeout(function(){ x.className = x.className.replace("show", ""); }, 1000);
				totalCart();
			}
		})
	});


	$('#demo3').skdslider({
		delay:2000,
		animationSpeed: 1000,
		showNextPrev:true,
		showPlayButton:true,
		autoSlide:true,
		animationType:'fading'
	});

	$('#stars li').on('mouseover', function(){
		var onStar = parseInt($(this).data('value'), 10); 
	   
		$(this).parent().children('li.star').each(function(e){
		  if (e < onStar) {
			$(this).addClass('hover');
		  }
		  else {
			$(this).removeClass('hover');
		  }
		});
	  }).on('mouseout', function(){
		$(this).parent().children('li.star').each(function(e){
		  $(this).removeClass('hover');
		});
	  });
	  
	$('#stars li').on('click', function(){
		var onStar = parseInt($(this).data('value'), 10); 
		var stars = $(this).parent().children('li.star');
		
		for (i = 0; i < stars.length; i++) {
		  $(stars[i]).removeClass('selected');
		}
		for (i = 0; i < onStar; i++) {
		  $(stars[i]).addClass('selected');
		}
		var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
		var msg = "";
		if (ratingValue > 1) {
			msg = ratingValue;
		}
		else {
			msg = ratingValue;
		}
		responseMessage(msg);
	}); 
	function responseMessage(msg) {
		document.getElementById("id_review_star").value = msg;
	}	

	  $('.responsive').slick({
	  dots: false,
	  infinite: true,
	  speed: 300,
	  autoplay:true,
	  autoplaySpeed:1500,
	  slidesToShow: 11,
	  slidesToScroll: 11,
	  responsive: [
		{
		  breakpoint: 1200,
		  settings: {
			slidesToShow: 3,
			slidesToScroll: 3,
			infinite: true,
			dots: false
		  }
		},
		{
		  breakpoint: 1000,
		  settings: {
			slidesToShow: 8,
			slidesToScroll: 8
		  }
		},
		{
		  breakpoint: 800,
		  settings: {
			slidesToShow: 6,
			slidesToScroll: 6
		  }
		},
		{
		  breakpoint: 600,
		  settings: {
			slidesToShow: 4,
			slidesToScroll: 4
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 2
		  }
		}
		]
	});
	  
	  $('.regulara').slick({
	  dots: false,
	  infinite: false,
	  speed: 300,
	  slidesToShow: 4,
	  slidesToScroll: 4,
	  responsive: [
		{
		  breakpoint: 1200,
		  settings: {
			slidesToShow: 3,
			slidesToScroll: 3
		  }
		},
		{
		  breakpoint: 950,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 2
		  }
		}
		]
	});
	  
    $(window).on('load', function() {
        $('.pre_loader').fadeOut('slow');
        $('.pre_loader').remove('slow');
    });  

});

function totalCart(){
	$.ajax({
		url: "../cart/totalcart",
		success: function(data){
			$("#gettotalcart").html(data);
			console.log(data)
		}
	})
}


$("input[name='qty']").TouchSpin({
	min: 1,
	max: 10,
	verticalbuttons: false
});
$('article').readmore({speed: 500});



