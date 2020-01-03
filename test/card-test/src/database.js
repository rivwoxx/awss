var mysql = require('mysql');
var {promisify} = require('util');
var {database} = require ('./keys');

var pool = mysql.createPool(database); //conexión a db pero usando metodo pool en lugar de createConnection
pool.getConnection((err,connection) => {
    if(err){
        if(err.code === 'PROTOCOL_CONNECTION_LOST'){
            console.error('DATABASE CONNECTION WAS CLOSED');
        }
        if(err.code === 'ER_CON_COUNT_ERROR'){
            console.error('DATABASE HAS TO MANY CONNECTIONS');
        }
        if(err.code === 'ECONNREFUSED'){
            console.log('DATABASE CONNECTION WAS REFUSED');
        }
    }

    if (connection) connection.release();
    console.log('DB is connected')
});

//promisify pool queries
pool.query = promisify(pool.query);
module.exports = pool;
