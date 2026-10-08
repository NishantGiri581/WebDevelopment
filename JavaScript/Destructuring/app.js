//Destructuring:- It is a JS expression that allows you to extract data from arrays or objects into distinct variables.

// let obj = {
//     name : "Nishant",
//     age : 24,
//     job : "Python Developer"
// }

// console.log(obj.age);

//Destructuring 
// const{name,age,job} = obj
// console.log(age);


// let obj = {
//     name : "Nishant",
//     age : 24,
//     details: {
//         job : "Python Developer",
//         price : {
//             total : 4500,
//             size : {
//                 width : 300,
//                 height : 400
//             },
//         },
//     },
//     game : "Cricket"
// };

// console.log(obj.details.price.size.height); // using dot method

//Destructuring
// const{name,age,details:{job,price:{total,size:{width,height}}}} = obj
// console.log(height);


//In Aarry list append
// let arr = ["Nishant","Sonu","Aditya",["Rohan","Arti",["Boss","Spider"]]];
// console.log(arr[3][2][1]);


//For Array
// let arr = ["Nishant",24,"Delhi"]
// const[name,age,city] = arr
// console.log(age);

//Destructuring 
// const[name,age,city]=  ["Nishant",24,"Delhi"];
// console.log(age);