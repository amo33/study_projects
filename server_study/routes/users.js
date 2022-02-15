// All the user related 
const express = require('express');
const router = express.Router();

// we had users section to use but we will use 'users' from server.js to indicate the relation between users.js and server.js 

/*
router.get('/users', (req,res)=>{
    res.send('User list')
})

router.get('/users/new', (req,res)=>{
    res.send("USer New Form")
})*/

router.get('/', (req,res)=>{
    res.send('User list')
})

router.get('/new', (req,res)=>{
    res.send("USer New Form")
})

module.exports = router 