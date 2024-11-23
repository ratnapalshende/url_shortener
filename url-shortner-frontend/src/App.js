import React, { useState } from 'react';
import './App.css';

function App() {
  const [url, setUrl] = useState('');
  const [shortenedUrl, setShortenedUrl] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!url) {
      setError('Please enter a valid URL.');
      return;
    }

    try {
      // Make a request to your Django backend API
      const response = await fetch('http://localhost:8000/api/shorten/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      if (response.ok) {
        const data = await response.json();
        setShortenedUrl(`http://localhost:8000/api/${data.shortCode}/`);
        setError('');
      } else {
        const data = await response.json();
        setError(data.message || 'Something went wrong.');
      }
    } catch (error) {
      setError('Failed to connect to the server.');
    }
  };

  return (
    <div className="App" style={{ textAlign: 'center', padding: '50px' }}>
      <h1 style={{ color: '#A100FF' }}>URL Shortener</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="url"
          placeholder="Enter URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          style={{ padding: '10px', width: '300px', marginBottom: '10px' }}
        />
        <button type="submit" style={{ padding: '10px', cursor: 'pointer', marginLeft: '10px' }}>
          Shorten URL
        </button>
      </form>

      {shortenedUrl && (
        <div>
          <h3>Shortened URL:</h3>
          <a href={shortenedUrl} target="_blank" rel="noopener noreferrer">
            {shortenedUrl}
          </a>
        </div>
      )}

      {error && (
        <div style={{ color: 'red', marginTop: '20px' }}>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default App;
