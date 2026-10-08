// Timer Function is used to schedule code execution --- either once after delay or repeatedly at regular intervals.
//Type of timer function.

//1) setTimeout:- It is used to execute a function once after a specified delay(in milliseconds).
//Syntax:- 
// setTimeout(Callback,delay);

//callback function:- function to run
//delay:- Time in milliseconds(1000ms = 1 second)

//Syntax:-
//  setTimeout(()=>{
//     console.log("TimerFunction running");
// },timeout);

// console.log("start"); 
// setTimeout(()=>{
//     console.log("TimerFunction running");
// }, 3000);
// console.log("End");


// const cleartimer = setTimeout(()=>{
//     function add(a,b){
//         return a+b
//     }
//     console.log(add(10,5));
// }, 3000);
//  clearTimeout(cleartimer); to stop time and not run function


//2) setInterval:- the code is execute after some time interval and it stop by control + c.
// It execute continuously
// setInterval(()=>{
//     console.log("hello");
// },3000);


// const timer = setInterval(()=>{
//    function add(a,b){
//     return a+b
//    }
//    console.log(add(10,5));
// },3000);



// let count = 5;
// const timer = setInterval(()=>{
//     console.log(`Counter Started : ${count}`);
//     count--;
//     if(count < 0){
//         clearInterval(timer)
//         console.log("Your Time is off");
//     }
// },2000)



// const timer = setInterval(()=>{
//    for (let i = 10; i >= 1; i--) {
//    console.log(i);
 
// }
// },2000)

