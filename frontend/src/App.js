import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Overview from './components/Overview';
import SentimentAnalysis from './components/SentimentAnalysis';
import TemporalAnalysis from './components/TemporalAnalysis';
import TopicModeling from './components/TopicModeling';
import QueryClassification from './components/QueryClassification';
import ResponseTimeAnalysis from './components/ResponseTimeAnalysis';
import ConversationPatterns from './components/ConversationPatterns';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/overview" component={Overview} />
          <Route path="/sentiment-analysis" component={SentimentAnalysis} />
          <Route path="/temporal-analysis" component={TemporalAnalysis} />
          <Route path="/topic-modeling" component={TopicModeling} />
          <Route path="/query-classification" component={QueryClassification} />
          <Route path="/response-time-analysis" component={ResponseTimeAnalysis} />
          <Route path="/conversation-patterns" component={ConversationPatterns} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
