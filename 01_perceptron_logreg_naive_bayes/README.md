# Classification: Perceptron, Logistic Regression, and Naive Bayes 

This module introduces some of the earliest machine learning models used for text classification. It walks through how machines began to separate different types of language — in this case, **poetic** (Shakespearean sonnets) and **legal** (U.S. Constitution and Bill of Rights) — using only **word frequencies**.

---

## 🔍 What’s Inside

- `01_perceptron_logreg_naivebayes.ipynb` – The interactive Google Colab notebook ([Run on Google Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/01_perceptron_logreg_naive_bayes/01_perceptron_logreg_naivebayes.ipynb))  
- `data/` – Contains raw poetic/legal texts and labeled data used for training  
- `generate_labeled_data.py` – A preprocessing script to convert raw texts into labeled sentences

---

## What You'll Learn

- How to represent text using the **Bag-of-Words** model
- How early models made decisions using rules
- How **Logistic Regression** and **Naive Bayes** add a probabilistic layer

## Take-Home Messages

- Early models operate without understanding meaning — they rely purely on word patterns.
- Bag-of-Words is a powerful yet simple way to turn text into something machines can use.
- Perceptron is deterministic; Logistic Regression and Naive Bayes are probabilistic.

## Data
We use two text sources to create a binary classification task:

- **Poetic sentences**: Ten sonnets were arbitrarily selected from Shakespeare’s full collection, with a preference toward more recognizable or previously encountered works. The selection was not randomized or based on specific thematic or linguistic criteria.

- **Legal sentences**: The legal document includes the US Constitution and the Bill of Rights.

## Data Source:
Shakespeare's Sonnets [Folger Shakespear Library](https://www.folger.edu/explore/shakespeares-works/shakespeares-sonnets/) 
License: Public Domain

U.S. Constitution [U.S. National Archives - The Constitution of the United States: A Transcription](https://www.archives.gov/founding-docs/constitution-transcript) 
License: Public Domain

U.S. Bill of Rights [U.S. National Archives - The Bill of Rights: A Transcription](https://www.archives.gov/founding-docs/bill-of-rights-transcript) 
License: Public Domain

## References
**Bag of Words**: Qader, Wisam A., Musa M. Ameen, and Bilal I. Ahmed. "An overview of bag of words; importance, implementation, applications, and challenges." 2019 international engineering conference (IEC). IEEE, 2019.
**Perceptron**: Rosenblatt, Frank. "The perceptron: a probabilistic model for information storage and organization in the brain." Psychological review 65.6 (1958): 386.
**Logistic Regression**: Freund, Rudolf J., and William J. Wilson. Statistical methods. Elsevier, 2003.
**Naive Bayes**: Rennie, Jason D., et al. "Tackling the poor assumptions of naive bayes text classifiers." Proceedings of the 20th international conference on machine learning (ICML-03). 2003. 
