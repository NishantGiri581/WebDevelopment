import React from 'react'
import Child2 from './Child2'

function Child1() {
  return (
    <div className='bg-red-300 p-5'>
        <h4>This is Child1 Component</h4>
        <Child2/>
    </div>
  )
}

export default Child1