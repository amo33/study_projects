// Function
// perform task or calculate a value

// 1. Function Delcaration
// function name(param1 , param2) {body... return;}
// one function === one thing (한 가지 일을 수행한다.)
// function 명도 고려해서 만든다.
// function is object in JS
'use strict';
function printHello(){
  console.log('Hello');
}
printHello();

function log(message){
  console.log(message);
}

log('Hello@');
log(1234);

// 2. parameters
// premitive type : passed by value
// object type : passed by reference
function changeName(object){
  object.name = 'coder';
}
const andy = {name : 'Amndy'};
changeName(andy);
console.log(andy);

// 3. default parametes (ES6에 추가됨 )
// 만약 들어오는 값이 없으면, default value를 사용한다.
function showMessage(message, from = 'unknown'){
  console.log(`${message} by ${from}`);
}
showMessage('Hi');

// 4. rest parameters -> 배열 형태로 전달된다. 즉, args가 배열형태라고 생각
function printAll(...args){
  for (let i=0; i<args.length; i++){
    console.log(args[i]);
  }
  console.log("Another Method : By using 'of' ");
  for (const arg of args){
    console.log(arg);
  }
}

printAll('dream', 'coding', 'andy');

// 5. local scope

let globalMessage = 'global'; // global
function printMessage(){
  let message = "hello";
  console.log(globalMessage);
  function printAnother(){
    console.log(message);
    let childMessage = "Hello";
  }
  // can't print the child one at this scope.
}

// 6. return

function sum(a, b){
  return a+b;
}
const result = sum(1, 2);
console.log(result);

// 7. early return - early exit
// logic을 생각할때 if else 시 잘 설계하기

function upgradeOne(user){
  if(user.poiny <= 10){
    return;
  }
  // long upgrade ones/
}

// 8 function 표현 방식
// function은 변수에 할당이 되고, parameter로 사용될 수 있고, 다른 함수에 의해 return 될 수 있다.

const print = function (){ // anonymous function
  console.log('print');
}

const print2 = function p(){ // named function
  console.log('print');
}
print();
const printAgain = print;
printAgain();

const sumAgain = sum;
console.log(sumAgain(2,3));

// 2. callback function - 함수의 parameter에 함수를 보내주는 방식이다.
function randomQuiz(answer, printYes, printNo){
  if(answer === `It's right`){
    printYes();
  }
  else{
    printNo();
  }
}

const printYes = function (){
  console.log('Yes');
}
const printNo = function (){
  console.log('No');
}
randomQuiz(`It's right`, printYes, printNo);
randomQuiz('I do not No', printYes, printNo);

// 3. arrow function
// always anonymous

const simplePrint = () => console.log('SimplePrint done!');
const add = (a,b) => a + b;
const add2 = (a,b) =>{
  // long long codes
  return a+b;
}

// IIFE 선언함과 동시에 바로 호출됨
(function hello(){
  console.log('IIFE');
})();

// Quiz
// make a function calculate(command, a, b)

const calculate = (command, a, b) =>{
  switch (command){
    case '+':
      return a+b;
    case '-':
      return a-b;
    case '*':
      return a*b;
    case '%':
      return a%b;
    case '/':
      return a/b;
    default:
      console.log('Wrong Input');
      return -1;
  }
}
console.log(calculate('-', 3, 2));
console.log(calculate('+', 3, 4));
console.log(calculate('#', 2 , 10));
