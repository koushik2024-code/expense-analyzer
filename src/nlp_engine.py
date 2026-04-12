import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

class NLPEngine:

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer    = PorterStemmer()

    def preprocess(self, text):
        text = str(text).lower()
        text = re.sub(r'[^a-z\s]', '', text)
        tokens = text.split()
        tokens = [t for t in tokens if t not in self.stop_words]
        tokens = [self.stemmer.stem(t) for t in tokens]
        return ' '.join(tokens)

    def preprocess_series(self, series):
        return series.apply(self.preprocess)
