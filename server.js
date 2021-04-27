var http = require("http"),
  url = require("url"),
  path = require("path"),
  fs = require("fs"),
  os = require("os"),
  port = process.argv[2] || 3000;

const { exec, spawn } = require("child_process");
const { extname } = require("path");

var executed_times = 0;

http.createServer(function (request, response) {

  var uri = url.parse(request.url).pathname,
    filename = path.join(process.cwd(), uri);

  var contentTypesByExtension = {
    '.html': "text/html",
    '.css': "text/css",
    '.js': "text/javascript",
    '.pdf': "application/pdf",
    '.php': "text/html"
  };
  var serverLanguages = {
    '.html': false,
    '.css': false,
    '.js': false,
    '.pdf': false,
    '.php': true,
  };
  try {
    if (fs.statSync(filename).isDirectory()) {
      console.log("directory touched");
      filename += '/index.html';
    }
      response.writeHead(200, contentTypesByExtension[path.extname(filename)]);
      response.write(
        '<html><body style="background-color:#1a1a1a; color: #fff; font-size: 28px;">It seems to run fine!</body></html>',
        "utf-8"
      );
      response.end();
  }
  finally {
    console.log('Something unexpected happened, we stop server.');
    response.writeHead(502, 'text/html');
    response.write(
      '<html><body style="background-color:#1a1a1a; color: #fff; font-size: 28px;">Ah! Something went wrong.</body></html>',
      "utf-8"
    );
    response.end();
    return;
  }
}).listen(parseInt(port, 10));

console.log("Static file server running at\n  => http://localhost:" + port + "/\nCTRL + C to shutdown");