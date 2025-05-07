from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, min_len=50, max_len=200):
    summary = summarizer(text, min_length=min_len, max_length=max_len, do_sample=False)
    return summary[0]['summary_text']
