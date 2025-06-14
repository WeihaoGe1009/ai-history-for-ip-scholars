# A Guided Demo Series of AI for Intellectual Property (IP) Scholars

## Goals 
To help IP scholars and students:
* Understand the history of AI/ML models
* Learn the basic principle of model learning and generation.
* Facilitate drawing the subtle line between "learning" and "memorization"
* Explore how creativity, authorship, plaigiarism, and other right infringement might happen

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
* provide a colab link explicitly with [Open in Colab]
* add a description of each module

### Module 1 - Classification: Perceptron, Logistic Regression, and Naive Bayes 
* Explore how early models like the Perceptron, Logistic Regression, and Naive Bayes were used to classify text. This module uses Bag-of-Words to distinguish Shakespearean poetry from U.S. legal language.
* Open and run this notebook [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/01_perceptron_logreg_naive_bayes/01_perceptron_logreg_naivebayes.ipynb) 

(this link will not work at this stage, but tested working with dummy repo)

### Module 2 - Neural Network: Learning Patterns to Scribble
* Analyze how simple neural network like Multilayer Perceptron (MLP) processes image of handwritten digits. Open and run this notebook [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/02_neural_networks/02_01_simple_neural_network.ipynb) 
* Utilize a simple convolutional neural network (CNN) to process image of handwritten digits, and generate handwriting-like scribbles. Open and run this notebook [Open in Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/02_neural_networks/02_02_convolutional_neural_network.ipynb) 
 


Each module includes:
- 📖 Brief history and model explanation
- 🧪 Interactive Colab demo
- 🖼️ Visualizations and examples


In this table, i should add references. 
| Module | Title                                                  | Focus                                       | Era         | Historical Role                                                                 |
| ------ | ------------------------------------------------------ | ------------------------------------------- | ----------- | ------------------------------------------------------------------------------- |
| `01`   |  *Classification: Perceptron, Logistic Regression, and Naive-Bayes*                | linear, probabilistic, and rule-based classification using word frequencies                  | 1950s–1970s | First generation of ML models: Demonstrates how early AI systems used simple statistical rules and word patterns - without understanding meaning - to classify language. |
| `02`   |  *Neural Networks*                             | Pattern learning in hidden layers, Multilayer Perceptrons and Convolutional Neural Network          | 1980s–2000s | Overcame linear limits; enabled deeper pattern learning with hidden layers      |
| `03`   | 📊 *Probabilistic Models (Naive Bayes, Markov, Music)* | Frequency-based classification & prediction | 1960s–2000s | Sequence modeling using statistics, including early text and music generation   |
| `04`   | 🔁 *Autoencoders*                                      | Compression and reconstruction              | 2000s–2010s | Early unsupervised representation learning; led to pretraining ideas            |
| `05`   | ✍️ *Large Language Models (LLMs)*                      | Deep context prediction via attention       | 2017–Now    | Scaled transformer-based generation; foundational for modern generative AI      |
| `06`   | 🎨 *Diffusion Models*                                  | Generating images from noise                | 2021–Now    | Probabilistic generative models; stylized creation rather than reproduction     |
| `07`   | 🤔 *Chain-of-Thought and Reflection*                   | Reasoning, verification, and self-checking  | 2023+       | Structural techniques for alignment, safety, and transparent decision-making    |


## References
Each module includes links and references relevant to the models it covers.  
A full set of historical and academic references will be added in a future update.

## AI Usage and Content Disclaimer
Portions of this repository, including code and explanatory text, were developed with the assistance of artificial intelligence tools (e.g., large language models). All generated content was reviewed and curated to ensure accuracy and educational clarity.

All data used in these demonstrations were either:

* **Created synthetically by the author(s)** for illustrative purposes, or

* **Obtained from the public domain** and explicitly free of copyright restrictions.

No copyrighted or proprietary data, code, or materials were used in the construction of this resource.

This project is licensed under the MIT License. You are free to reuse, modify, and distribute the materials in this repository, provided that you include proper attribution to the original authors.

For details, see the [LICENSE](./LICENSE) file. 
