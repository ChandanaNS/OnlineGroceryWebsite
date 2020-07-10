$(document).ready(function(){
	$('#fresh-arrow-click').click(function(){
		console.log('fresh level');
		$('#fresh-checkboxes').fadeToggle(400);
		$('#workout-checkboxes').hide();
		$('#trainer-checkboxes').hide();
	})
	$('#breakfast-arrow-click').click(function(){
		console.log('workout type');
		$('#fresh-checkboxes').hide();
		$('#workout-checkboxes').fadeToggle(400);
		$('#trainer-checkboxes').hide();
	})
	$('#beverages-arrow-click').click(function(){
		console.log('trainer level');
		$('#fresh-checkboxes').hide();
		$('#workout-checkboxes').hide();
		$('#trainer-checkboxes').fadeToggle(400);
	})

	if ('input[type=checkbox]:checked') {
		$()
	}

    // if checkbox is checked, show corresponding text with option to X out and delete text and uncheck checkbox
	$('input[type="checkbox"]').change(function () {
        var checkboxname = $(this).val();
        	console.log(this.value);
        if ($(".display").hasClass(checkboxname)) {
            if ($(this).is(":checked")) {
                $(".display." + checkboxname).show();
                $('.clearall').show();
            } else {
                $(".display." + checkboxname).hide();
            }
        }

        $('#close-all').click(function() {
		 	// $('input[type="checkbox"]').empty();
		 	$('input[type=checkbox]').each(function() { this.checked = false; });
		 	$('.display.' + checkboxname).hide();
		 	$('.clearall').hide();
		 	$('#fresh-checkboxes').hide();
			$('#workout-checkboxes').hide();
			$('#trainer-checkboxes').hide();

		});


    });

})