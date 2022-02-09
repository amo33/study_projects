'use strict';

// promise is used for asynhronous operation instead of callback
// 1. state : 상태 (현 상태)
// 2. producer와 consumer의 차이 - 제공하는 자와 활용하려는 자

// state : pending 상태 -> fulfilled state / 문제 생길 시 : rejected state
// producer : Promise object를 만드는자
// consumer : ㅔproducer로부터 받은 것을 활용

// 1. producer - promise 만들기
// when new promise is created, the executor runs automatically
const promise = new Promise((resolve, reject)=>{ // promise가 만들어지는 순간 안의 내용을 실행
  //do some heavy work 오래 걸리는 일은 비동기적으로 처리하는 것이 효과적
  console.log('Doing something...');
  setTimeout(()=>{
     //resolve('andy');
     reject(new Error('no Network'));
  }, 2000);
});

// 2. consumers : then, catch, finally -> get values
// then 은 promise가 수행해서 reolve가 실행되면 쓰인다. reject함수를 다룰 수 없다.
// catch는 promise가 수행하는 중, reject함수가 실행될때 쓰인다.
promise
.then((value) =>{ // promise가 잘 수행이 되어서 resolve의 callback함수를 통해서 전달한 값이 value로 넘어온다.
  console.log(value);
})
.catch(error=>{
  console.log(error);
})
.finally(()=> {console.log('finally'); // 성공하든 실패하든 상관없이 맨마지막에 무조건 실행
})

// 3. promise train
const fetchNumber = new Promise((resolve, reject) =>{
  setTimeout(()=> resolve(1), 1000);
})
// then은 값을 다룰 수 있고, promise를 다룰 수 있다.(look at the third 'then')
fetchNumber
.then(num => num*2) // 2 and 2 is tossed to the next
.then(num => num *3)
.then(num=>{
  return new Promise((resolve, reject)=>{
    setTimeout(()=> resolve(num-1), 1000);
  });
})
.then(num => console.log(num));

//4. error handling

const getHen = ()=>
  new Promise((resolve, reject)=>{
    setTimeout(()=> resolve('Big chicken'), 1000);

  });
const getEgg = hen =>
  new Promise((resolve, reject)=>{
  //  setTimeout(()=> resolve(`${hen}=> Egg`), 1000);
    setTimeout(()=> reject(`error! ${hen}=> Egg`), 1000);
  });
const cook = egg =>
  new Promise((resolve, reject)=>{
    setTimeout(()=> resolve(`${egg} => Pan`),1000);
  })

getHen()
.then(hen=> getEgg(hen))
.catch(error =>{ return 'Mega chicken! => Egg'})
.then(egg=> cook(egg))
.then(meal=> console.log(meal));
