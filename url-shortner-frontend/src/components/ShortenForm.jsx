import React, { useState } from 'react';
import axios from 'axios';

const ShortenForm = ({ setShortURL }) => {
  const [longURL, setLongURL] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const response = await axios.post('https://url-shortener-r8k7.onrender.com/api/shorten/', { url: longURL });
      setShortURL(response.data.shortCode);
    } catch (err) {
      setError('Error creating short URL. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ margin: '20px auto', maxWidth: '500px' }}>
      <input
        type="url"
        placeholder="Enter your long URL here"
        value={longURL}
        onChange={(e) => setLongURL(e.target.value)}
        style={{
          width: '100%',
          padding: '10px',
          borderRadius: '5px',
          border: '1px solid #ccc',
        }}
        required
      />
      <button
        type="submit"
        style={{
          marginTop: '10px',
          width: '100%',
          padding: '10px',
          borderRadius: '5px',
          backgroundColor: '#A100FF', // Accenture theme color
          color: '#fff',
          border: 'none',
        }}
      >
        Shorten URL
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
};

export default ShortenForm;
