import pandas as pd
from sklearn.utils import shuffle

def extract_poetic_sentences(filepath):
    sentences = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if stripped.isdigit():
                continue  # Skip sonnet number lines
            if not stripped:
                continue  # Skip blank lines
            sentences.append(stripped)
    return sentences

def extract_legal_sentences(filepath):
    sentences = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if len(stripped) > 12:  # Skip blank lines and "Article/Section number" 
                sentences.append(stripped)
    return sentences


poetic_sentences = extract_poetic_sentences("data/raw_poetic.txt")
legal_sentences = extract_legal_sentences("data/raw_legal.txt")

# Labels
poetic_labels = [0] * len(poetic_sentences)
legal_labels = [1] * len(legal_sentences)

# Merge and shuffle
sentences = poetic_sentences + legal_sentences
labels = poetic_labels + legal_labels
df = pd.DataFrame({'Sentence': sentences, 'Label': labels})
df = shuffle(df, random_state=42).reset_index(drop=True)

# Save
df.to_csv("data/labeled_sentences.csv", index=False)
print(f"Saved {len(df)} labeled sentences to data/labeled_sentences.csv")
