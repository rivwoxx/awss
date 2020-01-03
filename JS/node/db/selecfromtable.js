var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "rivwox",
  password: "peper",
  database: "tarjetas"
});

/*
con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT * FROM customers", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
});
*/

con.connect(function(err) {
    if (err) throw err;
    con.query("SELECT tarjeta FROM customers", function (err, result, fields) {
      if (err) throw err;
      console.log(result);
    });
  });