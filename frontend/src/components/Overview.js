import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Overview = () => {
  const [overviewData, setOverviewData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOverviewData = async () => {
      try {
        const response = await axios.get('/api/overview');
        setOverviewData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchOverviewData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Overview Analysis Results</h1>
      {overviewData && (
        <div>
          <h2>Summary</h2>
          <p>Total Interactions: {overviewData.Overview['Total Interactions']}</p>
          <p>Unique Topics: {overviewData.Overview['Unique Topics']}</p>
          <p>Query Categories: {overviewData.Overview['Query Categories']}</p>

          <h2>Sentiment Analysis</h2>
          <p>Positive Queries: {overviewData['Sentiment Analysis']['Positive Queries']}</p>
          <p>Negative Queries: {overviewData['Sentiment Analysis']['Negative Queries']}</p>
          <p>Neutral Queries: {overviewData['Sentiment Analysis']['Neutral Queries']}</p>

          <h2>Response Times</h2>
          <p>Average Response Time: {overviewData['Response Times']['Average Response Time']}</p>
          <p>Fastest Response: {overviewData['Response Times']['Fastest Response']}</p>
          <p>Slowest Response: {overviewData['Response Times']['Slowest Response']}</p>

          <h2>Top Themes</h2>
          <ul>
            {overviewData['Top Themes'].map((theme, index) => (
              <li key={index}>
                {theme.word}: {theme.frequency} occurrences
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Overview;
