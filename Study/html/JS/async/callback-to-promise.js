class Userstorage{

  loginUser(id, password){
    return new Promise((resolve, reject)=>{
      setTimeout(()=>{
        if((id === 'andy' && password === 'Anony') || (id === "Tom" && password === "code")){
          resolve(id);
        }else{
          reject(new Error('not found'));
        }
      }, 2000);
    })
  }

  getRoles(user){
    return new Promise((resolve, reject)=>{
      setTimeout(()=>{
        if(user === "andy"){
          resolve({name: "andy", role: "master"});
        }
        else{
          reject(new Error('No access'));
        }
      }, 1000);
    })
  }
}

const users = new Userstorage();
const id = prompt("Enter your Id");
const password = prompt("Enter Your password");
users.loginUser(id, password)
.then(item => users.getRoles(item))
.then(obj => {
  alert(`${obj.name} has a role which is ${obj.role}`);
});
