// Global variables
const global = {
  // Dictionary used to keep track of everything created, last resort for finding values
  str: String,
};

// Variables management Methods
export function defineVar(varName, varValue) {
  global[varName] = varValue;
  return varValue;
}
export function addVar(varName, addValue) {
  if (global[varName]) {
    if (global[varName] + addValue) {
      var sum = global[varName] + addValue;
      global[varName] = sum;
      return sum;
    } else {
      throw Error(
        `MathError: Error during addition of ${global[varName]} with ${addValue}, please ensure the operation is possible.`
      );
    }
  } else {
    throw Error(
      `DefineError: Please be sure to define the variable ${varName} using defineVar() before using addVar().`
    );
  }
}
export function minVar(varName, minValue) {
  if (global[varName]) {
    if (global[varName] - minValue) {
      var difference = global[varName] - minValue;
      global[varName] = difference;
      return difference;
    } else {
      throw Error(
        `MathError: Error during substraction of ${global[varName]} by ${minValue}, please ensure the operation is possible.`
      );
    }
  } else {
    throw Error(
      `DefineError: Please be sure to define the variable ${varName} using defineVar() before using minVar().`
    );
  }
}
export function divVar(varName, divValue) {
  if (global[varName]) {
    if (global[varName] / divValue) {
      var ratio = global[varName] / divValue;
      global[varName] = ratio;
      return ratio;
    } else {
      throw Error(
        `MathError: Error during division of ${global[varName]} by ${divValue}, please ensure the operation is possible.`
      );
    }
  } else {
    throw Error(
      `DefineError: Please be sure to define the variable ${varName} using defineVar() before using divvar().`
    );
  }
}
export function multVar(varName, multValue) {
  if (global[varName]) {
    if (global[varName] * multValue) {
      var product = global[varName] * multValue;
      global[varName] = product;
      return product;
    } else {
      throw Error(
        `MathError: Error during multiplying ${global[varName]} by ${multValue}, please ensure the operation is possible.`
      );
    }
  } else {
    throw Error(
      `DefineError: Please be sure to define the variable ${varName} using defineVar() before using multVar().`
    );
  }
}

// Generating Methods
export function helloWorld() {
  var appVersion = global.appVersion;
  var appName = global.appName;

  console.log("Hello World from", appName, appVersion);
}

export function exportAppData(div) {
  if (div.innerHTML) {
    var dataDiv = document.createElement('div');
    dataDiv.innerHTML = `Powered by ${appName}, version ${appVersion}`;
    dataDiv.classList.add('right-txt', 'no-select');
    div.appendChild(dataDiv);
  } else if (div === "console") {
    return `Generated from ${appName}, version ${appVersion}`;
  } else {
    console.error('DataError: [exportAppdata] - Div given isn\'t editable.');
  }
}

export function exportAppUtils(div) {
  if (div.innerHTML) {
    var utilsDiv = document.createElement("div");
    utilsDiv.innerHTML =
      '<a href="https://gitlab.com/CentaurusDJ/import-cours/-/issues">Report issue</a><br>'+
      '<a href="https://gitlab.com/CentaurusDj/import-cours/-/tree/main/www/portgen/">See source code</a>';
    utilsDiv.classList.add("left-txt", "no-select");
    div.appendChild(utilsDiv);
  }
}

function test(arg) {
  console.log(arg);
}

// Variables
var appVersion = defineVar("appVersion", 0.1);
const appName = defineVar("appName", "PortGen");
var oneVar = defineVar("oneVar", 1);

// Script Execution | Used only while developing otherwise might cause bugs and unecessary tasks for client
//console.log(global)