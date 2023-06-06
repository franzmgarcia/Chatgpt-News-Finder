import spacy
from transformers import pipeline

class NewsAnalyzer:
    def __init__(self):
        # Carga el modelo de lenguaje de spaCy
        #self.nlp = spacy.load('en_core_web_sm')
        self.nlp = spacy.load('es_core_news_sm')
        self.summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

    def analyze_text_spacy(self, text):
        # Usa spaCy para analizar el texto
        doc = self.nlp(text)

        # Imprime las entidades nombradas en el texto
        for entity in doc.ents:
            print(f"{entity.text} ({entity.label_})")

    def summarize_text(self, text):
        # Usa el modelo para generar un resumen del texto
        summary = self.summarizer(text, max_length=1000, min_length=1, do_sample=False)

        return summary[0]['summary_text']
