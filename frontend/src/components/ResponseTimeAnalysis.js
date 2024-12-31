import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ResponseTimeAnalysis = () => {
  const [responseTimeData, setResponseTimeData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchResponseTimeData = async () => {
      try {
        const response = await axios.get('/api/response-time-analysis');
        setResponseTimeData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchResponseTimeData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Response Time Analysis Results</h1>
      {responseTimeData && (
        <div>
          <h2>Response Time Statistics</h2>
          <p>Mean Response Time: {responseTimeData.mean} seconds</p>
          <p>Median Response Time: {responseTimeData.median} seconds</p>
          <p>Standard Deviation: {responseTimeData.std} seconds</p>
          <p>Minimum Response Time: {responseTimeData.min} seconds</p>
          <p>Maximum Response Time: {responseTimeData.max} seconds</p>

          <h2>Response Time Distribution</h2>
          <img src={responseTimeData.distribution} alt="Response Time Distribution" />
        </div>
      )}
    </div>
  );
};

export default ResponseTimeAnalysis;
