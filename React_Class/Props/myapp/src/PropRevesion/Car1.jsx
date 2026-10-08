import React from 'react'
import Car2 from './Car2'

function Car1(prop) {
  return (
    <div>Car1
        <Car2 name={prop.name} age={prop.age} image={prop.imageUrl}/>
    </div>
  )
}

export default Car1