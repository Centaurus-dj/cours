<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PHP - Exercice 4</title>
  <link rel="stylesheet" href="../../../Javascript/css/master.css">
</head>

<body class="dark-bg">
  <div id="get-back">
    <a class="back-link" href="../index.php">Return</a>
  </div> <br>
  <h1> PHP - Exercice 4 </h1>
  <?php
  $method = $_GET["method"];
  // GET METHOD
  $fget = $_GET["nbr"];
  $sget = $_GET["nbr2"];
  $oget = $_GET["operation"];
  // POST METHOD
  $fpost = $_POST["nbr"];
  $spost = $_POST["nbr2"];
  $opost = $_POST["operation"];
  if ($method == "GET") { //TODO: Work over variables scope to find a way to optimize this.
    if (isset($fget) and isset($sget) and !isset($oget)) {
      $result = $fget + $sget;
      echo "<p>la somme de $fget et $sget est $result</p>";
    } else if (isset($fget) and isset($sget) and isset($oget)) {
      if ($oget == '+') {
        $result = $fget + $sget;
        echo "<p>la somme de $fget et $sget est $result</p>";
      } else if ($oget == '-') {
        $result = $fget - $sget;
        echo "<p>la différence de $fget et $sget est $result</p>";
      } else if ($oget == '*') {
        $result = $fget * $sget;
        echo "<p>le produit de $fget et $sget est $result</p>";
      } else if ($oget == "/") {
        $result = $fget / $sget;
        echo "<p>le quotient de $fget et $sget est $result</p>";
      }
    } else {
      echo "<p>Something went wrong, please report this incident.</p>";
    }
  } else if ($method == "POST") { //TODO: Work over variables scope to find a way to optimize this.
    if (isset($fpost) and isset($spost) and !isset($opost)) {
      $result = $fpost + $spost;
      echo "<p>la somme de $fpost et $spost est $result</p>";
    } else if (isset($fpost) and isset($spost) and isset($opost)) {
      if ($opost == '+') {
        $result = $fpost + $spost;
        echo "<p>la somme de $fpost et $spost est $result</p>";
      } else if ($opost == '-') {
        $result = $fpost - $spost;
        echo "<p>la différence de $fpost et $spost est $result</p>";
      } else if ($opost == '*') {
        $result = $fpost * $spost;
        echo "<p>le produit de $fpost et $spost est $result</p>";
      } else if ($opost == "/") {
        $result = $fpost / $spost;
        echo "<p>le quotient de $fpost et $spost est $result</p>";
      }
    } else {
      echo "<p>Something went wrong, please report this incident.</p>";
    }
  } else {
    echo "
      <form action=\"php-exercise-4.php\" method=\"post\">
      <label for=\"nbr\">Nombre n°1:</label>
      <input type=\"text\" name=\"nbr\" value=\"5\" onclick=\"document.getElementsByName('nbr')[0].value = '';\">
      <div> et </div>
      <label for=\"nbr2\">Nombre n°2:</label>
      <input type=\"text\" name=\"nbr2\" value=\"7\" onclick=\"document.getElementsByName('nbr2')[0].value = '';\"> <br>
      <label for=\"operation\">Opération à éffectuer:</label>
      <input type=\"text\" name=\"operation\" value=\"+\" onclick=\"document.getElementsByName('operation')[0].value = '';\"><button onclick=\"operations = ['+', '-', '*', '/']; document.getElementsByName('operation')[0].value = operations[Math.floor(Math.random() * operations.length)];\"> Choisir aléatoirement l'opération</button> <br>
      <input type=\"submit\" value=\"Valider\">
      </form>";
  }
  ?>
</body>

</html>