# AI Text Summarizer

An AI-powered web application that summarizes text and PDF documents using Google Gemini and Streamlit.

## Features

- Paste text and generate summaries
- Upload PDF documents and extract text automatically
- Choose summary length:
  - Short (3–5 bullet points)
  - Medium (~150 words)
  - Detailed (300–400 words)
- Download the generated summary as a `.txt` file
- Uses Google Gemini API 

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv

## Project Structure

```text
AI_Text_Summarizer/
│── app.py
│── requirements.txt
│── .env
│── README.md

## Installation

1. Clone the repository
git clone https://github.com/your-username/AI_Text_Summarizer.git
cd AI_Text_Summarizer
2. Install dependencies
pip install -r requirements.txt

##Setup

1. Get a free Gemini API key

Create a free API key from Google AI Studio:

https://aistudio.google.com

2. Create a .env file
GEMINI_API_KEY=your_api_key_here
Run the Application
streamlit run app.py

The app will open in your browser at:

http://localhost:8501

##Usage

Choose Paste Text or Upload PDF
Enter text or upload a PDF
Select summary length
Click Generate Summary
Download the summary if needed
Example Resume Description

##Future Enhancements

Keyword extraction
Sentiment analysis
Translation support
Chat with PDF functionality

##License

This project is for educational and portfolio purposes.
