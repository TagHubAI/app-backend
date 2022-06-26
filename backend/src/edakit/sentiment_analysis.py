import os
import logging

import numpy as np

from transformers import AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax
from typing import List


class SentimentAnalyzer:
    """
    Class for sentiment prediction with 3 labels: negative, neutral and positive
    """
    def __init__(self, model_path: str="cardiffnlp/twitter-roberta-base-sentiment", cache_dir=None) -> None:
        self._labels = ["negative", "neutral", "positive"]

        if cache_dir and not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        self._tokenizer = AutoTokenizer.from_pretrained(model_path, cache_dir=cache_dir)
        logging.info("Successfully load sentiment tokenizer")
        self._model = AutoModelForSequenceClassification.from_pretrained(model_path, cache_dir=cache_dir)
        logging.info("Successfully load sentiment model")
        self._model_path = model_path
    
    @property
    def labels(self):
        return self._labels

    @property
    def tokenizer(self):
        return self._tokenizer

    @property
    def model(self):
        return self._model

    def get_list_sentiment(self, texts: List[str]) -> List[str]:
        """
        Predict sentiment for a list of input text
        """
        return [self.get_sentiment(text) for text in texts]

    def get_sentiment(self, text: str) -> str:
        """
        Predict sentiment for an input text
        """
        encoded_input = self._tokenizer(text, return_tensors="pt")
        output = self._model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        top_score_idx = np.argmax(scores)
        return self._labels[top_score_idx]


if __name__ == "__main__":
    sentiment_analyzer = SentimentAnalyzer()
    texts = ["This movie sucks", "This one is great", "The world is about to end"] # Example texts
    results = sentiment_analyzer.get_list_sentiment(texts=texts)
    for result, text in zip(results, texts):
        print(f"Text: {text} - Predicted label: {result}")