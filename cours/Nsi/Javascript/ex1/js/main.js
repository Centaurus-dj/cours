function simpleAlert(){
  alert('Bonjour à la classe de première NSI');
}
function simpleParsing(){
  var a, b, produit, somme;
  a = prompt("Donnez un nombre");
  b = prompt("Donnez un autre nombre");
  a = parseFloat(a);
  b = parseFloat(b);
  produit = a*b;
  somme = a+b;
  alert("le produit est "+ produit + ", et la somme est "+ somme)
}