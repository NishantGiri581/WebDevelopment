import React from 'react'

import { useSelector } from 'react-redux'

function App() {

  const count = useSelector((state)=>state.counter.value)
  return (
    <div>
  
      <Store/>
       <p>count : {count}</p>
    </div>
  )
}

export default App