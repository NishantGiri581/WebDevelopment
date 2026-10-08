import React from 'react'
import AllCar from './AllCar'

function Car3(prop) {
  return (
    <div>Car3
        <AllCar name={prop.name} age={prop.age} image={prop.imageUrl}/>
    </div>
  )
}

export default Car3