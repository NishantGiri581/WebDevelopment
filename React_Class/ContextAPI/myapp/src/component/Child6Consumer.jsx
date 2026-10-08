import React, { useContext } from "react";
import contextData from "./Context";

function Child6Consumer() {
  //Destructuring
  const {
    course,
    profile: { name, address },
    count,
    input,
    select,
    cardData,
    cardCount
  } = useContext(contextData);

  return (
    <div className="bg-zinc-400 p-7">
      Consumer Component
      <p>Count: **{count}**</p>
      <p>Course : {course}</p>
      <p>Name : {name}</p>
      <p>City : {address}</p>
      <p>Input Text : {input}</p>
      <p>Selected Course : {select}</p>
      <p>Card Item Name: {cardData.name}</p>
      <p>Card Item Price : {cardData.price}</p>
      <p>Count item: {cardCount}</p>
      <p>Total Price: {cardCount * cardData.price}</p>
    </div>
  );
}

export default Child6Consumer;
