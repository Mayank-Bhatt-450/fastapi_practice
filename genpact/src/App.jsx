import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [searchText, setSearchText] = useState('');
  const [cities, setCities] = useState([]);

  const handleSearch = (e) => {
    const value = e.target.value;
    setSearchText(value);

    if (!value.trim()) {
      setCities([]); 
      return;
    }

    axios.get(`http://127.0.0.1:8000/cities/${value}`)
      .then(response => {
        setCities(response.data.cities);
      })
      .catch(error => {
        console.error('Error fetching cities:', error);
      });
  };

  return (
    <>
      <input
        type="text"
        placeholder="Enter city prefix"
        value={searchText}
        onChange={handleSearch}
      />
      <div>
        {cities.map((city, index) => (
          <div key={index}>{city}</div> 
        ))}
      </div>
    </>
  );
}

export default App;
