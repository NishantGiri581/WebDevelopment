import React, { useMemo, useState, useCallback } from 'react'
import ChildMemo from '../UseMemoData/ChildMemo';


function UseCallback() {
    const [add, setAdd] = useState(0);
    const [sub, setSub] = useState(0);

    const heavyCalculation = useMemo(() => {
        let result = 0;
        for(let i = 0; i <= 99999; i++) { 
            result += 1; 
        }
        return result + add - sub; 
    }, [add, sub]);

     const resetCounters = useCallback(() => {
        setAdd(0);
        setSub(0);
    }, []); 
    
    return (
        <div>
            <h1>Total: {heavyCalculation}</h1>
            <button onClick={() => setAdd(add + 1)}>Add</button>
            <button onClick={() => setSub(sub + 1)}>Sub</button>
            <hr />
            <ChildMemo reset={resetCounters} />
        </div>
    )
}

export default UseCallback