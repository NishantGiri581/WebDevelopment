//Loop:- It is control structure that allows you to execute a block of code repeatedly
//       as long as a specified condition is true .

//for loop:- runs code a specific number of times.
// for(let i = 1; i<=3; i++){
//     console.log("Count",i);
// }

//While loop:- Runs while a condition is true.
// let i = 0;
// while (i<3){
//     console.log("Number",i);
//     i++
// }

//do while loop:- Runs once, then repeats while condition is true.
// let i = 0;
// do{
//     console.log("Iteration",i);
//     i++
// }while(i<3);

//for in loop:- Loops through object properties.
// const arr = ["a","b","c"];
// for(let i in arr){
//     console.log(i,":",arr[i]);
// }

// const obj = {name:"Nishu",age:21};
// for(let key in obj){
//     console.log(key,":",obj[key]);
// }


//for of loop:- Loops through iteerable items(like arrays, strings)
// let a = [1,2,3,4,5];
// for(let val of a){
//     console.log(val);
// }

//Nested for loop
// for(let i = 0; i<= 10; i++){
//     let row = "";
//     for(let j = 0; j<= 10; j++){
//         row += (i*j)+"\t"
//     }
//     console.log(row);
// }