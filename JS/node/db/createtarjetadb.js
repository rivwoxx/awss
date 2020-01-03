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
  var sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), tarjeta VARCHAR(255), csv VARCHAR(255), date VARCHAR(255))";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table created");
  });
}); 