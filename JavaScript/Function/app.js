//Function:- Functions are resuable blocks of code designed to perform specific tasks.
// function sum(x,y){
//     return x+y
// }
// console.log(sum(4,5));

// Types of function:-
//1) Named function:- declare by name keywords
// function greet(name){
//     return "Hello,"+ name;
// }
// console.log(greet("Nishant"));

//2) Function Expression:- Function Assigned to a variables
// const add = function(a,b){
//     return a+b
// }
// console.log(add(2,3));

//3) Arrow Function(ES6):- provide a short syntax, usefull in callbacks and method.
// const multiply = (a,b) => a*b;
// console.log(multiply(3,4));

//4) Anonymous function:- Does not have a name, used as a value.
// const greet = function(){
//     console.log("Hello");
// }
// greet();

//IIFE Immediately Invoked Function Expression:- wrapped in parentheses and follow by another set.
// (function(){
//     console.log("IIFE Executed");
// })();




//Callback Function in JavaScript:-
//It is passed as an argument to another function and is executed after main function completes.
//Used in async operations.

// function greet(name,callback){
//     console.log("hello,"+name);
//     callback();
// }
//   greet("Nishant",function(){
//     console.log("Welcome to home");
//   })

//Example
//   setTimeout(function() {
//   console.log("This runs after 2 seconds.");
// }, 2000);

//Callback Hell:- happens when you nest too many callback functions inside each other, making the code:
// getUser(userId, function(user) {
//   getPosts(user.id, function(posts) {
//     getComments(posts[0].id, function(comments) {
//       console.log('User:', user);
//       console.log('Posts:', posts);
//       console.log('Comments:', comments);
//     });
//   });
// });

// Solution of callback hell function by use of 
//      1)         Modularize your code.
//            Break up callbacks into named functions.
//      2)         Use Promises
//            Promises flatten the structure and make it readable.
//      3)         Use async/await
//            (cleanest option)


// Pure Function:-
// A pure function always produces the same output for the same input and has no side effects.
// function pureadd(a,b){
//     return a+b;
// }
// console.log(pureadd(2,3)); //5

// Impure Function:-
// An impure function may produce different outputs for the same input or have side effects.
// let counter = 0;
// function increment(){
//     counter++;
//     return counter;
// }
// console.log(increment()); //1
// console.log(increment()); //2
// console.log(increment()); //3
// The increment function is impure because it modifies the external variable counter.
