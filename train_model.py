import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.data_processor import DataProcessor
from src.nlp_engine     import NLPEngine
from src.ml_classifier  import ExpenseClassifier

print('Loading data...')
dp = DataProcessor()
df = dp.load('data/sample_data.csv')
print(f'Loaded {len(df)} transactions')

print('Preprocessing with NLP...')
nlp = NLPEngine()
X   = nlp.preprocess_series(df['description'])
y   = df['category']

print('Training ML classifier...')
clf = ExpenseClassifier()
clf.train(X, y)
clf.save('models/classifier.pkl')
print('Training complete!')
