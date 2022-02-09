'use strict';

// javascript는 동기적인 아이다. (in order after hoisting)
// hoisting : 변수와 함수 선언들이 제일 위로 자동으로 올라가는 것

console.log('1');
setTimeout(() =>{
  console.log('2'); // callback function
}, 500); // 1000 milisecond : 1초
console.log('3');

// synchronous callback

function printImmediately(print){
  print();
}
printImmediately(()=> console.log('hello'));

// asynhronous callback
// 절차적으로 수행하지 않고, 임의로 조정해준 순서로 출력하는 방식

function printWithDelay(print, timeout){
  setTimeout(print, timeout);
}
printWithDelay(()=> console.log('async callback'), 2000);

// Callback hell

class Userstorage{

  loginUser(id, password, onSuccess, onError){
    setTimeout(()=>{
      if((id === 'andy' && password === 'Anony') || (id === "Tom" && password === "code")){
        onSuccess(id);
      }else{
        onError(new Error('not found'));
      }
    }, 2000);
  }

  getRoles(user, onSuccess, onError){
    setTimeout(()=>{
      if(user === "andy"){
        onSuccess({name: "andy", role: "master"});
      }
      else{
        onError(new Error('No access'));
      }
    }, 1000);
  }
}

const users = new Userstorage();
const id = prompt("Enter your Id");
const password = prompt("Enter Your password");
/*
users.loginUser(id, password, user=>{
  users.getRoles(
    user,
    (userwithRole)=>{
      alert(`Hello ${userwithRole.name}, you have a ${userwithRole.role} role`);
    },
    error=>{
      console.log(error);
    }
  );
 },
 error =>{
   console.log(error);
 }
);
*/

users.loginUser(id, password, user=>{
  users.getRoles(user, (userwithRole)=>{
    alert(`Hello ${userwithRole.name}, you have a ${userwithRole.role} role.`);
  },
  error => {
    console.log(error);
  }
),
error => {
  console.log(error);
};
}
)
