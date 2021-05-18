<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PHP - Exercice 4</title>
  <link rel="stylesheet" href="../../css/master.css">
</head>

<body class="dark-bg">
  <div id="get-back">
    <a class="back-link" href="../index.php">Return to index</a> <br>
    <a class="back-link" href="php-exercise-4.php">Return to sender</a>
  </div> <br>
  <h1> PHP - Exercice 4 Part 2</h1>
  <?php
  function controlSet($var, $requestType)
  {
    if ($requestType == "get") {
      if (isset($_GET[$var])) {
        return $_GET[$var];
      } else {
        return null;
      }
    } else if ($requestType == "post") {
      if (isset($_POST[$var])) {
        return $_POST[$var];
      } else {
        return null;
      }
    } else if ($requestType == "both") {
      if (isset($_GET[$var])) {
        return $_GET[$var];
      } else if (isset($_POST[$var])) {
        return $_POST[$var];
      } else {
        return null;
      }
    } else {
      return null;
    }
  }

  $method = controlSet("method", "both");
  // GET METHOD
  $fget = controlSet("nbr", "get");
  $sget = controlSet("nbr2", "get");
  $oget = controlSet("operation", "get");
  // POST METHOD
  $fpost = controlSet("nbr", "post");
  $spost = controlSet("nbr2", "post");
  $opost = controlSet("operation", "post");

  if ($method == "GET" | $method == "get") { //TODO: Work over variables scope to find a way to optimize this.
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
  } else if ($method == "POST" | $method == "post") { //TODO: Work over variables scope to find a way to optimize this.
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
      $is1 = isset($fpost);
      $is2 = isset($spost);
      $is3 = isset($opost);

      echo "<p>Something went wrong, please report this incident.</p>
      <div id=\"php-log\">
        <txt>tested values:</txt>
        <ul>
          <elem>method: $method</elem>
          <elem>fpost: $fpost</elem>
          <elem>spost: $spost</elem>
          <elem>opost: $opost</elem>
        </ul>
        <txt>conditions:</txt>
        <ul>
          <elem>is1: $is1</elem>
          <elem>is2: $is2</elem>
          <elem>is3: $is3</elem>
        </ul>
      </div>";
    }
  } else {
    echo "
    <h1>Oh! Something went wrong, we couldn't determine which method the method is.</h1>
    ";
  }
  ?>
</body>

</html>