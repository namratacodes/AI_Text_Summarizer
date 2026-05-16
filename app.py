import os
from io import BytesIO

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

# Get Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found. Please add it to your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def extract_text_from_pdf(uploaded_file):
    """Extract text from uploaded PDF."""
    reader = PdfReader(BytesIO(uploaded_file.read()))
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip()


# Summary style prompts
summary_styles = {
    "Short": "Summarize the following text in 3-5 bullet points.",
    "Medium": "Summarize the following text in about 150 words.",
    "Detailed": (
        "Provide a detailed summary of the following text in 300-400 words. "
        "Include all important insights and key points."
    ),
}


def summarize_text(text, style):
    """Generate summary using Gemini."""
    prompt = f"""
{summary_styles[style]}

Text:
{text}
"""

    response = model.generate_content(prompt)
    return response.text


# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="wide"
)

# App Title
st.title("📝 AI Text Summarizer")
st.write("Summarize text or PDF documents using Google Gemini.")

# Input Method Selection
input_method = st.radio(
    "Choose Input Method",
    ["Paste Text", "Upload PDF"]
)

text = ""

# Paste Text Option
if input_method == "Paste Text":
    text = st.text_area(
        "Enter text to summarize",
        height=250
    )

# Upload PDF Option
else:
    uploaded_file = st.file_uploader(
        "Upload a PDF file",
        type=["pdf"]
    )

    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)

        if text:
            st.success("PDF text extracted successfully.")

            with st.expander("Preview Extracted Text"):
                st.write(text[:5000])
        else:
            st.warning("No readable text found in the PDF.")

# Summary Length Selection
style = st.selectbox(
    "Summary Length",
    ["Short", "Medium", "Detailed"]
)

# Generate Summary Button
if st.button("Generate Summary"):
    if not text.strip():
        st.warning("Please provide some text or upload a PDF.")

    elif len(text) < 50:
        st.warning("Text is too short to summarize.")

    else:
        # Limit text size to avoid very large requests
        max_chars = 20000

        if len(text) > max_chars:
            text = text[:max_chars]
            st.info(
                f"Input was truncated to the first {max_chars} characters."
            )

        with st.spinner("Generating summary..."):
            try:
                summary = summarize_text(text, style)

                st.subheader("Summary")
                st.write(summary)

                # Download button
                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")