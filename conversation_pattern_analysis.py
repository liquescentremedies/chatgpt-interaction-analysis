import pandas as pd
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import json

def download_nltk_data():
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
    except Exception as e:
        print(f"Warning: Failed to download NLTK data: {str(e)}")
        print("Some functionality may be limited.")

def identify_recurring_themes(queries):
    stopwords = set(nltk.corpus.stopwords.words('english'))
    all_words = []

    for query in queries:
        try:
            words = nltk.word_tokenize(str(query))
            words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords]
            all_words.extend(words)
        except Exception as e:
            print(f"Warning: Failed to process query: {str(e)}")
            continue

    word_freq = Counter(all_words)
    return word_freq

def generate_word_cloud(word_freq, filename):
    plt.figure(figsize=(10, 5))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

if __name__ == "__main__":
    try:
        # Download required NLTK data
        download_nltk_data()

        # Load the extracted data
        df = pd.read_csv('extracted_data.csv')
        queries = df['Query'].tolist()

        # Analyze word frequencies
        word_freq = identify_recurring_themes(queries)

        # Save word frequencies
        word_freq_df = pd.DataFrame([
            {'word': word, 'frequency': freq}
            for word, freq in word_freq.most_common()
        ])
        word_freq_df.to_csv('conversation_patterns.csv', index=False)
        print("Conversation pattern analysis results saved to conversation_patterns.csv")

        # Generate and save word cloud
        generate_word_cloud(word_freq, 'word_cloud.png')
        print("Word cloud visualization saved as word_cloud.png")

        # Display top themes
        print("\nTop 20 Recurring Themes:")
        for word, freq in word_freq.most_common(20):
            print(f"{word}: {freq}")

    except FileNotFoundError:
        print("Error: extracted_data.csv not found. Please run data_extraction.py first.")
    except Exception as e:
        print(f"Error performing conversation pattern analysis: {str(e)}")
