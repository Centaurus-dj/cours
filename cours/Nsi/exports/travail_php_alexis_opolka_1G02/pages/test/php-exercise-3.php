<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../css/master.css">
  <title>PHP - Exerice 3</title>
</head>

<body class="dark-bg">
  <div id="get-back">
    <a class="back-link" href="../index.php">Return</a>
  </div> <br>
  <?php
  function arrayRange(array $input_array)
  {
    $tsum = 0;
    foreach ($input_array as $elem) {
      $tsum += $elem;
    }
    $r = $tsum / count($input_array);
    return $r;
  }

  $l = array();
  echo "<button onclick=\"document.getElementById('nbrs-created').classList.toggle('d-none')\">Afficher log de création</button>
    <div id='nbrs-created' class='d-none' style='height:300px; overflow:auto;'>";
  for ($x = 1; $x <= 100; $x++) {
    global $l;
    $nbr = rand(0, 100);
    $l = array_pad($l, $x, $nbr);
    echo "Nbr n°$x: $nbr <br>";
  }
  $l_count = count($l);
  echo "</div> <br>";
  echo "<button onclick=\"document.getElementById('array-show').classList.toggle('d-none')\">Afficher tableau entier</button>
  <div id='array-show' class='d-none'>
    <h4>Size: $l_count</h4>
    <h4>Array:  </h4>";
  print_r($l);
  echo "</div> <br>";
  echo "<h4>La moyenne des nombres est: ";
  echo arrayRange($l);
  echo "</h4>";
  ?>
</body>

</html>