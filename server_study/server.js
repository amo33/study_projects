// This js is managed by nodemon. This is all about server code 
const express = require('express') // require express library 
const app = express() // set up an actual server 

app.set('view engine', 'ejs');

app.get('/', (req, res)=>{
    
    console.log('Here'); 
    /*
    //res.sendStatus(500) // can actually send http status code
    // res.status(500).json({message: 'Error'}) // can chain status with other things like json 
    res.download('server.js') // make them to download
   // res.send('Hi') // send this to other connected or to the html 
   */
    res.render('index', {text: 'world'}); // render html is showing the coded html file 
    
}) // make route 

const userRouter = require(".routes/users")

app.use("/users", userRouter)

app.listen(3000) // run the server by sending port number // running on port 3000