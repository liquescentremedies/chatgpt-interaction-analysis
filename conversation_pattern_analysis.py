import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

def identify_recurring_themes(queries):
    stopwords = set(nltk.corpus.stopwords.words('english'))
    all_words = []

    for query in queries:
        words = nltk.word_tokenize(query)
        words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords]
        all_words.extend(words)

    word_freq = Counter(all_words)
    return word_freq

def generate_word_cloud(word_freq):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Assuming the data has been extracted and organized into a DataFrame
    df = pd.read_csv('extracted_data.csv')
    queries = df['Query'].tolist()

    word_freq = identify_recurring_themes(queries)
    generate_word_cloud(word_freq)
