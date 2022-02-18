'use strict';
let square = require('./export_1');
console.log('The area of a square with a width of 4 is ' + square.area(4));

console.log("Here is your menu list\n which one you would like to pick?");

function pickmenu(){
    const arr = ["1","2","3","4"];
    return arr[Math.floor(Math.random()*arr.length)];
}

const var1 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("var1 order "+pickmenu())
    }, 2000);
})
const var2 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("var2 order "+ pickmenu())
    }, 3000);
});
const var3 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("var3 order "+ pickmenu())
    }, 1000);
});
const lst = [var1, var2, var3];
Promise.all(lst).then(console.log);
// ajax call just gives the user ordered results. So that's why we have an ordered result.