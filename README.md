# TEXT-SUMMARIZATION-TOOL

COMPANY : CODTECH IT SOLUTIONS

NAME : BASAVAPRABHU R HALAKATTI

INTERN ID : CT04DL919

DOMAIN : ARTIFICIAL INTELLIGENCE

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

Description :
This project, titled "AI Text Summarization Tool", was developed as part of Task 1 for the CodTech IT Solutions, Artificial Intelligence Internship. The goal of the task was to design and implement a tool that leverages Natural Language Processing (NLP) techniques to summarize lengthy articles or text documents into concise, meaningful outputs. The solution had to be implemented in Python, showcasing practical usage of NLP models and tools.

To make the tool accessible and easy to use, the project was developed using Gradio, a Python library that enables quick creation of web-based user interfaces for machine learning models. Gradio allowed me to deploy a simple yet effective frontend directly from a Python script, making the tool look like a web application while still being lightweight and easy to run locally or on Colab.

🔍 Objective of the Tool
The primary purpose of this summarization tool is to reduce the length of textual content without losing its core meaning. In today’s information-rich environment, being able to quickly grasp the main idea of a document is critical. This tool addresses that need by using powerful transformer-based models trained for summarization tasks.

⚙️ How It Works
The backend logic of the tool is powered by the Hugging Face Transformers library. Specifically, the project uses the facebook/bart-large-cnn model—a state-of-the-art abstractive summarization model. Unlike extractive models that pick important sentences from the original text, abstractive models like BART rephrase the text and generate new, concise sentences that retain the original meaning.

When the user enters or pastes a block of text into the Gradio interface and clicks the “Summarize” button, the input text is passed to the backend Python function. The model processes the input and returns a short summary. The summarized output is then displayed on the same interface, giving the user immediate results.

🎨 Frontend with Gradio

The use of Gradio for the frontend allowed me to:

Create a clean, user-friendly UI with just a few lines of code
Deploy the app on Google Colab without worrying about HTML, CSS, or JavaScript
Generate a public shareable link to the live demo instantly
Focus more on the AI functionality while still offering a usable interface
Gradio supports various input types, but for this project, a simple text box was sufficient to demonstrate the summarization task.

🧠 Technologies Used

Python: Core programming language
Hugging Face Transformers: To load and run pre-trained summarization models
Gradio: To create and launch the interactive web UI
Google Colab: For development and execution of the tool in a notebook environment

✅ Features

Accepts raw text input for summarization
Uses an abstractive NLP model for human-like summaries
Lightweight web interface using Gradio
Can be deployed locally or shared via public Colab links
Fully written and executed in Python (no separate frontend or backend files)

📈 Use Cases

Summarizing blog posts, news articles, or research abstracts
Helping students quickly grasp the gist of study material
Assisting writers in condensing long drafts
Creating automatic summaries for content-heavy websites

📌 Conclusion

The AI Text Summarization Tool built using Gradio and Transformers provides a simple, effective solution for automatic text summarization. It demonstrates the integration of NLP models into usable tools with minimal overhead. This project fulfills the requirements of Task 1 in the CodTech internship and highlights skills in machine learning, NLP, and interactive AI app development.

This tool lays the foundation for future extensions like summarizing from PDFs, URLs, or text inputs, and supports the broader vision of building accessible, AI-powered productivity tools for real-world users.
