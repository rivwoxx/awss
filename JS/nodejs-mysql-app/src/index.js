var express = require('express');
var morgan = require('morgan');
var exphbs = require('express-handlebars');
var path = require('path');

//inicializa
var app = express();

//settings 
// app.set('port', process.env.PORT || 4000);
// app.set('views', path.join(__dirname, 'views'));
// app.engine('.hbs', exphbs({  //configuracion de engine
//    defaultLayout: 'main',
//    layoutsDir: path.join(app.get('views'), 'layouts'), //directorio layouts esta dentro de /views
//    partialsDir: path.join(app.get('views'), 'partials'), //directorio partials esta dentro de /views
//    extname: '.hbs', //configurar extension de archivo de handlebars
//    helpers: require('./lib/handlebars')
// }))
// app.set('view.engine', '.hbs');

app.set('port', process.env.PORT || 4000);
app.set('views', path.join(__dirname, 'views'));
app.engine('.hbs', exphbs({
  defaultLayout: 'main',
  layoutsDir: path.join(app.get('views'), 'layouts'),
  partialsDir: path.join(app.get('views'), 'partials'),
  extname: '.hbs',
  helpers: require('./lib/handlebars')
}))
app.set('view engine', '.hbs');

//middleware
app.use(morgan('dev'))
app.use(express.urlencoded({extended:false}));  //acceptar datos de usuario desde formulario :)
app.use(express.json());    //para enviar y recibir jsons

//global_variables
app.use((req,res,next) => {
    //toma info de usuario y su respuesta y continua con el resto del código con next()
    next(); 
})

//routes
//define server url
app.use(require('./routes/'));
app.use(require('./routes/authentication'));
app.use('/links',require('./routes/links'));

//Public
app.use(express.static(path.join(__dirname,'public')));

//Starting the server
app.listen(app.get('port'),() =>{
    console.log('Server on port', app.get('port')); 
})