<!DOCTYPE html>
<html>

<body>
    <form style="font-size:150%;">

        <h1 style="font-size:300%;">Member</h1>

        <div class="container" style="background-color:#f1f1f1">
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
                $sql = "select * from project where phone_number='$phone_number'";
                $result = mysqli_query($con, $sql);
                $row = mysqli_fetch_assoc($result);
                echo "<h1>Username : " . $row["phone_number"] . "</h1>";
                echo "<h1>Name : " . $row["name"] . "</h1>";
                echo "<h1>E-mail : " . $row["Email"] . "</h1>";
                echo "<h1>Point : " . $row["Points"] . "</h1>";

            } else {
                echo "<h1> Login failed. Invalid username or password.</h1>";
            }
            ?>
        </div>
    </form>
</body>

</html>