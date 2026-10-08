import React from 'react'
import Child6Consumer from './Child6Consumer'

function Child5() {
  return (
    <div className='bg-violet-300 p-5'>
        <h4>This is Child5 Component</h4>
        <Child6Consumer/>
        </div>
  )
}

export default Child5