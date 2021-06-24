<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PHP - Exercice 5</title>
  <link rel="stylesheet" href="../../css/master.css">
</head>

<body class="dark-bg">
  <div id="get-back">
    <a class="back-link" href="../index.php">Return</a>
  </div> <br>
  <h1> PHP - Exercice 5, envoyeur </h1>
  <?php
  $send_nbr = random_int(-10, 10);
  echo "<a href='php-exercise-5-receiver.php?nbr=$send_nbr'>Passer à la deuxième page.</a>";
  ?>
</body>

</html>