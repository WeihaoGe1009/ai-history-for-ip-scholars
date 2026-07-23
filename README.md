# A Guided Demo Series of AI for Law Scholars

## Goals 
To help Law scholars and students:
* Understand the history of AI/ML models
* Learn the basic principle of model learning and generation.
* Explore how AI-related issues might raise 

## How to use this resource
### 1. requirements
* A Google account (Gmail or G Suite is fine)
* A modern web browser (Chrome, Firefox, Safari)
* No installation is required (Colab runs in the browser) 
* Internet connection (needed to run notebooks via Colab) 

### 2. First-Time Google Colab Setup
* **Step 1**: Go to [Google Colab homepage](https://colab.research.google.com/)
* **Step 2**: Sign in with your Google account
* **Step 3** when prompt to allow access or connect to Google Drive, either "Allow" or "Cancel" should work, since you don't need to save or upload anything.

### 3. Open and Run a Demo Notebook
* **Step 1**: Scroll down to the [**Modules**](#modules) section below.
* **Step 2**: Click the "Open in Colab" link for the module
* **Step 3**: The notebook will open in a new browser tab
* **Step 4**: Click the **Play button** next to each code and run it
* Tip: After opening this notebook in Colab, go to `Runtime → Run all` to execute everything automatically.
* Note: You may see a prompt like "This notebook was not authored by Google” — click “**Run Anyway**”
* All data is included in this public GitHub Repo
* After closing the tab of google colab, no changes are saved unless you make a copy.


## Modules

### Module 1 - Classification: Perceptron, Logistic Regression, and Naive Bayes 
* Explore how early models like the Perceptron, Logistic Regression, and Naive Bayes were used to classify text. This module uses Bag-of-Words to distinguish Shakespearean poetry from U.S. legal language.
* Open and run this notebook [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/01_perceptron_logreg_naive_bayes/01_perceptron_logreg_naivebayes.ipynb) 

### Module 2 - Neural Network: Neural Network: Perception, Pattern, and Prototype 
* Analyze how simple neural network like Multilayer Perceptron (MLP) processes image of handwritten digits. Open and run this notebook [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/02_neural_networks/02_01_simple_neural_network.ipynb) 
* Utilize a simple convolutional neural network (CNN) to process image of handwritten digits, and generate handwriting-like scribbles. Open and run this notebook [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/02_neural_networks/02_02_convolutional_neural_network.ipynb) 

### Module 3 - Markov Chain: Language, Probability & Illusion 
* View how models like Markov Chain generate contents and how it is different from search. Open and run this notebook [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/03_markov/03_markov.ipynb)

### Module 4 - Autoencoders & Compression - A Responsible Perspective
* Explore how autoencoders learn patterns from images, and its applications in data compression and image denoising. [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/04_autoencoders/04_autoencoder.ipynb) 

### Module 5 - Language Models — How Models Use Context, and What Their Training Data Contributes
* Briefly analyze how modern language models utilize "context" in a text. Additionally, we evaluate the influence of each sample in the training data set on a model in a very simple case. [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/05_language_models/05_language_models.ipynb)
* optional reading on more in-depth discussion on tracing influence of the training data in the large language models. [View on Github](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/05_language_models/optional_reading_training_data_influence.md)

### Module 6 - Generative Models - the foundation behind modern "AI" products.
* briefly demonstrate how generative model "generates" outputs from random noise, how to "prompt" a model, how would a model collapse, and how the output "follows" a style. [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/06_generative_models/06_generative_models.ipynb)
* optional reading introducing other content-creating models that are not genAI. [View on GitHub](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/06_generative_models/optional_reading_before_generative_AI.md)
* optional reading providing open discussion topics. [View on Github](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/06_generative_models/optional_reading_tech_law_society.md) 

### optional: Module 7 - After ChatGPT - treading in the waves of AIs
* a walkthrough of how to understand new concepts and the new model releases. [View on GitHub](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/07_after_chatgpt/07_after_chatgpt.md)
* extra reading briefly talking about a few technical concepts after ChatGPT. [View on GitHub](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/07_after_chatgpt/optional_reading_hallucination_agent_prompt_durability.md) 

| Module | Title                                                  | Focus                                       | Era         | Historical Role                                                                 |
| ------ | ------------------------------------------------------ | ------------------------------------------- | ----------- | ------------------------------------------------------------------------------- |
| `01`   |  *Classification: Perceptron, Logistic Regression, and Naive-Bayes*                | linear, probabilistic, and rule-based classification using word frequencies                  | 1950s–1970s | First generation of ML models: Demonstrates how early AI systems used simple statistical rules and word patterns - without understanding meaning - to classify language. |
| `02`   |  *Neural Network: Perception, Pattern, and Prototype*                             | pattern learning and image generation           | 1980s–2000s | Overcame linear limits; enabled deeper pattern learning with hidden layers      |
| `03`   |  *Markov Chain: Language, Probability, and Illusion* | Frequency-based content generation | 1960s–2000s | Sequence modeling using statistics, including early text and music generation   |
| `04`   |  *Autoencoders*                                      | Compression and reconstruction              | 2000s–2010s | Early unsupervised representation learning; led to pretraining ideas            |
|`05`   |  *Language Models*                      | Deep context prediction via attention       | 2017–Now    | Scaled transformer-based generation; foundational for modern generative AI      |
| `06`   | *Generative Models*                                  | Generating images from noise                | 2021–Now    | Probabilistic generative models; stylize mimicry     |
| `07`   | *After ChatGPT*                   | Following up the new, AI hallucination, and old issues in new era  | 2023+       | How to catch up with an explosion of AI products without getting exhausted    |


## References
Each module includes links and references relevant to the models it covers.  

## Questions & Requests

Have a question about a concept, or want another topic explained? Two ways to reach me:

- **Email** (no GitHub account needed): [how.ai.works.law.policy@gmail.com]
- **GitHub Q&A**: post in [Discussions → Q&A](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/discussions/categories/q-a)

Emailed questions of general interest may be posted (anonymized) to the Q&A, so answers stay searchable for everyone.

Found a bug in a notebook (broken cell, typo)? Please open an [Issue](https://github.com/WeihaoGe1009/ai-history-for-ip-scholars/issues) instead.

## AI Usage and Content Disclaimer
Portions of this repository, including code and explanatory text, were developed with the assistance of artificial intelligence tools (e.g., large language models). All generated content was reviewed and curated to ensure accuracy and educational clarity. Human efforts include: design and outline each demo, decide which models and tests to use, hyperparameter tuning, content of the text.

All data used in these demonstrations were either:

* **Created synthetically by the author(s)** for illustrative purposes, or

* **Publicly available for research and educational use**


No unauthorized copyrighted or proprietary data, code, or materials were used. All datasets and tools are either synthetic, open source, or publicly released for research and educational purposes.

This project is licensed under the MIT License. You are free to reuse, modify, and distribute the materials in this repository, provided that you include proper attribution to the original authors, Weihao Ge & Xiaoren Wang.

For details, see the [LICENSE](./LICENSE) file. 
