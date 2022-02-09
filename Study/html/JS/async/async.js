// async & await
// clear style of using Promise

function sleep(ms) {
  return new Promise(resolve=>setTimeout(resolve, ms));
}


출처: https://jam-ws.tistory.com/29 [쨈의 작업공간]

//1. async

function fetchUser(){
  // do network request in 10secs..
  return 'amo';
}

const user = fetchUser();
console.log(user);
// 6~12 는 동기적으로 진행한다.
//비동기적으로 처리하는 것이 클라이언트를 위해 진행

function fetchUser2(){
  return new Promise((resolve, reject)=>{ // resolve, reject로 실행
    // do network request for 10 10secs
    resolve('amo');
  })
}
const user2 = fetchUser2();
user2.then(console.log);
console.log(user2);

// async 키워드

async function fetchUser3(){ // 키워드 하나로 진행 가능
  return 'amo';
}
const user4 = fetchUser3();
console.log(user);

// 2. await

async function getApple(){
  await sleep(2000);
  return 'app';
}

async function getBanana(){
  await sleep(2000);
  return "bana";
}

// how to get apple and banana at the same time
async function pickFruits(){
  const applePromise = getApple();
  const bananaPromise = getBanana();
  const apple = await applePromise;
  const banana = await bananaPromise;

  return `${apple} + ${banana}`;
}

// useful api to do the preivous one
function pickAllFruits(){
  return Promise.all([getApple(), getBanana()]).then(fruits =>
    fruits.join(' + ')
  );
}
pickAllFruits().then(console.log);
// console.log -> 을 함수처럼 넘겨서 출력해주는 것이다.

// 먼저 나오는 값 한 개만 받고 싶다.

function pickOnlyOne(){
  return Promise.race([getApple(), getBanana()]);
}
pickOnlyOne().then(console.log);

//
