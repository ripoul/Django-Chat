$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});

function checkPasswordMatch() {
	var password = $("#password1").val();
	var confirmPassword = $("#confirm-password").val();

	console.log(password);
	console.log(confirmPassword);

	if (password != confirmPassword){
		$("#divCheckPasswordMatch").html("Passwords do not match!");
		document.getElementById('register-submit').disabled = true;
	}
	else{
		$("#divCheckPasswordMatch").html("Passwords match.");
		document.getElementById('register-submit').disabled = false;
	}
}
