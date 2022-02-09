// 1. Use strict
// use this for valina Javascript
'use strict';

// 2. variable
// let (added in ES6)

let name = 'andy';
console.log(name);
name = 'hello';
console.log(name);

// 3. block scope & global scope

let globalName = 'global name';
{
  let name = 'andy';
  console.log(name);
  name = 'hello';
  console.log(name);
}
console.log(name);
console.log(globalName);

// var hoisting -> 어디에 선언했냐 상관없이 제일 위로 선언을 올리는 것
// ex인데, var 는 사용하는 것을 지양한다. so use 'let'
{
  age = 4;
  var age;
}

// 4. constant : 선언함과 동시에 값을 변경 X which is immutable / 읽기만 가능하다.
// why immutable data is preferable
// - security
// - thread safety
// - reduce human mistakes
const daysInWeek = 7;
const maxNumber = 5;

const bigInt = 123456789012345678901234567890;
console.log(`value: ${daysInWeek}, type: ${typeof bigInt}`);
// 5. variable type
// primitive (single) type: number, string, boolean 같은 것 : 값 자체가 메모리에 저장
// object type : single type이 여러개 묶여있는 것 - 객체 형태 : reference를 가리키고 그 ref가 실제 object안의 값들을 저
// function , first class function : 함수 자체를 값으로 넘겨줄 수 있다.

//6 Dynamic typing : 타입을 dynamic하게 변경할 수 있다.
// console.log는 `` 로 쓴다.
let text = 'hello';
text = 1;
text = '7' + 5;
console.log(`text value : ${text}, type: ${typeof text}`);
text = '8' / '2';
console.log(`text value : ${text}, type: ${typeof text}`);

// Immutable data type: primitive type은 데이터 자체를 변경하는 것은 불가능 , frozen objects
// mutable data type : all objects are mutable






 
