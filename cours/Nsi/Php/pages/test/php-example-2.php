<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../../Javascript/css/master.css">
  <title>Example 2 - PHP</title>
</head>

<body class="dark-bg">
  <div id="get-back">
    <a class="back-link" href="../index.php">Return</a>
  </div> <br>
  <h1>PHP - Example 2</h1>
  <table border="1">
    <tr>
      <?php
      for ($i = 1; $i <= 10; $i = $i + 1) // ou ($i=1;$i<=10;$i++)
      {
        echo "<td>$i</td>";
      }
      ?>
    </tr>
  </table>

  <p></p>
  <table border="2">
    <tr>
      <?php
      $i = 1;
      while ($i <= 10) {
        echo "<td>$i</td>";
        $i = $i + 1;
      }
      ?>
    </tr>
  </table>
</body>

</html>