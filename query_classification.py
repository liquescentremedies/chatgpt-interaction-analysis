import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def preprocess_data(queries):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(queries)
    return X, vectorizer

def classify_queries(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    return model

def provide_insights(model, vectorizer, queries):
    X = vectorizer.transform(queries)
    predictions = model.predict(X)
    insights = pd.DataFrame({'Query': queries, 'Category': predictions})
    return insights

if __name__ == "__main__":
    # Assuming the data has been extracted and organized into a DataFrame
    df = pd.read_csv('extracted_data.csv')
    queries = df['Query'].tolist()
    categories = df['Category'].tolist()  # Assuming categories are already labeled in the data

    X, vectorizer = preprocess_data(queries)
    model = classify_queries(X, categories)
    insights = provide_insights(model, vectorizer, queries)
    print(insights.head())
