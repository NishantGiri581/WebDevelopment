import React, { useState } from "react";
import Child1 from "./Child1";
import contextData from "./Context";

function Provider1() {
  const [count, setCount] = useState(0); // State for the cart count
  const [input, setInput] = useState("Enter Text");
  const [select, setSelect] = useState("Select Course");
  const [cardData,setCardData] = useState("")
  const [cardCount,setCardCount] = useState(0)

  const course = "Python";
  const profile = {
    name: "Nishant",
    address: "New Delhi",
  };

  const cardDetail = {
    name: "Laptop",
    price:25000
  }

  const addToCart=()=>{
    setCardCount(cardCount + 1)
    setCardData(cardDetail)
  }

  return (
    <div className="bg-blue-300 p-5 ml-5">
      <h4>This is Provider Component</h4>
      <button
        className="bg-amber-300 rounded border-2"
        onClick={() => setCount(count + 1)}
      >
        Add
      </button>
      <button
        className="bg-pink-300 rounded border-2"
        onClick={() => setCount(count - 1)}
      >
        Sub
      </button>
      <input
        className="bg-zinc-500 rounded border-2"
        type="text"
        placeholder="enter some text"
        onChange={(event) => setInput(event.target.value)}
      />

      <select onChange={(event) => setSelect(event.target.value)}>
        <option value="">Select</option>
        <option value="Python">Python</option>
        <option value="JavaScript">JavaScript</option>
        <option value="Django">Django</option>
        <option value="Sql">Sql</option>
        <option value="React">React</option>
        <option value="Html">Html</option>
      </select>

      <button onClick={addToCart}>Add to cart</button>

      <contextData.Provider value={{ course, profile, count, input, select, cardData, cardCount}}>
        <Child1 />
      </contextData.Provider>
    </div>
  );
}

export default Provider1;
