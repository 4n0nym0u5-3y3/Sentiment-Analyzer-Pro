import tkinter as tk
from tkinter import messagebox, filedialog
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

class SentimentAnalyzerPro:

    def __init__(self, master):
        self.master = master
        master.title("Sentiment Analyzer Pro")
        master.geometry("600x500")
        master.resizable(False, False)

        # Initialize variables
        self.history = []

        # Setting up the main UI elements
        self.label = tk.Label(master, text="Enter your text:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(master, width=60, font=("Arial", 12))
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<Return>", self.analyze_sentiment)

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_sentiment, font=("Arial", 12))
        self.analyze_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.details_label = tk.Label(master, text="", font=("Arial", 10))
        self.details_label.pack(pady=10)

        self.wordcloud_button = tk.Button(master, text="Show Word Cloud", command=self.show_wordcloud, font=("Arial", 12))
        self.wordcloud_button.pack(pady=5)

        self.history_button = tk.Button(master, text="Show History", command=self.show_history, font=("Arial", 12))
        self.history_button.pack(pady=5)

        self.clear_button = tk.Button(master, text="Clear History", command=self.clear_history, font=("Arial", 12))
        self.clear_button.pack(pady=5)

        self.export_button = tk.Button(master, text="Export Results", command=self.export_results, font=("Arial", 12))
        self.export_button.pack(pady=5)

        master.protocol("WM_DELETE_WINDOW", self.on_close)

    def analyze_sentiment(self, event=None):
        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text.")
            return

        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)
        self.display_results(sentiment_scores)

        # Store the analysis in history
        self.history.append({
            'text': text,
            'positive': sentiment_scores['pos'],
            'neutral': sentiment_scores['neu'],
            'negative': sentiment_scores['neg'],
            'compound': sentiment_scores['compound']
        })

    def display_results(self, scores):
        compound_score = scores['compound']

        if compound_score >= 0.05:
            sentiment = "Positive"
            color = "green"
        elif compound_score <= -0.05:
            sentiment = "Negative"
            color = "red"
        else:
            sentiment = "Neutral"
            color = "blue"

        self.result_label.config(text=f"Overall Sentiment: {sentiment}", fg=color)
        self.details_label.config(
            text=f"Positive: {scores['pos']*100:.2f}% | "
                 f"Neutral: {scores['neu']*100:.2f}% | "
                 f"Negative: {scores['neg']*100:.2f}%"
        )

    def show_wordcloud(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text.")
            return

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No history available.")
            return

        history_window = tk.Toplevel(self.master)
        history_window.title("Analysis History")
        history_window.geometry("600x300")

        history_text = tk.Text(history_window, wrap="word", font=("Arial", 12))
        history_text.pack(expand=True, fill='both')

        for entry in self.history:
            history_text.insert(tk.END, f"Text: {entry['text']}\n")
            history_text.insert(tk.END, f"Positive: {entry['positive']*100:.2f}%, "
                                        f"Neutral: {entry['neutral']*100:.2f}%, "
                                        f"Negative: {entry['negative']*100:.2f}%\n")
            history_text.insert(tk.END, f"Overall Sentiment: {'Positive' if entry['compound'] >= 0.05 else 'Negative' if entry['compound'] <= -0.05 else 'Neutral'}\n")
            history_text.insert(tk.END, "-"*60 + "\n")

    def clear_history(self):
        self.history.clear()
        messagebox.showinfo("History", "History cleared.")

    def export_results(self):
        if not self.history:
            messagebox.showinfo("Export", "No data to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        df = pd.DataFrame(self.history)
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Export", f"Results exported to {file_path}")

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalyzerPro(root)
    root.mainloop()
