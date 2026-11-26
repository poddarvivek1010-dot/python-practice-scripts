from collections import Counter
import re


def analyze_text(text):
  words = re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())
  sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
  word_count = len(words)
  sentence_count = len(sentences)
  avg_word_len = sum(len(w) for w in words) / word_count if word_count else 0
  top_words = Counter(words).most_common(5)

  print(f"\nwords: {word_count}")
  print(f"sentences: {sentence_count}")
  print(f"unique words: {len(set(words))}")
  print(f"average word length: {avg_word_len:.2f} chars")
  print("top 5 words:", ", ".join(f"{w} ({c})" for w, c in top_words))


def main():
  print("paste or type text (press [enter] twice to analyze):")
  lines = []
  while True:
    line = input()
    if line == "":
      break
    lines.append(line)
  analyze_text("\n".join(lines))


if __name__ == "__main__":
  main()
