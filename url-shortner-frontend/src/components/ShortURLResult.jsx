import React from 'react';

const ShortURLResult = ({ shortURL }) => {
  return (
    shortURL && (
      <div style={{ textAlign: 'center', marginTop: '20px' }}>
        <p>Your shortened URL is:</p>
        <a
          href={`https://url-shortener-r8k7.onrender.com/api/shorten/${shortURL}/`}
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: '#A100FF', fontWeight: 'bold' }}
        >
          https://url-shortener-r8k7.onrender.com/api/shorten/{shortURL}/
        </a>
      </div>
    )
  );
};

export default ShortURLResult;
