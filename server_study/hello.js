const express = require("express");
const app = express();
// request method is get with using ? and = like these. 
app.get('/',function(req, res){
    res.send('Helllo world!');
});

app.listen(3000, function(){
    console.log('Example app listening on port 3000!');
});
