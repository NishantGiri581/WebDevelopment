import React, {useMemo, useState } from 'react'
import ChildMemo from './ChildMemo';

function UseMemoData() {
    const [add, setAdd] = useState(0);
    const [sub, setSub] = useState(0); // Initialize at 0

    const heavyCalculation = useMemo(() => {
        console.log("Running heavy calculation...");
        let result = 0;
        for(let i = 0; i <= 99999; i++) {
           result += 1;
        }
        
        return result + add - sub; 
    }, [add, sub]); 

    return (
        <div>
            <h1>Total: {heavyCalculation}</h1>
            <button onClick={() => setAdd(add + 1)}>Add : ({add})</button>
            <br />
            <button onClick={() => setSub(sub + 1)}>Sub : ({sub})</button>
            <hr />
            <ChildMemo heavyCalculation={heavyCalculation}/>
        </div>
    )
}

export default UseMemoData;