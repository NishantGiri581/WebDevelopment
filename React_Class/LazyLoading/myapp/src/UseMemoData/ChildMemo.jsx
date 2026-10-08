import React from 'react'

function ChildMemo({heavyCalculation}) {
  return (
    <div>
      <h4>This is Child Components</h4>
        <p>Value : {heavyCalculation}</p>
    </div>
  )
}

export default ChildMemo