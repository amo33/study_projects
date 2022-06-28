const { application } = require('express');
let wiki = require('./wiki.js');

application.use('/wiki', wiki);