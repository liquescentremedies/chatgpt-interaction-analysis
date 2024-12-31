import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TopicModeling = () => {
  const [topicData, setTopicData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTopicData = async () => {
      try {
        const response = await axios.get('/api/topic-modeling');
        setTopicData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err);
        setLoading(false);
      }
    };

    fetchTopicData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Topic Modeling Results</h1>
      {topicData && (
        <div>
          <h2>Topics and Keywords</h2>
          <ul>
            {topicData.topics.map((topic, index) => (
              <li key={index}>
                <strong>Topic {index + 1}:</strong> {topic.words}
              </li>
            ))}
          </ul>

          <h2>Document Topics</h2>
          <ul>
            {topicData.documents.map((doc, index) => (
              <li key={index}>
                <strong>Query:</strong> {doc.Query} <br />
                <strong>Topic:</strong> {doc.Topic} <br />
                <strong>Probability:</strong> {doc.TopicProbability}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default TopicModeling;
