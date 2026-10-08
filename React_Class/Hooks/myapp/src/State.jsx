import React, {useState} from 'react'

function State() {
    const [name,setName] = useState("Nishant Giri")
    
    const changeName =()=>{
        setName("Nishu")
        console.log(name)
    }

    const name1 = "Ducat India"
    const handleChangeName = () => {
      const name1 = "Ducat New Delhi"
      console.log(name1)
    }

  return (
    <div>
        <h4>Name: {name}</h4>
        <button onClick={changeName}>Click for State Change</button>
         <h4>Name: {name1}</h4>
        <button onClick={handleChangeName}>Click for Variable Change</button>
    </div>
  )
}

export default State