// Array:- It is data structure used to store multiple values in a ordered list in a single variables.
// it start with zero index of elements.

// const arr = [1,2,3,4,5,6];
// console.log(arr.length);
// console.log(arr[2]);


//CREATE ARRAY
//1) Using Literal => using Square bracket[].
// const arr1 = [1,2,3,4,5,6];
// console.log(arr1);

//2) Using Constructor => use of new keywords.
// let arr = new Array(10,20,30);
// console.log(arr);

//BASIC OPERATIONS ON JAVASCRIPT ARRAYS OR METHOD
//1) Accessing Elements of an Array:- using of index start with zero.
// let arr = ["HTML","CSS","JAVASCRIPT"];
// console.log(arr[1]);

//2) Accessing the Last Elements
// let arr = ["HTML","CSS","JAVASCRIPT"];
// console.log(arr[arr.length-1]);

//3)Modifying array elements
// let arr = ["HTML","CSS","JAVASCRIPT"];
// arr[1]="Python"
// console.log(arr);

//4) Array length
//  let arr = ["HTML","CSS","JAVASCRIPT"];
//  console.log(arr.length);

//5) Array toString()
// let arr = ["HTML","CSS","JAVASCRIPT"];
// console.log(arr.toString());

//6) Array Join()
// let arr = ["HTML","CSS","JAVASCRIPT"];
// console.log(arr.join("|"));

//7) Array Delete
// let arr = ["HTML","CSS","JAVASCRIPT"];
// delete arr[2];
// console.log(arr);

//8) array concat()
// let arr1 = [1,2,3];
// let arr2 = [4,5,6];
// let arr3 = [7,8,9];
// let arr4 = arr1.concat(arr2.concat(arr3));
// console.log(arr4);

//9) array flat()
// let arr = ["HTML","CSS","JAVASCRIPT",["Python","C++",[1,2,3]]];
// console.log(arr.flat());

//10) array Push()  
// let arr = ["HTML","CSS","JAVASCRIPT"];
// let newArray = arr.push("Python")
// console.log(arr); 
// console.log(newArray); // length provide 4

//11) array unshift()
// let fruits = ["Banana", "Mango"];
// let newLength = fruits.unshift("Apple");
// console.log(fruits);      // ["Apple", "Banana", "Mango"]
// console.log(newLength);   // 3


//12) Array pop()
// let fruits = ["Apple", "Banana", "Mango"];
// let removed = fruits.pop();
// console.log(fruits);   // ["Apple", "Banana"]
// console.log(removed);  // "Mango"

//13) array shift()
// let fruits = ["Apple", "Banana", "Mango"];
// let removed = fruits.shift();

// console.log(fruits);   // ["Banana", "Mango"]
// console.log(removed);  // "Apple"

//14) Array splice()
// let fruits = ["Apple", "Banana", "Mango", "Orange"];
// let removed = fruits.splice(1, 2);  

// console.log(fruits);   // ["Apple", "Orange"]
// console.log(removed);  // ["Banana", "Mango"]

//15) Array slice()
// let fruits = ["Apple", "Banana", "Mango", "Orange"];
// let result = fruits.slice(1, 3);

// console.log(result);   // ["Banana", "Mango"]
// console.log(fruits);   // ["Apple", "Banana", "Mango", "Orange"] (unchanged)

//16) array some() Method
// let numbers = [1, 3, 5, 7, 8];
// let result = numbers.some(num => num % 2 === 0);

// console.log(result); // true (because 8 is even)

//17) Array Map() Method
// let numbers = [1, 2, 3, 4];
// let doubled = numbers.map(num => num * 2);

// console.log(doubled); // [2, 4, 6, 8]
// console.log(numbers); // [1, 2, 3, 4] (unchanged)

//18) Array Filter() Method
// let numbers = [1, 2, 3, 4, 5, 6];
// let evens = numbers.filter(num => num % 2 === 0);

// console.log(evens); // [2, 4, 6]


//19) Array Reduce() Method
// let numbers = [1, 2, 3, 4, 5];
// let sum = numbers.reduce((acc, num) => acc + num, 0);

// console.log(sum); // 15

//20) Array Reverse() Method
// let numbers = [1, 2, 3, 4, 5];
// numbers.reverse();

// console.log(numbers); // [5, 4, 3, 2, 1]

//21) Array Values() Method
// let numbers = [10, 20, 30];
// let iterator = numbers.values();

// for (let value of iterator) {
//   console.log(value);
// }


// let arr = [1,2,3,4,5];
// arr.reverse();

