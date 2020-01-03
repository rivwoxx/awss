var os = require('os');

console.log(os.arch());
console.log(os.platform());
console.log(os.release());
//console.log(os.cpus());
console.log('free mem:', os.freemem());
console.log(os.totalmem());
//console.log(os.userInfo());