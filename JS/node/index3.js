var fs = require('fs')

//creando nuevo archivo

fs.writeFile('./test.txt',"Subieron la mota!, Tambien el alcohol",function(err){ 
    //recibe un error
    if(err){
        console.log(err);
    }
    console.log('Archivo creado')
})

fs.readFile('./test.txt', function(err,data){
    if(err){
        console.log(err)
    }
    console.log(data.toString());
    //console.log(data.toJSON());
})