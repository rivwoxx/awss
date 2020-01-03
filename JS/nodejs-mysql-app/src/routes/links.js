var express = require('express');
var router = express.Router();
var pool = require('../database')

router.get('/add', (req, res) => {
    res.render('links/add');
});

router.post('/add', async (req,res) => {
    // console.log(req.body);
    const {title, url, description} = req.body;
    const newlink ={
        title,
        url,
        description
    };
    await pool.query('INSERT INTO links set ?', [newlink]);   //this is an async insert
    res.send('received');
    // console.log(newlink);
});

module.exports = router;