/* 
Variables :- It is a container used to store data.
          :- Three keywords in JavaScript
             1) var,
             2) let,
             3) const
*/
//Scope in JS :- It define where variables cab accessed or used in a program.
//            :- Types of Scope in JS :
            
//1) Global Scope:- Declare outside all functions/blocks and access anywhere in the code.
// let a = 20;
// function test(){
//     console.log(a);
// }

//2) Lexical Scope:- Inner functions can access variables of outer function.
//i) function Scope:- declare inside a function using var, let, const. Accessiable inside the function.
// function show(){
//     let x = 5;
//     console.log(x);
// }
// console.log(x); // Error

//ii) Block Scope:- Declare inside {} , access inside only.
// {
//     let a = 20;
//     console.log(a);
// }

// let y = 10;
// console.log(typeof y); //typeof is a operator used to find data type of a variables.
//         Number 

