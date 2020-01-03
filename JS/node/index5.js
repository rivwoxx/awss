var express = require('express');

var server = express();

server.get('/', function(req,res){
    res.send('<h1>El pollo no deberia poder volar</h1>')

})
server.listen(3000, function(){
    console.log('Server on port 3000');
})