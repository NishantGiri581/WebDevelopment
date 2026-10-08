import React from 'react'
import { ImAppleinc } from "react-icons/im";

function Icons() {
  return (
    <div>
        <div>
            <ImAppleinc className='text-4xl text-zinc-500 m-20 hover:text-green-500 hover:scale-125 duration-300'/>
        </div>
        <hr />
        <br />
        <div>
            <img src="https://i.pinimg.com/236x/98/58/74/9858745cd157f2797065e639c5b3bf23.jpg" className='w-50 h-50' alt="mage not found" />
        </div>
    </div>
  )
}

export default Icons