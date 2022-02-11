// function declare

function add(a, b){ // no type declare
  const sum = a+b;
  return sum; // pass the result
}

const result = add(1,2);
console.log(result);

// toss function to parameter

function doSomething(add){
  console.log(add);
  const result = add(2,4);
  console.log(result);
}
function doSomething2(add){
  console.log(add);

}
// 함수를 전달하는 것은 이와 같다.
doSomething(add); // 아예 함수 자체가 넘겨진다.

// 함수를 잘못 전달하는 예시
doSomething2(add(1,2)); // 이건 함수의 return 결과를 domsomething2 함수에 넘겨주는 거다.

// const에 함수 할당

const addec = add;
console.log(addec);
addec(1,3); // 변수가 함수처럼 쓰여지는 것을 볼 수 있다.
