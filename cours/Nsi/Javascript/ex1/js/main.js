// Hub Functions
function toggleLinksBehaviour () { // Toggle document cookie for the behaviour of opening a link in site
  if (getCookie('link') == 'new') {
    setCookie('link', 'current', 365); // Toggle to current tab for opening a link
  } else if (getCookie('link') == 'current') {
    setCookie('link', 'new', 365); //  Toggle to new tab for opening a link
  }
  writeValue(getCookie('link'), 'link-behaviour'); // Create output of changement
}
// Exercises Functions
// Example lesson 1
function simpleAlert () { // Is ther really any use of writing anything?
  alert('Bonjour à la classe de première NSI');
}
// Exercise 1
function simpleParsing () { // We parse floats, really easy, not needed to be commented
  var a = parseFloat(prompt('Donnez un nombre'));
  var b = parseFloat(prompt('Donnez un autre nombre'));
  var produit = a * b;
  var somme = a + b;
  if (isNaN(a) && isNaN(b)) {
    alert('Les deux nombres n\'ont pas étés rentrés');
  } else if (isNaN(a) || isNaN(b)) {
    alert('Un nombre n\'a pas été rentré');
  } else {
    alert('le produit de ' + a + ' et ' + b + ' est ' + produit + ', et la somme est ' + somme);
  }
}
// Exercise 2
function pythagoreFunc (input1Id, input2Id) {
  var ab = parseFloat(document.getElementById(input1Id).value); // ab given value
  var ac = parseFloat(document.getElementById(input2Id).value); // ac given value
  var bcSquare = ab ** 2 + ac ** 2; // Squared bc value
  var bc = Math.sqrt(ab ** 2 + ac ** 2); // Squared root value of Squared bc

  console.log(ab, ac); // Debug use, can comment after not needed anymore
  console.log(bcSquare + ' = ' + bc); // Debug use, can comment after not needed anymore
  return bc; // return bc value
}
// Exercise 4
function guessNumber () { // TODO: Create version for when DOM elem not present in document
  var guessValue = window.guessValue; // get value the user will need to guess
  var input = document.getElementById('guess-input').value; // get value the user entered
  console.log('Value to guess:', guessValue); // Debug use, can comment after not needed anymore
  var body = document.getElementById('return-info'); // get document DOM element for printing output
  if (input != '') {
    if (input > guessValue) { // when it's greater than the value to guess
      body.innerText = 'The number to guess is less than ' + input + ' (entered: ' + input + ')';
    } else if (input < guessValue) { // when it's lesser than the value to guess
      body.innerText = 'The number to guess is greater than ' + input + ' (entered: ' + input + ')';
    } else { // when it's the value to guess
      body.innerText = 'The number to guess is exactly ' + guessValue + ' (entered: ' + input + ')';
    }
  } else { // when user didn't entered anything
    body.innerText = 'You haven\'t entered a guess';
  }
  console.log('return-info:', body.innerText);
  console.log('input-value:', input);
}
function changeGuessNumber () { // We reset the Value of the number to guess, helps to continue to use the feature
  window.guessValue = Math.floor(Math.random() * 20); // while not needed to refresh the page
  console.clear(); // clear console for more readibility
  console.log("New Value to guess:", window.guessValue); // Debug use, can comment after not needed anymore
  document.getElementById('guess-input').value = ''; // Reset value input
  guessNumber(); // Call guessNumber() function to reset output
}
// Exercise 5
function checkStringAppearence (stringToSearch, searchString) {
  console.log('In', '"' + searchString + '"', 'we search', '"' + stringToSearch + '"'); // Debug use, can comment after not needed anymore
  var body = document.getElementById('result-check'); // We get the div where we'll be printing the result
  var x = 0; // Used to know the exact position of the apparition of the letter researched
  var r = String(stringToSearch + ' found at position: \n');
  var None = true; // Used to know if the string contains the letter we're searching for
  for (char of searchString) { // For-of loop to test each letter
    x += 1;
    if (char == stringToSearch) {
      None = false;
      console.log('Found:', char, 'at position of index', x, '(' + searchString.charAt(x - 1) + ')');
      if (body == undefined || body == null) { // Format returned content for alert statement
        r += String('- ' + (x - 1) + ' in given text. \n');
      }
      else { // FOrmat returned content for HTML div and parsing
        r = r.replace("\n", "<br>");
        r += String('- ' + (x-1) + ' in given text. <br>');
      }
    }
  }
  if (None == true) { // If the letter we're searching for isn't in the given string
    r = String('In the given text, we can\'t find any ' + stringToSearch + '.');
  }
  console.log(body);
  if (body == undefined || body == null) { // if div searched is not in the document
    alert(r); // call an alert statement
  } else {
    body.innerHTML = r; // Otherwise write the returned content
  }
}
// Example 2 lesson 1
function simpleJsInteraction (word) { // Is there really any use of writing anything?
  alert(word + ' Madame ou Monsieur');
}
// Example 3 lesson 1
function changeColour () {
  var color = document.body.style.backgroundColor; // get current background colour of document
  if (color == 'rgb(26, 26, 26)' || color == '') {
    alert('You clicked me! We change the colour to orange.'); // code of example, can be optimised for smoother experience
    document.body.style.backgroundColor = 'orange'; // change to orange background colour
  } else {
    alert('You clicked me! We change the colour to its inital state.'); // code of example, can be optimised for smoother experience
    document.body.style.backgroundColor = 'rgb(26, 26, 26)'; // change to default background colour, hexadecimal value: #1a1a1a
  }
}
// Example 4 lesson 1
function simpleSelection () {
  const selector = document.getElementById('choice');
  const myChoice = selector[selector.selectedIndex];
  alert('Vous avez choisi la valeur = ' + myChoice.value + ', soit le choix = ' + myChoice.text);
}
// Form Example lesson 1
function simpleFormInteraction () {
  var response = document.getElementById('responseId').value;

  // Conditions are doubled for the case of user entering nbr in string and not as integer
  if (response == '1' || response == 'un') {
    document.getElementById('result-area').innerHTML = 'one';
  } else if (response == '2' || response == 'deux') {
    document.getElementById('result-area').innerHTML = 'two';
  } else if (response == '3' || response == 'trois') {
    document.getElementById('result-area').innerHTML = 'three';
  } else if (response == '4' || response == 'quatre') {
    document.getElementById('result-area').innerHTML = 'four';
  } else {
    document.getElementById('result-area').innerHTML = 'Je ne comprend pas';
  }
}
// Exercise 6
function calculateQcm (divQuest1, divQuest2, divQuest3) {
  // We proceed to check if all the values are correct for next conditions
  if (divQuest1.value == undefined) { // The user didn't clicked any buttons
    alert("Vous n'avez pas choisi une des deux réponse à la question 1.");
    return; // We stop the function
  } else if (divQuest3.value == '') { // The user didn't entered anything
    alert("Vous n'avez pas entré de réponse à la question 3.");
    return; // We stop the function
  }
  if (isNaN(parseInt(divQuest3.value))) { // The user entered a string while we need a number
    alert("Vous avez entré une chaine de caractère à la question 3 alors qu'il ne faut que des nombres.");
    return; // We stop the function
  }

  // Answers picked from the user
  const valueQuest1 = divQuest1.value;
  const valueQuest2 = divQuest2.value;
  const valueQuest3 = parseInt(divQuest3.value);

  // Correct answers of Qcm
  const trueValueQuest1 = true;
  const trueValueQuest2 = 'function';
  const trueValueQuest3 = parseInt((12 - 4) ** 2);
  const reprTrueValueQuest1 = '"Vrai"';
  const reprTrueValueQuest2 = '"function"';
  const reprTrueValueQuest3 = String('"' + parseInt((12 - 4) ** 2) + '"');

  // Function related variables, we'll use them to make statistics and decide whether the user passed the Qcm or not
  var stats = {
    "quest1": false,
    "quest2": false,
    "quest3": false,
  };

  // We log the answers given by user and the correct ones in the console | Debug Use, can comment them when not anymore needed
  console.log('valueQuest1:', valueQuest1, 'trueValueQuest1:', trueValueQuest1);
  console.log('valueQuest2:', valueQuest2, 'trueValueQuest2:', trueValueQuest2);
  console.log('valueQuest3:', valueQuest3, 'trueValueQuest3:', trueValueQuest3);

  if (valueQuest1 == trueValueQuest1) {
    stats.quest1 = true;
  }
  if (valueQuest2 == trueValueQuest2) {
    stats.quest2 = true;
  }
  if (valueQuest3 == trueValueQuest3) {
    stats.quest3 = true;
  }

  if (stats.quest1 == true && stats.quest2 == true && stats.quest3 == true) {
    alert('Vous avez réussi le QCM, bravo à vous !');
  } else {
    var r = 'Vous avez échoué au QCM:\n';
    if (stats.quest1 == true) {
      r += 'Question 1: Vous avez juste \n';
    } else {
      r += String('Question 1: Vous avez faux, la réponse était ' + reprTrueValueQuest1) + '\n';
    }
    if (stats.quest2 == true) {
      r += 'Question 2: Vous avez juste \n';
    } else {
      r += String('Question 2: Vous avez faux, la réponse était ' + reprTrueValueQuest2 + '\n');
    }
    if (stats.quest3 == true) {
      r += 'Question 3: Vous avez juste \n';
    } else {
      r += String('Question 3: Vousd avez faux, la réponse était ' + reprTrueValueQuest3 + '\n');
    }
    alert(r);
  }
}

// Utils Functions
function getIdInputValue (inputId) { // Function to ease picking value of any input
  return document.getElementById(inputId).value;
}
function writeValue (variable, elemId) { // Function to write any value in an HTML element
  var body = document.getElementById(elemId);
  if (body == null) {
    console.error("Can't write in null data");
  } else {
    body.innerText = variable;
  }
}
function openLink (link) { // Function to control link openning behaviour
  value = getCookie('link');
  if (value == 'new') {
    window.open(link, '_blank');
  } else {
    window.location.href = link;
  }
}
function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function checkCookie() {
  var user = getCookie("username");
  if (user != "") {
    alert("Welcome again " + user);
  } else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) {
      setCookie("username", user, 365);
    }
  }
}


// Draw functions
function drawTriangle (ab, ac, bc, drawingSpaceId) {
  var abDraw = ab * 50;
  var acDraw = ac * 50;
  var drawingSpace = document.getElementById(drawingSpaceId);
  if (!drawingSpace.getContext) {
    console.error('Tag given isn\'t a canvas one');
    return;
  } else {console.log('drawing Space accessed');}
  var ctx = drawingSpace.getContext('2d');
  var coordsAx = 50;
  var coordsAy = 50;
  var coordsBx = coordsAx+abDraw;
  var coordsBy = coordsAy;
  var coordsCx = coordsAx;
  var coordsCy = coordsAy + acDraw;
  var dataxDist = coordsBx + 100;
  drawingSpace.width = innerWidth;
  drawingSpace.height = innerHeight;

  console.log("width:", innerWidth + ", height:", innerHeight);
  console.log("dataxDist", dataxDist);
  console.log('ab:', ab);
  console.log('ac:', ac);
  console.log('bc:', bc);


  // Clean the drawing space
  ctx.clearRect(0, 0, drawingSpace.width, drawingSpace.height);

  // Set line stroke and line width
  ctx.strokeStyle = 'white';
  ctx.lineWidth = 5;

  // Draw triangle
  //  A     B
  //
  //  C
  ctx.beginPath();
  ctx.moveTo(coordsAx - ctx.lineWidth/2, coordsAy);
  ctx.lineTo(coordsBx, coordsBy);
  ctx.lineTo(coordsCx, coordsCy);
  ctx.lineTo(coordsAx, coordsAy);
  ctx.stroke();
  ctx.closePath();

  // Draw data about segments
  ctx.font = "20px Georgia";
  ctx.fillStyle = "white";
  ctx.fillText('ab:' + ab + ' cm', dataxDist, 50);
  ctx.fillText('ac:' + ac + ' cm', dataxDist, 80);
  ctx.fillText('bc:' + bc + ' cm', dataxDist, 110);
}
guessValue = Math.floor(Math.random() * 20);
setCookie('link', 'new', 365);