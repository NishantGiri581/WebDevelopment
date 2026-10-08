import React from "react";

function ResultCar(props) {
  return (
    <div>
      <div className="bg-red-300 h-60 w-80">
        <p>This is ResultCar Component</p>
        <p>name : {props.name}</p>
        <p>age : {props.age}</p>
        <img src={props.image} alt="loading...." style={{ height: "100px" }} />
      </div>
    </div>
  );
}

export default ResultCar;
