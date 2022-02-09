// 1. object to json
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
console.log(json);

const tiger = {
  name : "kevin",
  color : 'Orange',
  size : "Huge",
  birthdate : new Date(),
  Feature: () => {
    console.log(`${name} is the strongest!`);
  }
}

json = JSON.stringify(tiger);
console.log(json);

json = JSON.stringify(tiger, ["name"]);
console.log(json);

json = JSON.stringify(tiger, (key, value) => {
  return key === 'color' ? 'RainBow' : value;
});
console.log(json);

// 2. JSON to object
// parse(json)
console.clear();
const obj = JSON.parse(json, (key, value) =>{
  return key === 'birthdate' ? new Date(value) : value;
});
console.log(obj);
console.log(tiger.birthdate.getDate());
console.log(obj.birthdate.getDate());
// obj.jump(); // 이때 이 함수는 아까 데이터만 넘긴것을 다시 받았기 때문에 이는 실행이 안된다.
// obj에서의 모든 값들은 string이다. if parse에 callback 함수 없이 가져오면 그냥 문자열들을 가져온 셈이다.
