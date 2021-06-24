<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../css/master.css">
  <title>Document</title>
</head>

<body class="dark-bg">

  <header class="warp">
    <div class="float-left">
      <a class="back-link" href="../index.php">Return</a>
    </div>
    <div class="float-center">QCM</div>
  </header>
  <?php
  // Func to control if var is set or not, optimize use of built-in functions
  function controlSet(string $var, string $typeRequest, mixed $elseValue=null): mixed {
    if ($typeRequest == "get") { // var sent by GET method
      if (isset($_GET[$var])) {
        return $_GET[$var];
      } else {
        return $elseValue;
      }
    } else if ($typeRequest == "post") { // var sent by POST method
      if (isset($_POST[$var])) {
        return $_POST[$var];
      } else {
        return $elseValue;
      }
    } else if ($typeRequest == "both") {
      if (isset($_GET[$var])) { // Firstly check if given using URL
        return $_GET[$var];
      } else if (isset($_POST[$var])) { // Else check if given using POST method
        return $_POST[$var];
      } else { // If none works, return null value
        return $elseValue;
      }
    } else { // If other or none argument given, return null value
      return $elseValue;
    }
  }

  // Func to control output of a var, if equal to a non-existing output create one to recognize state of var
  function getOutputOf(mixed $variable): mixed {
    // TODO: Find a better method of returning a string, maybe using a constructor. | Needs further research
    if (is_null($variable)) {
      return "null";
    } else if ($variable == "") {
      return "empty";
    } else {
      return "$variable";
    }
  }

  // Func to create a readable layout of arrays
  function getArrayLayout(array $array): string {
    $htmlBreakElement = "<br />";
    $r = "{ $htmlBreakElement";
    foreach ($array as $key => $value) {
      $r = "$r". "<div class=\"indent-left\">". "[$key] => $value". $htmlBreakElement. "</div>";
    }
    $r = "$r }";
    return $r;
  }

  // Func to create conditions, easier to control special cases
  function isEqualTo(mixed $variable, mixed $value): bool {
    if (is_array($value)) {
      foreach ($value as $key => $inDepthValue) {
        if ($variable == $inDepthValue) {
          return true;
        }
      } return false;
    } else {
      if ($variable == $value) {
        return true; // If condition true, return true
      } else {
        return false; // Otherwise, return false
      }
    }
  }

  // Func to create conditions where we have different possibilities of values, in particular arrays used as named arrays
  function inDictArray(string|int $valueWanted, array $localArray): bool{
    $keysArray = array_keys($localArray);
    $arrayLength = count($keysArray);
    $indexedArray = array();

    for ($x = 0; $x < $arrayLength; $x ++){ // Create indexed array
      array_push($indexedArray, $localArray[$keysArray[$x]]);
    }
    for ($x = 0; $x < $arrayLength; $x ++){
      $tempValue = $indexedArray[$x];
      $outValue = $tempValue;
      if (is_array($tempValue)) {
        $outValue = getArrayLayout($tempValue);
        foreach ($tempValue as $key => $value) {
          $tempValue = $value;
        }
      }
      if (isEqualTo($valueWanted, $tempValue)) {
        return true;
      }
      echo "(Array) element n°" . $x + 1 . ": $outValue <br />";
    }
    return false;
  }

  $status = controlSet("status", "get");

  if ($status == "enter" | $status == null) {
    // If we access file for the 1st time

    echo "
    <div>
      <form action=\"index.php?status=end\" method=\"post\">

        <label for=\"radio-one\">Qu'est-ce que la morphine ?</label> <br> <!-- TODO: Find a better way to change value when clicking on text other than using onclick state -->
        <input class=\"indent-left\" type=\"radio\" name=\"radio-one\" id=\"rd-1\" value=\"medicine\"> <label onclick=\"document.getElementById('rd-1').checked = true;\">Un médicament</label> <br>
        <input class=\"indent-left\" type=\"radio\" name=\"radio-one\" id=\"rd-2\" value=\"trick\"> <label onclick=\"document.getElementById('rd-2').checked = true;\">Un bonbon</label> <br>
        <input class=\"indent-left\" type=\"radio\" name=\"radio-one\" id=\"rd-3\" value=\"religion\"> <label onclick=\"document.getElementById('rd-3').checked = true;\">Un mouvement religieux</label> <br>
        <br>

        <label for=\"options\">Le PHP est un langage:</label>
        <select name=\"select-one\">
            <option vlaue=\"balsitic\">Balistique</option>
            <option value=\"server\">Serveur</option>
            <option value=\"stylistic\">Stylistique</option>
        </select>

        <label for\"question-one\">Quel est le résultat de l'addition de 20 et 95 ?</label>
        <input type=\"text\" name=\"input-one\">

        <label for=\"question-two\">Quel est la signification de \"NSI\" ?</label> <br>
        <help class=\"none-txt\">Veuillez écire en minuscule, au singulier et séparé par un espace.</help>
        <input type=\"text\" name=\"input-two\">
        <input type=\"submit\" name=\"submit\" value=\"Soumettre\">
      </form>
    </div>
    ";
  } else if ($status == "end") {
    // If we access file after having completed the form
    $layout = controlSet("layout", "get", "perma");

    // controlSet new variables
    $radio1 = controlSet("radio-one", "post"); // == medicine
    $select1 = controlSet("select-one", "post"); // == server
    $input1 = controlSet("input-one", "post"); // == 115
    $input2 = controlSet("input-two", "post"); // numérique science informatique


    // getOutputOf --> In case of crossing Debugging status
    $outRadio1 = getOutputOf($radio1);
    $outSelect1 = getOutputOf($select1);
    $outInput1 = getOutputOf($input1);
    $outInput2 = getOutputOf($input2);


    // Answers dictionnary
    $validValues = array(
      "radio1" => "medicine",
      "select1" => "server",
      "input1" => 115,
      "input2" => array("numérique science informatique", "numerique science informatique"),
    );

    // Total Score
    $score = 0;

    // Definitive layout
    /// Put at start, conditions about each variables using array.
    if (isEqualTo($radio1, $validValues['radio1'])) {
      $score += 1;
      $q1Symbol = "&#9989;";
    } else {
      $q1Symbol = "&#10060;";
    }
    if (isEqualTo($select1, $validValues['select1'])) {
      $score += 1;
      $q2Symbol = "&#9989;";
    } else {
      $q2Symbol = "&#10060;";
    }
    if (isEqualTo($input1, $validValues['input1'])) {
      $score += 1;
      $q3Symbol = "&#9989;";
    } else {
      $q3Symbol = "&#10060;";
    }
    if (isEqualTo($input2, $validValues['input2'])) {
      $score += 1;
      $q4Symbol = "&#9989;";
    } else {
      $q4Symbol = "&#10060;";
    }

    // Temporary layout
    if (isEqualTo($layout, "temp")) {
      echo "
      <h2>Status has been found as : $status</h2>
      <h3>
        <a href=\"index.php?status=enter\">Toggle init state</a>,
        <a href=\"index.php?status=end\">Toggle current state</a>,
        <a href=\"index.php?status=error\">Toggle error state</a>,
        <a href=\"index.php?status=end-debug&radio-one=$outRadio1&select-one=$outSelect1&input-one=$outInput1&input-two=$outInput2\">Toggle end-debug state</a> <br>
        <a href=\"https://gitlab.com/CentaurusDj/import-cours/\">Access Repo</a>
      </h3>
      <p>Next comes test of function:</p>
      ";
      echo inDictArray("numérique science informatique", $validValues);
    } else {
      echo "
      <h1>Votre score est de: $score</h1>
      <p><a id=\"correction-link\" href=\"javascript:void()\" onclick=\"document.getElementById('correction-container').classList.toggle('d-none'); document.getElementById('correction-link').classList.add('d-none');\">Voir correction</a></p>
      <div id=\"correction-container\" class=\"d-none\">
        <ul>
          <ul>Question 1: medicine $q1Symbol</ul>
          <ul>Question 2: server $q2Symbol</ul>
          <ul>Question 3: 115 $q3Symbol</ul>
          <ul>Question 4: ". getArrayLayout($validValues['input2']) . "$q4Symbol</ul>
        </ul>
      </div>

      <script>
        var separation = document.createElement('txt');
        var refreshPage = document.createElement('a');
        var pointedDiv = document.getElementsByClassName('float-left')[0];

        separation.innerHTML = '/';
        refreshPage.classList.add('back-link');
        refreshPage.innerText = 'Refresh';
        refreshPage.href = 'index.php';

        pointedDiv.appendChild(separation);
        pointedDiv.appendChild(refreshPage);
      </script>
      ";
    }
  } else if($status == "end-debug"){
    $radio1 = controlSet("radio-one", "get"); // == medicine
    $select1 = controlSet("select-one", "get"); // == server
    $input1 = controlSet("input-one", "get"); // == 115
    $input2 = controlSet("input-two", "get"); // numérique science informatique

    echo "
    <h2>Debug End:</h2>
    <ul>
      <ul>Status: $status</ul>
      <ul>radio1: $radio1</ul>
      <ul>select1: $select1</ul>
      <ul>input1: $input1</ul>
      <ul>input2: $input2</ul>
    </ul>
    <script>
      var separation = document.createElement('txt');
      var refreshPage = document.createElement('a');
      var pointedDiv = document.getElementsByClassName('float-left')[0];

      separation.innerHTML = '/';
      refreshPage.classList.add('back-link');
      refreshPage.innerText = 'Refresh';
      refreshPage.href = 'index.php';

      pointedDiv.appendChild(separation);
      pointedDiv.appendChild(refreshPage);
    </script>
    ";
  } else {
    echo "<h1>Oh! Something went wrong, please report this incident at <a href=\"https://gitlab.com/CentaurusDJ/import-cours/-/issues\">Repository Issues</a>.</h1>";
  }

  ?>

</body>

</html>