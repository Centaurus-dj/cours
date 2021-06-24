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
    <a class="back-link" href="../index.php">Return</a> <br>
    <div class="back-link" style="margin-left: 20px;">ou</div>
    <a class="back-link" href="php-exercise-5-sender.php"> Return Sender</a>
  </div> <br>
  <h1> PHP - Exercice 5, Receuveur </h1>
  <?php
  $sent_nbr = $_GET["nbr"];
  if (isset($sent_nbr)) {
    $sqrt_nbr = sqrt($sent_nbr);
    if (!is_nan($sqrt_nbr)) {
      echo "La racine caré de $sent_nbr est $sqrt_nbr.";
    } else {
      echo "On ne peut pas avoir la racine carré de $sent_nbr.";
    }
  } else {
    echo "Something went wrong, we coudln't GET the wanted argument.";
  }
  ?>
</body>

</html>