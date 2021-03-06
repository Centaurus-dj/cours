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
    <a class="back-link" href="../index.php">Return to index</a> <br>
    <a class="back-link" href="php-exercise-4.php">Refresh Page</a>
  </div> <br>
  <h1> PHP - Exercice 4 </h1>
  <?php
  function controlSet($var, $type_request) {
    if ($type_request == "get") {
      if (isset($_GET[$var])) {
        return $_GET[$var];
      } else {
        return null;
      }
    } else if ($type_request == "post") {
      if (isset($_POST[$var])) {
        return $_POST[$var];
      } else {
        return null;
      }
    } else if ($type_request == "both") {
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
  $fget = controlSet("nbr", "get"); // first with GET
  $sget = controlSet("nbr2", "get"); // second with GET
  $oget = controlSet("operation", "get"); // operation with GET
  // POST METHOD
  $fpost = controlSet("nbr", "post"); // first with POST
  $spost = controlSet("nbr2", "post"); // second with POST
  $opost = controlSet("operation", "post"); // operation with POST

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
    echo '
    <div id="php-outer-choice-container" class="center-txt medium-txt">
      <div class="alert-box">
        <span class="closebtn" onclick="this.parentElement.style.display=\'none\';">&times;</span>
        The random button for operation may cause unwanted behaviour, please do not use it.
      </div> <br>
      <div id="quest-div">Which form to use?</div> <br>
      <div id="res-div">
        <div id="post-res">
          - <a href="javascript:void" onclick="var div1=document.getElementById(\'post-form-container\'); var div2=document.getElementById(\'quest-div\'); var div3=document.getElementById(\'res-div\'); div1.classList.toggle(\'d-none\'); div2.classList.toggle(\'d-none\'); div3.classList.toggle(\'d-none\');">Post form</a>
        </div>
        or
        <div id="get-res">
          - <a href="javascript:void" onclick="var div1=document.getElementById(\'get-form-container\'); var div2=document.getElementById(\'quest-div\'); var div3=document.getElementById(\'res-div\'); div1.classList.toggle(\'d-none\'); div2.classList.toggle(\'d-none\'); div3.classList.toggle(\'d-none\');">Get form</a>
        </div>
      </div>
      <div id="forms-container">
        <div id="get-form-container" class="d-none">
          <form action="php-exercise-4-part2.php" method="get">
            <label for="nbr">Nombre n°1:</label>
            <input type="text" name="nbr" value="5" onclick="document.getElementsByName(\'nbr\')[0].value = \'\';">
            <div> et </div>
            <label for="nbr2">Nombre n°2:</label>
            <input type="text" name="nbr2" value="7" onclick="document.getElementsByName(\'nbr2\')[0].value = \'\';"> <br>
            <label for="operation">Opération à éffectuer:</label>
            <input type="text" name="operation" value="+" onclick="document.getElementsByName(\'operation\')[0].value = \'\';">
            <button onclick="operations = [\'+\', \'-\', \'*\', \'/\']; document.getElementsByName(\'operation\')[0].value = operations[Math.floor(Math.random() * operations.length)];"> Choisir aléatoirement l\'opération</button> <br>

            <!-- Hidden input to set the method -->
            <input type="text" name="method" value="get" class="d-none">

            <input type="submit" value="Valider">
          </form>
        </div>
        <div id="post-form-container" class="d-none">
          <form action="php-exercise-4-part2.php" method="post">
            <label for="nbr">Nombre n°1:</label>
            <input type="text" name="nbr" value="5" onclick="document.getElementsByName(\'nbr\')[1].value = \'\';">
            <div> et </div>
            <label for="nbr2">Nombre n°2:</label>
            <input type="text" name="nbr2" value="7" onclick="document.getElementsByName(\'nbr2\')[1].value = \'\';"> <br>
            <label for="operation">Opération à éffectuer:</label>
            <input type="text" name="operation" value="+" onclick="document.getElementsByName(\'operation\')[1].value = \'\';">
            <button onclick="operations = [\'+\', \'-\', \'*\', \'/\']; document.getElementsByName(\'operation\')[1].value = operations[Math.floor(Math.random() * operations.length)];"> Choisir aléatoirement l\'opération</button> <br>
            <!-- Hidden input to set the method -->
            <input type="text" name="method" value="post" class="d-none">
            <input type="submit" value="Valider">
          </form>
        </div>
      </div>
    </div>
    ';
  }
  ?>
</body>

</html>