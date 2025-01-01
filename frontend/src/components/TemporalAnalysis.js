import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TemporalAnalysis = () => {
  const [temporalData, setTemporalData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTemporalData = async () => {
      try {
        const response = await axios.get('/api/temporal-analysis');
        setTemporalData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchTemporalData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Temporal Analysis Results</h1>
      {temporalData && (
        <div>
          <h2>Interaction Frequency Over Time</h2>
          <img src={temporalData['Interaction Frequency Over Time']} alt="Interaction Frequency Over Time" />

          <h2>Engagement Trends (7-day Moving Average)</h2>
          <img src={temporalData['Engagement Trends']} alt="Engagement Trends" />
        </div>
      )}
    </div>
  );
};

export default TemporalAnalysis;
