<?php
session_start();

// initializing variables
$phone_number = "";
$Name = "";
$email = "";
$errors = array();

// connect to the database
$db = mysqli_connect('', '', '', '');
//mysqli_set_charset($db, "utf8");




// REGISTER USER
if (isset($_POST['reg_user'] )) {
	// receive all input values from the form
	$Name = mysqli_real_escape_string($db, $_POST['Name']);
	$phone_number = mysqli_real_escape_string($db, $_POST['phone_number']);
	$email = mysqli_real_escape_string($db, $_POST['email']);
	$psw = mysqli_real_escape_string($db, $_POST['psw']);
	$psw_repeat = mysqli_real_escape_string($db, $_POST['psw_repeat']); 

	// form validation: ensure that the form is correctly filled ...
	// by adding (array_push()) corresponding error unto $errors array


	if (empty($Name)) {
		array_push($errors, "Name is required");
	}
	if (empty($phone_number)) {
		array_push($errors, "phone number is required");
	}
	if (empty($email)) {
		array_push($errors, "Email is required");
	}
	if (empty($psw)) {
		array_push($errors, "Password is required");
	}
	if ($psw != $psw_repeat) {
		array_push($errors, "The two password do not match");
	}

	// first check the database to make sure 
	// a user does not already exist with the same username and/or email

	$user_check_query = "SELECT * FROM project WHERE phone_number='$phone_number' LIMIT 1";
	$result = mysqli_query($db, $user_check_query);
	$user = mysqli_fetch_assoc($result);

	if ($user) { // if user exists
		if ($user['phone_number'] === $phone_number) {
			array_push($errors, "phone number already exists");
			header('location: Register2.html');
		}

	}

	// Finally, register user if there are no errors in the form
	if (count($errors) == 0) {
		$password = $psw; //encrypt the password before saving in the database

		$query = "INSERT INTO project (phone_number, Name, email, password) 
  			  VALUES('$phone_number', '$Name', '$email', '$password')";
		mysqli_query($db, $query);
		$_SESSION['phone_number'] = $phone_number;
		$_SESSION['success'] = "You are now logged in";
		header('location: http://login.aj-tay.com/');
	}
}
