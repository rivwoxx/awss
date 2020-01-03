var http = require('http')

//req = request / res = respond
/*http.createServer(function(req,res){
    res.writeHead(200,{'Content-type': 'text/html'});
    res.write('<h1>El pavo esta volando, vaaaato!</h1>');
    res.end();
}).listen(8000); */

const handleServer = function(req,res) {
    res.writeHead(200,{'Content-type': 'text/html'});
    res.write('<h1>El pavo esta volando, vaaaato!</h1>');
    res.end(); 
}

const server = http.createServer(handleServer);

server.listen(8080, function(){
    console.log('Server on port 8080')
})