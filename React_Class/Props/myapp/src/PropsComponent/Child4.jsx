import React from 'react'
import Child5Data from './Child5Data'

function Child4(props) {
  return (
    <div>Child4
        <Child5Data data={props.data}/>
    </div>
  )
}

export default Child4