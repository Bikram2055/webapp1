	$(document).ready(function(){
		$('#btn').click(function(){
			var a = $('#item1').text();
			var b = $('#p1').text();
			$('.price1').text(b);
			$('.item').text(a);
			var a = parseInt($('#quan').text(), 10)
			b = parseInt(b, 10);
			$('#tot').text(a*b);
		});
	});

	$(document).ready(function(){
		$('#aa').click(function(){
			var b = $('#quan').text();
			b=parseInt(b, 10);
			b = b+1;
			$('#quan').text(b);
			var a = $('.price1').text();
			a=parseInt(a, 10);
			$('#tot').text(a*b);
		});
	});
	$(document).ready(function(){
		$('#ab').click(function(){
			var b = $('#quan').text();
			b=parseInt(b, 10);
			b = b-1;
			if (b<1){
				b=1;
			}
			$('#quan').text(b);
			var a = $('.price1').text();
			a=parseInt(a, 10);
			$('#tot').text(a*b);
		});
	});
