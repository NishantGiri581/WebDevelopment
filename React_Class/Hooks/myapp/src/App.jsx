import React from 'react'
import State from './State'
import SideEffect from './SideEffect'
import UseEffect from './UseEffect'
import FetchData from './FetchData'
import Axios from './Axios'
import Counter from './customHook/Counter'
import Counter1 from './customHook/Counter1'

function App() {
  return (
    <div>
        <UseEffect/>
        <State/> 
        <SideEffect/>
        <FetchData/>
        <Axios/>
        <Counter/>
        <Counter1/>
    </div>
  )
}

export default App