var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "rivwox",
  password: "peper",
  database: "test"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "CREATE TABLE testa (name VARCHAR(255), address VARCHAR(255))";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table created");
  });
});