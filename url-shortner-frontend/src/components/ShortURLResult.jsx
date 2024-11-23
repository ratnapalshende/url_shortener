import React from 'react';

const ShortURLResult = ({ shortURL }) => {
  return (
    shortURL && (
      <div style={{ textAlign: 'center', marginTop: '20px' }}>
        <p>Your shortened URL is:</p>
        <a
          href={`http://127.0.0.1:8000/api/shorten/${shortURL}/`}
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: '#A100FF', fontWeight: 'bold' }}
        >
          http://127.0.0.1:8000/api/shorten/{shortURL}/
        </a>
      </div>
    )
  );
};

export default ShortURLResult;
