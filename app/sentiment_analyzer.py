from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.classifier = pipeline("sentiment-analysis", model=model_name)
    
    def analyze_text(self, text):
        return self.classifier(text)[0]
    
    def analyze_batch(self, texts):
        return self.classifier(texts)
