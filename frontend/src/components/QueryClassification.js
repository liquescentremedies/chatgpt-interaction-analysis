import React, { useEffect, useState } from 'react';
import axios from 'axios';

const QueryClassification = () => {
  const [classificationData, setClassificationData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchClassificationData = async () => {
      try {
        const response = await axios.get('/api/query-classification');
        setClassificationData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchClassificationData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Query Classification Results</h1>
      {classificationData && (
        <div>
          <h2>Query Categories</h2>
          <ul>
            {classificationData.map((item, index) => (
              <li key={index}>
                <strong>Query:</strong> {item.Query} <br />
                <strong>Category:</strong> {item.Category} <br />
                <strong>Keywords:</strong> {item.CategoryKeywords}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default QueryClassification;
