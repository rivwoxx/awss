var express = require('express');
var router = express.Router();

router.get('/', (req, res) => {
    res.send('The real Slim Shady, Please Stand up!')
});

module.exports = router;