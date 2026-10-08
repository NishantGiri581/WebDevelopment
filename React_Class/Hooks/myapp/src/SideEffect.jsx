import React, { useEffect, useState } from 'react'

function SideEffect() {
    const [count, setCount] = useState(0)
    const [data , setData] = useState(40)
    const [hello , setHello] = useState(10)
    
    useEffect(()=>{
      function effect(){
        console.log("This is Effect")
      }
      effect();
    },[hello])

   

  return (
    <div>
        <h2>count :{count}</h2>
        <h2>Data: {data}</h2>
        <h2>Hello: {hello}</h2>
        <button className='bg-red' onClick={()=> setCount(count+1)}>Increment</button>
        <button className='bg-red' onClick={()=> setData(data - 2)}>Decrement</button>
        <button className='bg-red' onClick={()=> setHello(hello * 5)}>Multiply</button>
    </div>
  )
}

export default SideEffect