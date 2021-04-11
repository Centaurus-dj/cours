<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../../Javascript/css/master.css">
  <title>PHP - Exemple 3</title>
</head>

<body>
  <div id="get-back">
    <a class="back-link" href="../index.php">Return</a>
  </div> <br>
  <h1>PHP - Exemple 3</h1>
  <?php
  // les variables existent-t-elles ?
  if (isset($_GET['nom']) and isset($_GET['prenom'])) { // oui, les variables existent
    $name = $_GET['nom'];
    $surname = $_GET['prenom'];
    //echo "<p>Bonjour $surname $name</p>";
    echo "<p>Bonjour $surname $name</p>";
  } else {
    echo "<p>Bonjour Madame ou Monsieur. </p>";
  }
  ?>
</body>

</html>