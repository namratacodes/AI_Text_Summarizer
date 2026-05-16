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
- Uses Google Gemini API (free tier available)

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