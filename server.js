var http = require("http"),
  url = require("url"),
  path = require("path"),
  fs = require("fs"),
port = process.argv[2] || 3000;

http.createServer(function (request, response) {

  var uri = url.parse(request.url).pathname, 
    filename = path.join(process.cwd(), uri);

  var contentTypesByExtension = {
    '.html': "text/html",
    '.css': "text/css",
    '.js': "text/javascript",
    '.pdf': "bin/pdf"
  };

  console.log("serving:", filename);

  fs.exists(filename, function (exists) {
    if (!exists) {
      response.writeHead(404, { "Content-Type": "text/html" });
      response.write("<html><style>html{background:#1a1a1a;color:#fff;font-size:48px;user-select:none;text-align:center;}</style>404 not found</html>");
      response.end();
      return;
    }

    if (fs.statSync(filename).isDirectory()) filename += '/index.html';

    fs.readFile(filename, "binary", function (err, file) {
      if (err) {
        response.writeHead(500, { "Content-Type": "text/plain" });
        response.write(err + "\n");
        response.end();
        return;
      }

      var headers = {};
      var contentType = contentTypesByExtension[path.extname(filename)];
      console.log('content', contentTypesByExtension[path.extname(filename)]);
      if (contentType) headers["Content-Type"] = contentType;
      response.writeHead(200, headers);
      response.write(file, "binary");
      response.end();
    });
  });
}).listen(parseInt(port, 10));

console.log("Static file server running at\n  => http://localhost:" + port + "/\nCTRL + C to shutdown");