<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../css/master.css">
  <title>PHP - Exemple 4 - Méthode POST Fichier PHP</title>
</head>

<body class="dark-bg">
  <div id="get-back">
    <a class="back-link" href="../index.php">Return</a>
    <div class="back-link" style="margin-left: 20px;">ou</div>
    <a class="back-link" href="php-example-4-HTML.html">Return 1st part</a>
  </div> <br>
  <h1>PHP - Exemple 4 - Méthode POST Fichier PHP</h1>
  <?php
  $npost = $_POST["nom"];
  $ppost = $_POST["prenom"];
  // les variables existent-elles ?
  if (isset($npost) and isset($ppost)) {
    //Oui les variables existent
    // echo "<p>Bonjour $ppost et $npost !</p>";
    echo "<p>Bonjour $ppost $npost !</p>";
  } else {
    echo "<p>Bonjour Madame ou Monsieur.</p>";
  }
  ?>
</body>

</html>