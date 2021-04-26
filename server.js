var http = require("http"),
  url = require("url"),
  path = require("path"),
  fs = require("fs"),
  exec = require("child_process"),
  os = require("os"),
port = process.argv[2] || 3000;


http.createServer(function (request, response) {

  var uri = url.parse(request.url).pathname,
    filename = path.join(process.cwd(), uri);

  var contentTypesByExtension = {
    '.html': "text/html",
    '.css': "text/css",
    '.js': "text/javascript",
    '.pdf': "application/pdf",
  };
  var serverLanguages = [
    'php',
  ];

  console.log("serving:", filename);

  fs.exists(filename, function (exists) {
    // If the URL doesn't gives a file
    if (!exists) {
      response.writeHead(404, { "Content-Type": "text/html" });
      response.write("<html><style>html{background:#1a1a1a;color:#fff;font-size:48px;user-select:none;text-align:center;}</style>404 not found</html>");
      response.end();
      return;
    }

    // If URL finish with "/" we search the index HTML file and send it.
    if (fs.statSync(filename).isDirectory()) filename += '/index.html';

    // If URL states an existing file in dir
    fs.readFile(filename, "binary", function (err, file) {
      if (err) { // If when tries to reach file error occurs, send errors as response
        response.writeHead(500, { "Content-Type": "text/plain" });
        response.write(err + "\n");
        response.end();
        return;
      }

      // If file needs to be processed by server then sent to client
      if (serverLanguages[path.extname(filename)]) {
        console.log('Processing file...');
        headers["Content-Type"] = contentType;
        response.writeHead(200, headers);
        if (os.platform == "win32") { // Script on Windows
          response.write(exec("libs/php/Win_php/php.exe" + filename, (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`);
                return;
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
                return;
            }
            console.log(`stdout: ${stdout}`);
          }), "binary");

        } else if (os.platform == "linux") { // Script on Linux
          response.write(exec("libs/php/Linux_php/php" + filename, (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`);
                return;
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
                return;
            }
            console.log(`stdout: ${stdout}`);
          }), "binary");
        }
        response.end();
      } else {
        console.log('Terminate process, file not taken...');
        exec("npm stop", (error, stdout, stderr) => {
          if (error) {
              console.log(`error: ${error.message}`);
              return;
          }
          if (stderr) {
              console.log(`stderr: ${stderr}`);
              return;
          }
          console.log(`stdout: ${stdout}`);
        });
      }

      var headers = {};
      var contentType = contentTypesByExtension[path.extname(filename)];
      console.log('content:', contentTypesByExtension[path.extname(filename)]);
      if (contentType) headers["Content-Type"] = contentType;
      response.writeHead(200, headers);
      response.write(file, "binary");
      response.end();
    });
  });
}).listen(parseInt(port, 10));

console.log("Static file server running at\n  => http://localhost:" + port + "/\nCTRL + C to shutdown");