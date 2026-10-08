import React from "react";

function Flex() {
  return (
    <div>
      <div>
        <ul className="flex md:gap-x-20 justify-evenly md:text-2xl font-semibold md:p-5 p-3 rounded-xl">
          <li className="h-25 w-25 bg-amber-400">Box1</li>
          <li className="h-25 w-25 bg-green-400">Box2</li>
          <li className="h-25 w-25 bg-red-400">Box3</li>
          <li className="h-25 w-25 bg-blue-400">Box4</li>
        </ul>
      </div>
      <hr /><hr /><hr /><br />
      <div>
        <ul className="flex flex-col md:gap-y-20 gap-y-5 pl-5">
          <li className="h-25 w-25 bg-amber-400">Box1</li>
          <li className="h-25 w-25 bg-green-400">Box2</li>
          <li className="h-25 w-25 bg-red-400">Box3</li>
          <li className="h-25 w-25 bg-blue-400">Box4</li>
        </ul>
      </div>
    </div>
  );
}

export default Flex;
