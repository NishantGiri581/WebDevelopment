import React from 'react'

function SubChild(props) {
  return (
    <div style={{backgroundColor:"lightgray", padding:"20px"}}>
        <h2>This is SubChild</h2>
        <h3>Name: {props.name}</h3>
    </div>
  )
}

export default SubChild