'use strict';
//class - template
//object- instance of class (class의 실제 객체들)

// class declaration

class Person {
  // constructor
  constructor(name, age){
    //fields
    this.name = name;
    this.age = age;
  }

  // methods
  speak(){
    console.log(`${this.name}: hello!`);
  }
  // getter 와 setter는 사용자가 잘못 입력하는 것을 방지하기 위해 쓰임
}

const andy = new Person('andy', 20);
console.log(andy.name);
console.log(andy.age);
andy.speak();

// getter & setter
class User {
  constructor(firstName, lastName, age){
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  get age(){
    return this._age;
  }

  set age(value){
   //  if (value <0){
  //    throw error(`age can't be negative!`);
  //  }
  //  this._age = value;
    this._age = value <0 ? 0 : value;
  }
}
const user1 = new User('Tom', 'Anderson', 10);
const user2 = new User('James', 'Choi', -1);

// public & private fields

class Experiment{
  publicField = 2; // public임
  #privateField = 3; // private임
}
const experiment = new Experiment();
console.log(experiment.publicField);
console.log(experiment.privateField);

// static property and methods
// class를 가지고 있는 고유한 값으로 object와 관계없이 클래스의 것으로 클래스로 선언해야함

class Article{
  static publisher = 'Dream comes true';
  constructor(articleNumber){
    this.articleNumber = articleNumber;
  }

  static printPublisher(){
    console.log(Article.publisher);
  }
}

const article1 = new Article(1);
const article2 = new Article(2);
console.log(Article.publisher);
Article.printPublisher();

// 상속과 다양성

class Shape{
  constructor(width, height, color){
    this.width = width;
    this.height = height;
    this.color = color;
  }
  draw(){
    console.log(`Drawing ${this.color} color!`);
  }

  getArea(){
    return this.width * this.height;
  }
}

class Rectangule extends Shape{}
class Triangule extends Shape{
  draw(){
    super.draw();
    console.log('*');
  }
  getArea(){
    return this.width*this.height*0.5;
  }
  tostring(){
    return `Triangule: color: ${this.color}`;
  }
}

const rectangule = new Rectangule(20, 20, 'blue');
rectangule.draw();
console.log(rectangule.getArea());
const triangule = new Triangule(20, 20, 'red');
triangule.draw();
console.log(triangule.getArea());
console.log(triangule);


// instanceof - 상속한것인지 확인할 수 있다.

console.log(rectangule instanceof Rectangule);
