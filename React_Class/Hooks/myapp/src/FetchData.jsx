import React, { useEffect, useState } from "react";

function FetchData() {
  const [user, setUser] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((data) => setUser(data))
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      <h3>This is Fetch data component</h3>
      <ul>
        {
            user.map((item)=>(
                <li>key={item.id}
                <p>UserId:{item.userId}</p>
                <p>Id:{item.id}</p>
                <p>Title:{item.title}</p>
                <p>Body:{item.body}</p>
                </li>
            ))
        }
      </ul>
    </div>
  );
}

export default FetchData;
