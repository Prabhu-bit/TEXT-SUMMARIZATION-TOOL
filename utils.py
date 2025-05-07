import pdfplumber
from newspaper import Article

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
