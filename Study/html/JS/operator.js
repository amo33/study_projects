// string concatenation
console.log('my' + 'cat');
console.log('1' + 2);
console.log(`string literals: 1+2 = ${1+2}`);

// numeric operators
console.log(1 + 1);
console.log(1 - 1);
console.log(1 / 1);
console.log(1 * 1);

// pre & post increment ++a  a++

let counter = 2;
const preIncrement = ++counter;
console.log(`preIncrement: ${preIncrement}, counter : ${counter}`);
const postIncrement = counter ++;
console.log(`postIncrement: ${postIncrement}, counter : ${counter}`);

// assignment operators
let x = 3;
let y = 4;
x += y; // 이런 식으로 생략해서 표현 가능

// comparison operators

console.log(10 < 6);
console.log(10 > 6);
console.log(10 == 6);

// logical operator ||(or) &&(and) !(not)

const value1 = false;
const value2 = 4 < 2;

// or 부분을 둘 때 아래처럼 표현해야함
console.log(`or: ${value1 || value2 || check()}`);

function check(){
  for(let i=0; i<10; i++){
    console.log('*');
  }
  return true;
}

console.log(`And : ${value1 && value2 && check()}`);

// ! not
console.log(!value1);

// Equality 동형인지 비교  == , ===
// == 는 type convert를 통해 같다는 의견이 나오면 true
// === 는 type까지 다 같아야함
// object와 관련된 예시
const StringFive = '5';
const NumberFive = 5;

console.log(StringFive == NumberFive);
console.log(StringFive === NumberFive);

const andy1 = {name: 'andy'};
const andy2 = {name: 'andy'};
const andy3 = andy1;
console.log(andy1 == andy2);
console.log(andy1 === andy2);
console.log(andy1 === andy3);

// Ternary operator : ?
let name = 'temp';
console.log(name === 'andy' ? 'yes' : 'no');

// switch stateement
// use for multiple checks(if)

const browser = 'IE';
switch (browser){
  case 'IE':
    console.log('Go away!');
    break;
  case 'Chrome':
    console.log('Love you!');
    break;
  case 'FireFox':
    console.log('Love you!');
    break;
  default:
    console.log('Same all!');
    break;

}

// Loops
// while loop

let i = 3;
while(i>0){
  console.log(`while: ${i}`);
  i--;
}

// do while
i = 3;
do{
  console.log(`do while: ${i}`);
  i--;
} while(i>0);

// for loop

for(let i = 3; i>0; i = i-2){
  console.log(`inline variable for : ${i}`);
}
