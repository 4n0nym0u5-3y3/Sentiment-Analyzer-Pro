# Sentiment Analyzer Pro

## Overview
**Sentiment Analyzer Pro** is a Python-based graphical user interface (GUI) application designed to analyze the sentiment of user-provided text. Using the NLTK library's VADER sentiment analysis tool, the application categorizes text into positive, neutral, or negative sentiment. The application also features advanced functionalities, such as a text analysis history, word cloud visualization, and the ability to export results to a CSV file.

## Features

- **Real-time Sentiment Analysis**: Analyze text sentiment in real-time, displaying results as positive, neutral, or negative.
- **Sentiment Scores**: Detailed breakdown of positive, neutral, and negative sentiment scores.
- **Text History**: Automatically saves and displays a history of analyzed texts.
- **Word Cloud Visualization**: Generates a word cloud to visualize the most frequently used words in the analyzed text.
- **Export Results**: Export sentiment analysis history to a CSV file for further analysis or record-keeping.
- **Clear History**: Easily clear the analysis history with a single click.

## Requirements

- Python 3.x
- Required Python Libraries:
  - `tkinter` (Usually included with Python)
  - `nltk`
  - `matplotlib`
  - `wordcloud`
  - `pandas`


1. **Clone the repository** (or download the files):
   ```bash
   git clone link
   cd sentiment-analyzer-pro
   ```

2. **Install the required Python packages**:
   ```bash
   pip install nltk matplotlib wordcloud pandas
   ```

3. **Download the NLTK VADER lexicon**:
   Run the following Python commands to download the necessary NLTK data:
   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

4. **Run the application**:
   ```bash
   python sentiment_analyzer_pro.py
   ```

## Usage

1. **Start the Application**: Run the `sentiment_analyzer_pro.py` script to launch the application.
2. **Enter Text**: Type the text you want to analyze in the input field.
3. **Analyze**: Press Enter or click the "Analyze" button to see the sentiment analysis results.
4. **Show Word Cloud**: Click "Show Word Cloud" to generate a word cloud based on the entered text.
5. **View History**: Click "Show History" to see all the text that has been analyzed so far.
6. **Clear History**: Click "Clear History" to delete all past analysis records.
7. **Export Results**: Click "Export Results" to save the analysis history as a CSV file.


