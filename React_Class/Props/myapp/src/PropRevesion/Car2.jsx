import React from 'react'
import Car3 from './Car3'

function Car2(prop) {
  return (
    <div>Car2
        <Car3 name={prop.name} age={prop.age} image={prop.imageUrl}/>
    </div>
  )
}

export default Car2