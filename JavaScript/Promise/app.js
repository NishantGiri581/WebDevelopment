// Promise :- It is an object and a constructor used to handle asynchronous operation.
//         :- It is a constructor that returns a promise object, which represent the eventual
//            completion or failure of an asynchronous task.

//Syntax:- 

// let promise = new Promise((resolve, reject)=>{
//     let isSuccess = true;
//     if(isSuccess){
//         resolve("Promise is resolved");
//     }else{
//         reject("Promise is rejected");
//     }
// })

// .then((result)=> console.log(result))
// .catch((error)=> console.log(error))




// let promise = new Promise((resolve, reject)=>{
//     let num = 2;
//     if(num%2==0){
//         resolve("Promise is resolved and num is even");
//     }else{
//         reject("Promise is rejected and num is odd");
//     }
// })

// .then((result)=> console.log(result))
// .catch((error)=> console.log(error))


// Api Calling Data
// const getData = fetch("https://jsonplaceholder.typicode.com/posts/1")
// .then((res)=>res.json())
// .then((data)=>console.log(data))
// .catch((err)=>console.log(err))




// let checkEven = new Promise((resolve,reject)=>{
//     let number = 4;
//     if(number % 2 === 0){
//         resolve("The number is even!");
//     }
//     else{
//         reject("The number is odd!");
//     }
// });

// checkEven
// .then((message)=> console.log(message)) //on success
// .catch((error)=> console.log(message)); //on failure


//Advanced Promise methods
//1) Promise.all() :- it take an array of promises and returns a single promise that
//                    resolve when all of promise are resolved, or rejects if any one fails.

// Promise.all([promise1,promise2,promise3])
// .then(results => console.log(results))
// .catch(error=> console.log(error));

// const p1 =  Promise.resolve("Get Html Code")
// const p2 =  Promise.resolve("Get CSS Code")
// const p3 =  Promise.resolve("Get JavaScript Code")
// Promise.all([p1,p2,p3])
// .then((result) => console.log(result));



// const getData1 =   fetch("https://jsonplaceholder.typicode.com/posts/1")
// .then(res => res.json())
// .then((data)=>console.log(data))
// .catch((err)=>console.log(err))

// const getData2 =   fetch("https://jsonplaceholder.typicode.com/users/1")
// .then(res => res.json())
// .then((data)=>console.log(data))
// .catch((err)=>console.log(err))

// const getData3 =   fetch("https://jsonplaceholder.typicode.com/comments/1")
// .then(res => res.json())
// .then((data)=>console.log(data))
// .catch((err)=>console.log(err))


//2) 


// const delay = (ms) => new Promise(resolve => setTimeout(resolve , ms));
// console.log("Start")
// delay(2000).then(()=>console.log("Show After 2 Second"));

