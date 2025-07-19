import pytest
from app.sentiment_analyzer import SentimentAnalyzer

@pytest.fixture
def analyzer():
    return SentimentAnalyzer()

def test_analyze_text_positive(analyzer):
    result = analyzer.analyze_text("I love this product!")
    assert result["label"] == "POSITIVE"
    assert 0 <= result["score"] <= 1

def test_analyze_text_negative(analyzer):
    result = analyzer.analyze_text("This is terrible.")
    assert result["label"] == "NEGATIVE"
    assert 0 <= result["score"] <= 1
