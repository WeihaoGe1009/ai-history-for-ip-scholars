# Module 5 Large Language Models — How Models Use Context, and What Their Training Data Contributes 

In previous modules, we explored models that made decisions based on simple word frequencies, short memory (Markov models), or compressed image representations. In this module, we begin to see how modern language models like BERT extend these ideas — using deeper layers, attention mechanisms, and richer input representations to build a powerful understanding of context. These models don’t reason like humans, but they predict text in ways that resemble understanding. This opens new technical possibilities — and new legal questions about authorship, influence, and control.


## What's Inside
* `05_llms.ipynb` - The interactive Google Colab notebook ([Run on Google Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/05_llms/05_llms.ipynb))
* `optional_reading_training_data_influence.md` - The optional reading document discussing tracing how the data used to train the models would influence the models.
* `data/` - contains the subset from the SST2 data set for sentiment analysis 
* `scripts/` - contains the script that curates the data 

## What You'll Learn
* How modern language model work differently from the models in our previous demos, such as Bag of Words.
* How modern language model utilize the context.
* An oversimplified case to see how training data influences the output model.

## Take-Home Messages
* Modern language model utilize more than word frequencies.  
* Modern language model "pays different **attentions**" to the context.
* It is possible to trace the influence of each data sample on the trained model. 

## Data
* Section 1:
    * frequency vs context: manually written sentences
    * sentiment analysis: a tiny subset from the **Stanford Sentiment Treebank (SST-2)**
* Section 2: manually written sentences
* Section 3: manually written numerical data  

## Dataset Attribution and License

The data in `sst2_long_subset.csv` is a 1000-example sample from the **Stanford Sentiment Treebank (SST-2)**., and we only select phrases with larger than 8 words.

- Source: Socher et al. (2013), “Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank”
- License: For research and educational use
- Subset extracted via the Hugging Face Datasets interface (`glue/sst2`)
- No redistribution of full dataset
- This subset is used under the assumption of fair academic use for instructional purposes only

- Full dataset documentation:
https://huggingface.co/datasets/glue/viewer/sst2 

## References
* **SBERT**
* **BERT** 
* **SST-2**
* **Transformer** Vaswani, Ashish, et al. "Attention is all you need." Advances in neural information processing systems 30 (2017).
* For full citations related to influence tracing, please see the optional reading material []()  
