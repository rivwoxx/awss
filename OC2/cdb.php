<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

<?php
    $db_h ="localhost";
    $db_nom ="prueba";
    $db_usr ="pepe";
    $db_pss ="wer";
    
    $conect = mysqli_connect($db_h,$db_usr,$db_pss);

    /* check connection */ 
if (mysqli_connect_errno()) { 
    printf("Connect failed: %s\n", mysqli_connect_error()); 
    exit(); 
} 
    $database = mysqli_select_db($conect,$db_nom); 
 
 
?> 
<?php 
 
$result = mysqli_query($conect, "SELECT * FROM pepe"); 
 
while($query_data = mysqli_fetch_row($result)) { 
  echo "<table>"; 
  echo "<tr>"; 
  echo "<td>",$query_data[0], "</td>", 
       "<td>",$query_data[1], "</td>", 
       "<td>",$query_data[2], "</td>"; 
  echo "</tr>"; 
  echo"</table>"; 
} 
?> 
 
</body> 
</html>
