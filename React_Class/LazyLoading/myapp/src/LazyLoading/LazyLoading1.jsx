import React, { Suspense, useState } from 'react'
const LazyData=React.lazy(()=>import('./LazyData'))

function LazyLoading1() {

  const [load , setLoad]=useState(false)


  return (
    <div>
        <h3 className='text-3xl text-red-400 font-bold'>This is main component</h3>

        <button onClick={()=>setLoad(true)}>Click</button>
        {
        load?
        <Suspense fallback={<h3><b>Loading......</b><h3/></h3>}>
           <LazyData/>
        </Suspense>
        :null
        }
   
    </div>
  )
}

export default LazyLoading1