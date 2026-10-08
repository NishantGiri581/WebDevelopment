import React from 'react'

function Grid() {
  return (
    <div>
        <div className='grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 
        gap-x-5 gap-y-5 m-3 border-black rounded-lg'>
            <div className='bg-red-400 h-20 rounded-lg col-span-2'></div>
            <div className='bg-green-400 h-20 rounded-lg '></div>
            <div className='bg-yellow-400 h-20 rounded-lg'></div>
            <div className='bg-blue-400 h-20 rounded-lg'></div>
            <div className='bg-black h-20 rounded-lg'></div>
            <div className='bg-pink-400 h-20 rounded-lg'></div>
            <div className='bg-zinc-400 h-20 rounded-lg'></div>
            <div className='bg-orange-400 h-20 rounded-lg '></div>
        </div>
    </div>
  )
}

export default Grid