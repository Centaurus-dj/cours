<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../../../Javascript/css/master.css">
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


  $status = controlSet("status", "get");

  if ($status == "enter") {
    // HTML Form Here
  } else if ($status == "end") {
    // ControlSet new variables
  }

  ?>

</body>

</html>