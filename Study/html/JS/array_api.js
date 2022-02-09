'use strict';

// Q1. make a string out of an Array
{
  const fruits = ['apple', 'Banana', 'Orange'];
  const result = fruits.join(',');
  console.log(result);
}
// Q2. make an array out of string
{
  const fruits = 'App, Bana, Peac, grap';
  const result = fruits.split(',');
  console.log(result[2]);
}
//Q3 make this array look like the next : [5,4,3,2,1]
{
  const array= [1, 2, 3, 4, 5];
  const result = array.reverse();
  console.log(result);
}

// Q4 make new array without first two elements
{
  const array = [1, 2, 3, 4, 5];
  //const result = array.splice(2);
  const result = array.slice(2, array.length + 1);
  console.log(result);

}

class Student {
  constructor(name, age, enrolled, score){
    this.name = name;
    this.age = age;
    this.enrolled = enrolled;
    this.score = score;
  }
}
const students = [
  new Student('A', 29, true, 45),
  new Student('B', 28, false, 80),
  new Student('C', 30, true, 90),
  new Student('D', 40, false, 66),
  new Student('E', 18, true, 88),
];

//Q5
// Find  upper than 90 score
{ /*
  const result =[];
  for(let i = 0; i< students.length; i++){
    if (students[i].score === 90){
      result.push(students[i]);
    }
  }
  console.log(result);
 */
 const result = students.find((student) => student.score === 90
 )
 console.log(result);
}

//Q6 make an array of enrolled students
{
  const result = students.filter((student) => student.enrolled === true);
  console.log(result);
}

// Q7 make an array containing only the students' scores
{
  const result = students.map((student) => student.score);
  console.log(result);
}
// Q8 check if there is a student with the score lower than 50
{
  const result = students.find((student) => student.score < 50) ? true : false;
  // const result = students.some((student) => student.score < 50);
  console.log(result);
}

// Q9 compute average score
{
  const result = students.map((student) => student.score).reduce((pre, cur) => pre+cur) / students.length;
  const result2 = students.reduce((prev, curr)=>{
    return prev + curr.score;
  }, 0);
  console.log(result2);
}
//Q10 make a string containong all scores

{
  const temp = students.map((student) => student.score).join(',');
  console.log(temp);
}

// Q10-2
{
  const result = students.map((student) => student.score)
  .sort((a,b) => a-b)
  .join(',');
  console.log(result);
}
