'use strict';

// Array
// Array Declaration
const arr1 = new Array();
const arr2 = [1, 2];

// Index 활용 방식
const fruits = ['apple','Banana'];
console.log(fruits);
console.log(fruits[1]);

// loop

for(let i=0; i<fruits.length; i++){
  console.log(fruits[i]);
}
fruits.forEach((fruit, index) => {
  console.log(fruit, index);
});

// addition, deletion, copy

// push
fruits.push('Watermelon', 'Mango');
console.log(fruits);

// pop
fruits.pop();
fruits.pop();
console.log(fruits);

// unshift: add item at the front
fruits.unshift('Strawberry', 'Lemon');
//shift : remove from the beginning
fruits.shift();
fruits.shift();
// These two are slower than pop & push. Because front use needs to be updated (뒤에 있는거 한칸씩 땡기거나 미뤄야하므로)

//splice : 특정 인덱스에서부터 삭제

fruits.push('PaPaya', 'Grape');
console.log(fruits);
// fruits.splice(1); // 1부터 모든 데이터를 지운다.
//fruits.splice(1,2); // 1 인덱스부터 2개 지운다.
fruits.splice(1,1, 'Peach', 'Palm'); // 1부터 1개 지우고 뒤에 있는 것들을 차례로 넣어준다.
console.log(fruits);

const fruits2 = ['Bear', 'Coconut'];
const newFruits = fruits.concat(fruits2);

// 5. Search
// find the index of the item

console.log(fruits);
console.log(fruits.indexOf('Grape'));
console.log(fruits.includes('Coconut'));
console.log(fruits.indexOf('Coconut'));

// last index of
fruits.push('Grape');
console.log(fruits.indexOf('Grape')); // 중복되도 제일 첫번째인것
console.log(fruits.lastIndexOf('Grape')); // 뒤에 제일 먼저 나오는 중복된 아이템
