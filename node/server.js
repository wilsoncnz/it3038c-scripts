var fs = require("fs");
var http = require("http");
var ip = require('ip');
var os = require("os");

function getUptime_days() {
  days = Math.floor(os.uptime() / (60*60*24));
  return days 
}

function getUptime_hours() {
  hours = Math.floor((os.uptime() % (60*60*24)) / (60*60));
  return hours 
}

function getUptime_minutes() {
  minutes = Math.floor(((os.uptime() % (60*60*24)) % (60*60)) / (60));
  return minutes 
}

function getUptime_seconds() {
  seconds = Math.floor(((os.uptime() % (60*60*24)) % (60*60)) % (60));
  return seconds 
}

var server = http.createServer(function(req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function (err, body) {
          res.writeHead(200, {"Content-Type": "text/html"});
          res.end(body);
    });
}
    else if(req.url.match("/systeminfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
          <html>
            <head>
              <title>Node JS Response</title>
            </head>
            <body>
              <p>Hostname: ${myHostName}</p>
              <p>IP: ${ip.address()}</p>
              <p>Server Uptime: Days: ${getUptime_days()}, Hours: ${getUptime_hours()}, Minutes: ${getUptime_minutes()}, Seconds: ${getUptime_seconds()}</p>
              <p>Total Memory: ${os.totalmem()*0.000001} MB</p>
              <p>Free Memory: ${os.freemem()*0.000001} MB</p>
              <p>Number of CPUs: ${os.cpus().length}</p>            
            </body>
          </html>` 
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/html"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000)

console.log("Server listening on port 3000");
