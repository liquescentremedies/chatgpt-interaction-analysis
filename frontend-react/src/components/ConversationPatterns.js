import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ConversationPatterns = () => {
  const [patternData, setPatternData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPatternData = async () => {
      try {
        const response = await axios.get('/api/conversation-patterns');
        setPatternData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchPatternData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Conversation Pattern Analysis Results</h1>
      {patternData && (
        <div>
          <h2>Top Recurring Themes</h2>
          <ul>
            {patternData['Top Themes'].map((theme, index) => (
              <li key={index}>
                {theme.word}: {theme.frequency} occurrences
              </li>
            ))}
          </ul>

          <h2>Word Cloud</h2>
          <img src={patternData['Word Cloud']} alt="Word Cloud" />
        </div>
      )}
    </div>
  );
};

export default ConversationPatterns;
