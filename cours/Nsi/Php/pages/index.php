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
  <div id="back-links">
    <a class="back-link" href="../index.html">Return to Index</a>
  </div>
  <header>Un premier programme en PHP: pour les tests</header>

  <?php
  // Commentaire en php
  // Utilisation de variables, avec le signe dollard '$'
  $var1 = 5;
  $var2 = 7;
  $somme = $var1 + $var2;

  //echo permet d'afficher sur la page
  // On peut mêler du texte et dees variables
  echo "<p>La somme de $var1 et $var2 est $somme.</p>";

  $nombre1 = rand(1, 100); // rand(a, b) génère un entier aléatoire entre a et b (inclus)

  echo "<p>Le 1er nombre choisi au hasard est $nombre1.</p>";
  $nombre2 = rand(1, 100);
  echo "<p>Le 2e nombre choisi au hasard est $nombre2.</p>";

  $somme2 = $nombre1 + $nombre2;
  // On affiche la somme
  echo "<p>La somme de $nombre1 et $nombre2 est $somme2.</p>";
  ?>

  <div class="warp">
    <div class="float-left">
      <!-- EXEMPLES -->
      <ul> Exemples:
        <ul>
          - <a href="test/php-example-2.php">Exemple 2</a>
        </ul>
        <ul>
          - <a href="test/php-example-3.php?nom=Galois&prenom=Evariste">Exemple 3</a>
        </ul>
        <ul>
          - <a href="test/php-example-4-HTML.html">Exemple 4</a>
        </ul>
      </ul>
      <!-- EXERCICES -->
      <ul>Exercices:
        <ul>
          - <a href="test/php-exercise-2.php">Exercice 2</a>
        </ul>
        <ul>
          - <a href="test/php-exercise-3.php">Exercice 3</a>
        </ul>
        <ul>
          Exercice 4 Options:
          <ul>
            - <a href="test/php-exercise-4.php?method=GET&nbr=2&nbr2=2">Exercice 4</a>
          </ul>
          <ul>
            - <a href="#js-php-action" onclick="window.location.href=String('test/php-exercise-4.php?method=GET&nbr='+Math.floor(Math.random() * 20)+'&nbr2='+Math.floor(Math.random() * 20));">
              Exercice 4 | Random
            </a>
          </ul>
          <ul>
            - <a href="#js-php-action" onclick="operations = ['+', '-', '*', '/']; window.location.href=String('test/php-exercise-4.php?method=GET&nbr='+Math.floor(Math.random() * 20)+'&nbr2='+Math.floor(Math.random() * 20)+'&operation='+operations[Math.floor(Math.random() * operations.length)]);">
              Exercice 4 | All Random
            </a>
          </ul>
          <ul>
            - <a href="test/php-exercise-4.php">
              Exercice 4 | POST method
            </a>
          </ul>
        </ul>
        <ul>
          - <a href="test/php-exercise-5-sender.php">Exercice 5</a>
        </ul>
        <ul>
          - <a href="qcm/index.php?status=enter">Exercice 6 | QCM</a>
        </ul>
      </ul>
    </div>
  </div>

</body>

</html>