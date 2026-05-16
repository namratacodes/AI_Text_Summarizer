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

## Installation

1. Clone the repository
2. Install dependencies
pip install -r requirements.txt

## Setup

1. Get a free Gemini API key

Create a free API key from Google AI Studio:

https://aistudio.google.com

2. Create a .env file
GEMINI_API_KEY=your_api_key_here
3. Run the Application
streamlit run app.py

The app will open in your browser at:

http://localhost:8501

## Usage

1. Choose Paste Text or Upload PDF
2. Enter text or upload a PDF
3. Select summary length
4. Click Generate Summary
5. Download the summary if needed

## Future Enhancements

1. Keyword extraction
2. Sentiment analysis
3. Translation support
4. Chat with PDF functionality

## License

This project is for educational and portfolio purposes.

## Project Structure

```text
AI_Text_Summarizer/
│── app.py
│── requirements.txt
│── .env
│── README.md


