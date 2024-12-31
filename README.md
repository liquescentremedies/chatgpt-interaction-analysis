# ChatGPT Interaction Analysis

A comprehensive toolkit for analyzing personal ChatGPT conversations to gain insights into engagement patterns, learning styles, and interaction behaviors.

## Purpose

This project helps you understand your interaction patterns with ChatGPT by analyzing exported conversation data. It provides insights into:
- Common themes and topics in your conversations
- Emotional tone of interactions
- Response times and engagement patterns
- Query types and categories
- Temporal patterns of usage

## Prerequisites

1. Python 3.6 or higher
2. Your ChatGPT conversation data exported as `model_comparisons.json` with the following structure:
   ```json
   {
     "conversations": [
       {
         "messages": [
           {
             "role": "user",
             "content": "your message",
             "timestamp": "2023-01-01T12:00:00Z"
           },
           {
             "role": "assistant",
             "content": "ChatGPT's response",
             "timestamp": "2023-01-01T12:00:05Z"
           }
         ]
       }
     ]
   }
   ```

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   This will install all required packages including:
   - pandas: Data manipulation
   - numpy: Numerical operations
   - nltk: Natural language processing
   - scikit-learn: Machine learning
   - matplotlib: Visualization
   - textblob: Sentiment analysis
   - wordcloud: Word cloud generation

2. **Place your data file**:
   - Put your `model_comparisons.json` file in the project root directory

## Running the Analysis

Run the scripts in the following order:

1. **Extract Data**:
   ```bash
   python data_extraction.py
   ```
   Creates `extracted_data.csv` with structured conversation data.

2. **Analyze Sentiment**:
   ```bash
   python sentiment_analysis.py
   ```
   Generates sentiment analysis results and visualizations.

3. **Analyze Temporal Patterns**:
   ```bash
   python temporal_analysis.py
   ```
   Creates temporal analysis results and visualizations.

4. **Model Topics**:
   ```bash
   python topic_modeling.py
   ```
   Identifies main conversation topics and their distribution.

5. **Classify Queries**:
   ```bash
   python query_classification.py
   ```
   Categorizes queries and generates insights.

6. **Analyze Response Times**:
   ```bash
   python response_time_analysis.py
   ```
   Evaluates response time patterns.

7. **Analyze Conversation Patterns**:
   ```bash
   python conversation_pattern_analysis.py
   ```
   Identifies recurring themes and generates word clouds.

8. **Generate Overview**:
   ```bash
   python overview_synthesis.py
   ```
   Combines all analyses into a comprehensive report.

## Output Files

The analysis generates several output files:

### Data Files
- `extracted_data.csv`: Raw structured conversation data
- `sentiment_analysis.csv`: Sentiment analysis results
- `temporal_analysis.csv`: Temporal pattern data
- `topic_modeling.csv`: Topic modeling results
- `query_classification.csv`: Query classification results
- `response_time_analysis.csv`: Response time data
- `conversation_patterns.csv`: Word frequency data
- `analysis_summary.json`: Comprehensive analysis results

### Visualizations
- `query_sentiment_distribution.png`: Sentiment analysis visualization
- `response_sentiment_distribution.png`: Response sentiment visualization
- `interaction_frequency.png`: Temporal pattern visualization
- `engagement_trends.png`: User engagement trends
- `topic_distribution.png`: Topic distribution chart
- `query_categories.png`: Query category distribution
- `response_time_distribution.png`: Response time patterns
- `word_cloud.png`: Word cloud of common themes
- `overview_*.png`: Overview visualizations

## Error Handling

Each script includes error handling for common issues:
- Missing input files
- Data format problems
- Processing errors

If you encounter errors, check:
1. The `model_comparisons.json` file exists and has the correct format
2. All required packages are installed
3. Scripts are run in the correct order

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
