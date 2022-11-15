<?php

$uname1 = $_POST['Username'];
$email  = $_POST['Password'];




if (!empty($Username) || !empty($Password)) )
{

$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "projects";



// Create connection
$conn = new mysqli ($host, $Username, $Password);

if (mysqli_connect_error()){
  die('Connect Error ('. mysqli_connect_errno() .') '
    . mysqli_connect_error());
}
else{
  $SELECT = "SELECT Username From login Where  Username = ? Limit 1";
  $INSERT = "INSERT Into login (Username,Password )values(?,?)";

//Prepare statement
     $stmt = $conn->prepare($SELECT);
     $stmt->bind_param("s", $Username);
     $stmt->execute();
     $stmt->bind_result($Username);
     $stmt->store_result();
     $rnum = $stmt->num_rows;

     //checking username
      if ($rnum==0) {
      $stmt->close();
      $stmt = $conn->prepare($INSERT);
      $stmt->bind_param("ssss", $Username1,$Password);
      $stmt->execute();
      echo "New record inserted sucessfully";
     } else {
      echo "Someone already register using this email";
     }
     $stmt->close();
     $conn->close();
    }
} else {
 echo "All field are required";
 die();
}
?>