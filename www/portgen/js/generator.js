// Generating Methods
export function helloWorld() {
  var appVersion = window.appVersion;
  var appName = window.appName;

  console.log("Hello World from", appName, appVersion);
}

export function exportAppData(divTag) {
  if (document.getElementsByTagName(divTag)) {
    var div = document.getElementsByTagName(divTag);
    div.innerHTML = String('Generated from ' + String(appName) + ', ' + String(appVersion));
  } else {
    console.error('DataError: [exportAppdata] - Div given isn\'t editable.' )
  }
}

// Variables
const appVersion = 0.1; // TODO: Search why can't retrieve value when calling as globalThis attribute?
const appName = 'PortGen';