<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../css/master.css">
  <title>Exercise 2 - PHP</title>
</head>

<body class="dark-bg">
  <div id="get-back">
    <a class="back-link" href="../index.php">Return</a>
  </div> <br>
  <div class="warp">
    <div class="float-left">
      <?php
      $nbr1 = rand(1, 15);
      $multdone = 0;

      echo "<h3>Number: $nbr1</h3>";
      echo "<table border='1' spacing='5'>";
      echo "<tr><td>Multiplié par:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr>";
      echo "<tr><td>Résultat:</td>";
      while ($multdone < 10) {
        $result = $nbr1 * ($multdone + 1);
        echo "<td>$result</td>";
        $multdone += 1;
      }
      echo "</tr></table>";
      ?>
    </div>
  </div>
</body>

</html>