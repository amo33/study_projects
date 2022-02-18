const http = require("http");
const querystring = require('querystring');

const server = http.createServer(function(req, res){
    let postdata = '';
    let result = undefined;
    req.on('data', function(data){
        postdata = postdata + data;
    });

    req.on('end', function(){
        var parsedQuery = querystring.parse(postdata);
    
        console.log(parsedQuery);

        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end('var1 value =' + result);
    
    });
});

server.listen(8000, ()=>{
    console.log('Server is running ...');
})

