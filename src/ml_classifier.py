import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

class ExpenseClassifier:

    def __init__(self):
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=5000)),
            ('clf',   LogisticRegression(max_iter=300, C=1.0, random_state=42)),
        ])

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        preds    = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, preds)
        print(f'Model Accuracy: {accuracy * 100:.2f}%')
        print(classification_report(y_test, preds))
        return self

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path='models/classifier.pkl'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)
        print(f'Model saved to {path}')

    def load(self, path='models/classifier.pkl'):
        self.model = joblib.load(path)
        print(f'Model loaded from {path}')
        return self
