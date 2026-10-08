import React from 'react'

function Nav() {
  return (
    <div>
       <nav className='bg-blue-400 md:p-5 p-3 md:font-bold rounded-2xl'>
        <ul className='flex justify-around flex-direction: row space-x-4'>
            <li className='hover:text-red-400'>Home</li>
            <li className='hover:text-red-400'>Contact</li>
            <li className='hover:text-red-400'>Service</li>
            <li className='hover:text-red-400'>About</li>
            <li className='hover:text-red-400'>sign in</li>
        </ul>
       </nav>
    </div>
  )
}

export default Nav