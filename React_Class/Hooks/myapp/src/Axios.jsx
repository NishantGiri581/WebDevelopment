import React, { useEffect, useState } from "react";
import axios from "axios";

function Axios() {
  const [user, setUser] = useState([]);

  const fetchData = async () => {
    try {
      const response = await axios.get(
        "https://jsonplaceholder.typicode.com/posts"
      );
      setUser(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <h3>This is Fetch data component</h3>
      <ul>
        {user.map((item) => (
          <li>
            key={item.id}
            <p>UserId:{item.userId}</p>
            <p>Id:{item.id}</p>
            <p>Title:{item.title}</p>
            <p>Body:{item.body}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Axios;
