<?php
include('connection.php');
$phone_number = $_POST['phone_number'];
$psw = $_POST['psw'];

//to prevent from mysqli injection  
$phone_number = stripcslashes($phone_number);
$psw = stripcslashes($psw);
$phone_number = mysqli_real_escape_string($con, $phone_number);
$psw = mysqli_real_escape_string($con, $psw);

$sql = "select * from project where phone_number = '$phone_number' and password = '$psw'";
$result = mysqli_query($con, $sql);
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
$count = mysqli_num_rows($result);

if ($count == 1) {
    echo "<h1><center> Login successful </center></h1>";
} else {
    echo "<h1> Login failed. Invalid username or password.</h1>";
}
?>