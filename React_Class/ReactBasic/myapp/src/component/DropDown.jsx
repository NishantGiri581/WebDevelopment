import React from 'react'

function DropDown() {
  return (
    <div>
        <ul className='flex gap-x-20 justify-center'>
            <li className='group relative hover:text-red-400'>State
            <ul className='invisible group-hover:visible bg-zinc-400 text-white p-3  rounded-lg  w-64px border-2 border-black absolute'>
                <li className='hover:text-amber-200'>Bihar</li>
                <li className='hover:text-amber-200'>Punjab</li>
                <li className='hover:text-amber-200'>Gujarat</li>
                <li className='hover:text-amber-200'>Assam</li>
            </ul>
            </li>

            <li className='group relative hover:text-red-400'>City
                <ul className='invisible group-hover:visible bg-zinc-400 text-white p-3  rounded-lg  w-64px border-2 border-black absolute'>
                <li className='hover:text-amber-300'>Patna</li>
                <li className='hover:text-amber-300'>Chandighar</li>
                <li className='hover:text-amber-300'>Sawarmati</li>
                <li className='hover:text-amber-300'>Dispur</li>
            </ul>
            </li>

            <li className='group relative hover:text-red-400'>MLA
                <ul className='invisible group-hover:visible bg-zinc-400 text-white p-3  rounded-lg  w-64px border-2 border-black absolute'>
                <li className='hover:text-amber-200'>Nishant</li>
                <li className='hover:text-amber-200'>Sonu</li>
                <li className='hover:text-amber-200'>Rohit</li>
                <li className='hover:text-amber-200'>Babu</li>
            </ul>
            </li>
        </ul>
    </div>
  )
}

export default DropDown