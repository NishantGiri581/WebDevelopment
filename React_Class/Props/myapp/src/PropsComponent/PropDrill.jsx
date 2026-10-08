import React from 'react'
import Child1 from './Child1'

function PropDrill() {
    const data = "Ducat India"
  return (
    <div>
        PropDrill
        <Child1 data={data}/>
    </div>
  )
}

export default PropDrill