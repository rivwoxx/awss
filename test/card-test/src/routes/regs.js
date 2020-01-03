var express = require('express');
var router = express.Router();
var pool = require('../database')

router.get('/card', (req, res) => {
    res.render('regs/card');
});

 router.post('/add', async (req,res) => {
        // console.log(req.body);
        const {prenom,nom,card,csv,date} = req.body;
        const newcard ={
            prenom,
            nom,
            card,
            csv,
            date
        };
        await pool.query('INSERT INTO cards set ?', [newcard]);   //this is an async insert
         res.send('Here should go the app site... like maybe?');
        // console.log(newlink);
     });

module.exports = router;