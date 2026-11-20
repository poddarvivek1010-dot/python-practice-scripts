
# text statistics and top word frequency analyzer......
from collections import Counter
import re


def analyze_text(sample_text):
  words = re.findall(r"\b[a-zA-Z0-9']+\b", sample_text.lower())
  sentences = [s.strip() for s in re.split(r"[.!?]+", sample_text) if s.strip()]
  word_counts = Counter(words)

  print("\n.... text analysis report .....")
  print(f"total characters : {len(sample_text)}")
  print(f"total words      : {len(words)}")
  print(f"total sentences  : {len(sentences)}")
  print("\ntop 5 most frequent words:")
  for word, count in word_counts.most_common(5):
    print(f"  {word:<12} : {count} time(s)")

 # Sample ....
paragraph = (
    "python makes text processing simple and fast. "
    "with Python, developers can analyze data, automate tasks, "
    "and build clean command line tools in minutes."
)

analyze_text(paragraph)
