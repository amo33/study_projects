'use strict';
/*
class Userstorage{

  loginUser(id, password, onSuccess, onError){
    setTimeout(()=>{
      if((id === 'andy' && password === 'Anony') || (id === "Tom" && password === "code")){
        onSuccess(id);
      }else{
        onError(new Error('not found'));
      }
    }, 2000);
  }

  getRoles(user, onSuccess, onError){
    setTimeout(()=>{
      if(user === "andy"){
        onSuccess({name: "andy", role: "master"});
      }
      else{
        onError(new Error('No access'));
      }
    }, 1000);
  }
}
*/
/*
const users = new Userstorage();

const id = prompt("Enter your Id");
const password = prompt("Enter Your password");
*/
/*
users.loginUser(id, password, user=>{
  users.getRoles(
    user,
    (userwithRole)=>{
      alert(`Hello ${userwithRole.name}, you have a ${userwithRole.role} role`);
    },
    error=>{
      console.log(error);
    }
  );
 },
 error =>{
   console.log(error);
 }
);
*/
/*
const solvehell = ()=> {
  return new Promise((resolve, reject)=>{
    const id = prompt("Enter your ID");
    const password = prompt("Enter your password");
    setTimeout(()=>{
      resolve({'id':id, 'password': password});
    }, 1000);
  })
};
*/
// why ------------------------------> undefined is still uponing? 
const loginUser = (user)=>{
  return new Promise((resolve, reject)=>{
    setTimeout(()=>{
      console.log(user.id);
      console.log(user.password);
      if((user.id === 'andy' && user.password === 'Anony') || (user.id === "Tom" && user.password === "code")){
        resolve(user.id);
      }else{
        reject(new Error(`error ${user.id} failed to log in.`));
      }
    }, 2000);
  })
}
const getRoles = (user)=>{
   new Promise((resolve, reject)=>{
    setTimeout(()=>{
      if(user === 'andy'){
        resolve({'userid': user, 'userrole':'master'});
      }
      else{
        reject(new Error(`error ${user} does not exist.`));
      }
    }, 1000);
  })
}
/*
solvehell()
.then((user)=>loginUser(user.id, user.password))
.then(id => getRoles(id))
.catch(error => {return "admin"})
.then(user2 =>{alert(`${user2.userid} has a role which is ${user2.userrole}`);})
.catch(error => console.log(error))
.finally(() => console.log("Done!"));
*/
const id = prompt("Enter your ID");
const password = prompt("Enter your password");
const user = {'id':id, 'password': password};
loginUser(user.id, user.password)
.then(id => getRoles(id))
.catch(error => {return "admin"})
.then(user2 =>{alert(`${user2.userid} has a role which is ${user2.userrole}`);})
.catch(error => console.log(error))
.finally(() => console.log("Done!"));
/*
class Userstorage{

  loginUser(id, password){
    return new Promise((resolve, reject)=>{
      setTimeout(()=>{
        if((id === 'andy' && password === 'Anony') || (id === "Tom" && password === "code")){
          resolve(id);
        }else{
          reject("Not found!");
        }
      }, 2000);
    });

  }

  getRoles(user){
    return new Promise((reolve, reject)=>{
      setTimeout(()=>{
        if(user === "andy"){
          resolve({name: "andy", role: "master"});
        }
        else{
          reject("Not found2!");
        }
      }, 1000);
    });

  }
}

const users = new Userstorage();
const id = prompt("Enter your Id");
const password = prompt("Enter Your password");

users.
*/
