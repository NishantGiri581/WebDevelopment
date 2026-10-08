import React, { useState } from 'react'

function useCustom(parameter=0) {
    const [count,setCount] = useState(parameter)

    const increment =()=>{
        setCount(count+1)
    }
      const decrement =()=>{
        setCount(count-1)
    }
      const reset =()=>{
        setCount(0)
    }
      const multi =(value)=>{
        setCount(count*value)
    }
  return [count,increment,decrement,reset,multi];
}
export default useCustom