<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../Javascript/css/master.css">
  <title>1er Programme - tests</title>
</head>
<body class="dark-bg">
  <h1>Un premier programme en PHP: pour les tests</h1>

  <?php
    // Commentaire en php
    // Utilisation de variables, avec le signe dollard '$'
    $var1=5;
    $var2=7;
    $somme=$var1+$var2;

    //echo permet d'afficher sur la page
    // On peut mêler du texte et dees variables
    echo "<p>La somme de $var1 et $var2 est $somme.</p>";

    $nombre1 = rand(1, 100); // rand(a, b) génère un entier aléatoire entre a et b (inclus)

    echo "<p>Le 1er nombre choisi au hasard est $nombre1.</p>";
    $nombre2 = rand(1, 100);
    echo "<p>Le 2e nombre choisi au hasard est $nombre2.</p>";

    $somme2 = $nombre1+$nombre2;
    // On affiche la somme
    echo "<p>La somme de $nombre1 et $nombre2 est $somme2.</p>";
  ?>

</body>
</html>