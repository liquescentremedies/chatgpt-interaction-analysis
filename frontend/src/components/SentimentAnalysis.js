import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SentimentAnalysis = () => {
  const [sentimentData, setSentimentData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSentimentData = async () => {
      try {
        const response = await axios.get('/api/sentiment-analysis');
        setSentimentData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchSentimentData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Sentiment Analysis Results</h1>
      {sentimentData && (
        <div>
          <h2>Query Sentiment Distribution</h2>
          <p>Positive Queries: {sentimentData['Query Sentiment Distribution']['Positive']}</p>
          <p>Negative Queries: {sentimentData['Query Sentiment Distribution']['Negative']}</p>
          <p>Neutral Queries: {sentimentData['Query Sentiment Distribution']['Neutral']}</p>

          <h2>Response Sentiment Distribution</h2>
          <p>Positive Responses: {sentimentData['Response Sentiment Distribution']['Positive']}</p>
          <p>Negative Responses: {sentimentData['Response Sentiment Distribution']['Negative']}</p>
          <p>Neutral Responses: {sentimentData['Response Sentiment Distribution']['Neutral']}</p>
        </div>
      )}
    </div>
  );
};

export default SentimentAnalysis;
