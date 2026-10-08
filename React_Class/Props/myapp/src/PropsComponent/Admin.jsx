import React from 'react'
//Destructure Props 
function Admin({image,data,city,object,children,array,}) {
  const {name , age, course, fee} = object
  const [address, contact, hobby] = array
  return (
    <div>
        <div style={{backgroundColor:"lightskyblue", padding:"20px"}}>
        <img src={image} height="100px" alt=""/>
        <p >This is Admin Class</p>
        <h4>Company: {data || "Unknown"}</h4>
        <h4>City: {city || "enter address"}</h4>
        <p>Name : {name || "Enter Name"}</p>
        <p>Age : {age || "Enter Age"}</p>
        <p>Tech : {course || "IT course"}</p>
        <p>Fee : {fee || "Avg 25000"}</p>
        <p>Address : {address}</p>
        <p>Mob : {contact}</p>
        <p>Hobby : {hobby}</p>
        </div>
        <p>{children} </p>
    </div>
  )
}

export default Admin