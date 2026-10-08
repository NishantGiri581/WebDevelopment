import React from "react";

function AllCar(props) {
  return (
    <div className="bg-amber-400 h-50 w-80">
      <h1 className="text-3xl">AllCar</h1>
      <p>name : {props.name}</p>
      <p>age : {props.age}</p>
      <img src={props.image} alt="loading...." style={{ height: "100px" }} />
      
    </div>
  );
}

export default AllCar;
