var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "rivwox",
  password: "peper"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});