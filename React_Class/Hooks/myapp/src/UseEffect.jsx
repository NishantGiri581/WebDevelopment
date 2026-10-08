import React, { useEffect, useState } from 'react'

function UseEffect() {
    const [count,setCount] = useState(0)

    useEffect(()=>{
        function effect(){
          console.log("This is effect function")
        }
        effect();
     },[]);
    

  return (
    <div>
        <h2>Count:{count}</h2>
        <button onClick={()=> setCount(count+1)}>Increment</button>
    </div>
  )
}

export default UseEffect