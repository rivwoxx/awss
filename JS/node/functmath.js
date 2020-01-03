//nuestro propio modulo
function add(x1,x2){
    return x1 + x2
}

function subs(x1,x2){
    return x1 - x2
}

function mul(x1,x2){
    return x1 * x2
}

function div(x1,x2){
    if(x2 == 0){
        console.log('No se puede dividir entre 0')
    }else{
        return x1 / x2
    }
}

exports.add = add;
exports.subs = subs;
exports.mul = mul;
exports.div = div;