import streamlit as st
from summarizer import summarize_text
from utils import extract_text_from_pdf, extract_text_from_url

st.title("🧠 AI Text Summarizer")
st.write("Summarize articles, PDFs, or plain text using BART NLP model.")

option = st.radio("Choose input type:", ["Plain Text", "Upload PDF", "From URL"])

input_text = ""

if option == "Plain Text":
    input_text = st.text_area("Enter your text here:", height=300)

elif option == "Upload PDF":
    uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_pdf:
        input_text = extract_text_from_pdf(uploaded_pdf)
        st.success("PDF text extracted!")

elif option == "From URL":
    url = st.text_input("Enter article URL:")
    if st.button("Extract Text"):
        input_text = extract_text_from_url(url)
        st.success("Article text extracted!")

if input_text:
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(input_text)
            st.subheader("Summary:")
            st.write(summary)
            st.download_button("Download Summary", summary, file_name="summary.txt")
