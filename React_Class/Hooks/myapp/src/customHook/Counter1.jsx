import React from 'react'
import useCustom from './useCustom'

function Counter1() {
  const [count,increment,decrement,reset,multi] = useCustom()
  return (
    <div>
        <h3>This is Counter Component</h3>
        <h4>Counter1 : {count}</h4>
        <button style={{backgroundColor:"green"}} onClick={increment}>Increment</button>
        <button style={{backgroundColor:"orange"}} onClick={decrement}>Decrement</button>
        <button style={{backgroundColor:"red"}} onClick={reset}>Reset</button>
        <button style={{backgroundColor:"skyblue"}} onClick={()=>multi(3)}>Multiply</button>
    </div>
  )
}

export default Counter1