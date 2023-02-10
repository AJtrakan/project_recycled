<!DOCTYPE html>
<html>

<body>
    <form style="font-size:150%;">

        <h1 style="font-size:300%;"><center>Check point</center></h1>

        <div class="container" style="background-color:#f1f1f1">
            <?php
            include('connection.php');
            $phone_number = $_POST['phone_number'];

            //to prevent from mysqli injection  
            $phone_number = stripcslashes($phone_number);
            $phone_number = mysqli_real_escape_string($con, $phone_number);

            $sql = "select * from project where phone_number = '$phone_number' ";
            $result = mysqli_query($con, $sql);
            $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
            $count = mysqli_num_rows($result);

            if ($count == 1) {
                $sql = "select * from project where phone_number='$phone_number'";
                $result = mysqli_query($con, $sql);
                $row = mysqli_fetch_assoc($result);
                // echo "<h3>username : " . $row["phone_number"] . "</h3>";
                echo "<h1><center> My points : " . $row["Points"] . "</center></h1>";

            } else {
                echo "<h1> Login failed. Invalid username or password.</h1>";
            }
            ?>
        </div>
    </form>
</body>

</html>