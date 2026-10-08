// Object:- An object is a non premitive data type used to store key-value pairs.

//Two primary way two create object in javaScript.

//1)Object Constructor:- An object constructor is a special type of function used to create multiple objects with the same structure.
// let obj = new Object();
// obj.name = "Nishant",
// obj.age = 23,
// obj.job = "Python Developer"
// console.log(obj);



//2)Object Literal :- An object literal is a list of name:value pairs inside curly{}braces.

// let obj = {
//     name: "Nishant",
//     age: 23,
//     job: "Python Developer"
// }
// console.log(obj);
// console.log(obj.name); //1) Accessing by dot(.)in object.

// let arr = ["Nishant","sonu","Aditya","Adarsh","Akash","Mann","Yogesh","Keshav"]
// console.log(arr);
// console.log(arr[2]);  //1)Accessing by index[]in arr.



// let obj = {
//     name: "Nishant",
//     age: 23,
//     job: "Python Developer"
// }
// obj.age = 24; //2) Modifying and Adding by reassigning their value in object.
// console.log(obj);


// let arr = ["Nishant","sonu","Aditya","Adarsh","Akash","Mann","Yogesh","Keshav"]
// console.log(arr);
// console.log(arr[2]); //2)Change a Specific Element by Index in array.

//2)Removing Properties
// let obj = {model:"Tesla",color:"Red"}
// delete obj.color;
// console.log(obj);


//Nested Object in JavaScript :- An object inside another object.
// const Student = {
//     name:"Nishu",
//     Address:{ city:"Delhi", pin:110008},
//     marks:{math:90, Science:70}
// }
// //Student.address.city = "Mumbai";  Update nested value
// //delete Student.address.city;
// console.log(Student.Address.city);



//Object Method :- Function inside that object , function definition stored as a property value.
// const Person = {
//     firstName:"Nishant",
//     lastName:"Giri",
//     id : 581,

//     fullName: function(){
//         return this.firstName+" "+this.lastName;
//     }
// };
// console.log(Person.fullName());


//Classes : Class is a program-code template for creating objects. It have some variables and some function.
// class MyClass {
//     constructor(){}
//     myMethod(){}
// }
// let myObj = new MyClass();


// class ToyotaCar{
//     start(){
//         console.log("Start");
//     }
//     stop(){
//         console.log("Stop");
//     }
//     setBrand(brand){
//         this.brand = brand;
//     }
// }
// let fortuner = new ToyotaCar();
// fortuner.setBrand("Fortuner")
// console.log(fortuner); 
// console.log(typeof fortuner); 
// console.log(fortuner.start()); 
// console.log(fortuner.stop()); 


//Inheritance :(( It is passing down properties and methods from parents class to child class.

// class Person{
//     constructor(){
//         this.species = "Homo sapiens";
//     }
//     eat(){
//         console.log("Eat");
//     }
//     sleep(){
//         console.log("Sleep");
//     }
//      work(){
//         console.log("Not Solve");
//     } 
// }
// class Engineer extends Person{
//     work(){
//         console.log("Solve problem");
//     } 
// } 
// let NishantObj = new Engineer();
// console.log(NishantObj.eat());
// let p1 = new Person()
// console.log(p1.species);

