

// const getdata = async()=>{
//     try{
//         const response = await fetch("https://jsonplaceholder.typicode.com/posts/1")
//         const data = await response.json()
//         console.log(data);
//     }catch(err){
//         console.log(err);
//     }
// }
// getdata()

// through Id
// const element = document.getElementById("id_main")
// console.log(element);

// const ducat = document.getElementById("id_heading")
// console.log("Heading",ducat);



//Through Class
// const element = document.getElementsByClassName("class_main")[0]
// console.log(element);

// const ducat = document.getElementsByClassName("heading")[0]
// console.log("Heading",ducat);


//Using Tag Name
// const element = document.getElementsByTagName("div")[0]
// console.log(element);


//Query Selector
// const element = document.querySelector("#id_main")
// console.log(element);

// const element = document.querySelector(".class_main")
// console.log(element);

// const element = document.querySelectorAll(".class_main")[3]
// console.log(element);

// const element = document.querySelectorAll("h1")[0]
// console.log(element);




//Fetch Api : It provide interface for fetching resources
//AJAX : Asynchronous js and xml
//JSON : JavaScript Object Notation
//json() method: returns a second promise that resolve with result pf parsing the response body text as JSON.


// const URL = "https://jsonplaceholder.typicode.com/users";
// const factPara = document.querySelector("#fact");
// const btn = document.querySelector("#btn");

// const getFacts = async () => {
//         console.log("Getting data ....");
//         let response = await fetch(URL);
//         console.log(response);
//         let data = await response.json();
//         factPara.innerText = data[5].email;
// };
// console.log(getFacts());
// btn.addEventListener("click",getFacts);


/////using promise chain/////
// const URL = "https://jsonplaceholder.typicode.com/users";
// const factPara = document.querySelector("#fact");
// const btn = document.querySelector("#btn");

// function getFacts(){
//     fetch(URL).then((response)=>{
//         return response.json();
//     }).then((data)=>{
//         console.log(data);
//         factPara.innerText = data[9].email;
//     })
// }

// btn.addEventListener("click",getFacts);


