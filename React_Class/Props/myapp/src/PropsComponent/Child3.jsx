import React from 'react'
import Child4 from './Child4'

function Child3(props) {
  return (
    <div>Child3
        <Child4 data={props.data}/>
        <h3>Name : {props.data}</h3>
    </div>
  )
}

export default Child3