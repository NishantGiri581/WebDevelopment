import React from 'react'
import useCustom from './useCustom'

function Counter() {
    const [count,increment,decrement,reset] = useCustom()
  return (
    <div>
        <h3>This is Counter Component</h3>
        <h4>Counter:{count}</h4>
        <button style={{backgroundColor:"green"}} onClick={increment}>Increment</button>
        <button style={{backgroundColor:"orange"}} onClick={decrement}>Decrement</button>
        <button style={{backgroundColor:"red"}} onClick={reset}>Reset</button>
    </div>
  )
}

export default Counter