// import React from 'react'
// import Child from './PropsComponent/Child'
// import Admin from './PropsComponent/Admin'
// import PropDrill from './PropsComponent/PropDrill'

// function App() {
//     const name = "Ducat"
//     const address = 'Delhi'
//     const imageUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnXNw9zDUCZQhISpVSSarxKxRZQ9RV6AV_pw&s"

//     const Profile={
//         name: "Nishant",
//         age: 23,
//         course: "Python",
//         fee: 35000
//     }
//     const details = ["Bihar", 8851888818, "Cricket"]

//   return (
//     <div>
//         <div style={{backgroundColor:"lightcoral", padding:"20px"}}>
//             <p> This is a Parents Class</p>
//             <Child name="Ducat" address="Delhi"/>
//             <Admin
//             data={name} 
//             city={address} 
//             image={imageUrl} 
//             object = {Profile}
//             array={details}>
//                 <h3>This is Html content</h3>
//             </Admin>
//             <hr />
//             <PropDrill/>
//         </div>
        
       
//     </div>
//   )
// }

// export default App





import React from 'react'
import Car1 from './PropRevesion/Car1'
import ResultCar from './PropRevesion/ResultCar'

function App() {
   
  const name = "Nishant"
  const age = 34
  const imageUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnXNw9zDUCZQhISpVSSarxKxRZQ9RV6AV_pw&s"

  const Profile={
        name: "Nishant",
        age: 23,
        course: "Python",
        fee: 35000
    }

  return (
    <div className='flex flex-col items-center'>
      <h3>This is App Component</h3>
      <Car1 name={name} age={age} image={imageUrl}/>
      <ResultCar name={name} age={age} image={imageUrl}/>
    </div>
  )
}

export default App