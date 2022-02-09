// Objects
// one of the Js data type - 관련된 data와 method를 하나로 묶었다.
const name = 'andy';
const age = 4;

function print(person){
  console.log(person.name);
  console.log(person.age);
}

const obj1 = {}; // ㅐobject literal syntax로 생성
const obj2 = new Object(); // constructor로 생성

const andy = {name: 'An', age : 20};
print(andy);

// Javascript는 나중에 field를 추가할 수 있다. (run time에 objetc를 다루기 때문이다.)
andy.year = 3;
// string으로 배열형 접근하거나 바로 위처럼 . 으로 접근하기도 함
console.log(andy['year']);

andy['HasJob'] = true;
console.log(andy.HasJob);

function printValue(obj, key){
  console.log(obj[key]);
}
printValue(andy, 'year');

// property value shorthand - makePerson function 참고

const person1 = {name: 'bob', age:2};
const person2 = {name: 'steve', age: 3};
const person3 = {name: 'Tom', age: 4};
const person4 = makepersons('Roan', 20);
function makepersons(name, age){
  return{
    name,
    age,
  };
}

// in operator : prorerty가 존재하는지 (key) check한다.

console.log('name' in andy);
console.log('age' in andy);
console.log('weigth' in andy);

// console.clear();

// for .. in vs for .. of
// for( key in obj )
for(key in andy){
  console.log(key);
}

// for (value in iterable) 배열과 같은 배열 리스트를 쓴다.

const array = [1, 2, 3, 4, 5];
for (let i=0; i<array.length; i++){
  console.log(array[i]);
}
for(value of array){
  console.log(value);
}

// cloning

const user = {name: 'andy', age : 22};
const user2 = user; // user안에 들어있는 레퍼렌스가 따로 할당되고 그 레퍼렌스는 user와 같은 property 가리킨다.
user2.name = 'code';
console.log(user); // 따라서 완벽한 복제는 없다.

// 방법
const user4 = {};
Object.assign(user4, user);
console.log(user4);

const user5 = Object.assign({}, user2);
console.log(user5);
