var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "rivwox",
  password: "peper",
  database: "tarjetas"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "INSERT INTO customers (nombre, tarjeta, csv, date) VALUES ('Alejandro Sagastegui', '5454545454545454','645','02/24')";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
  });
});