import React from 'react'
import SubChild from './SubChild'

function Child(Props) {
    console.log(Props)
  return (
    <div>
        <div style={{backgroundColor:"lightgreen", padding:"20px"}}>
            <h2> This is Child Class</h2>
            <h3>Name : {Props.name}</h3>
            <h3>City : {Props.address}</h3>
            <SubChild name="Boss"/>
        </div>
        

    </div>
  )
}

export default Child