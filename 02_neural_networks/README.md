# Neural Network: Perception, Pattern, and Prototype

Neural networks have played a central role in the history of machine learning — first inspiring hope in the 1950s, then fading from favor, and later returning to power modern AI.
This module offers a visual introduction to how these networks learn from examples.

In the first part, a simple model learns to recognize handwritten digits and reveals a blurry "average" shape based on learning. In the second, a more advanced network identifies patterns like strokes and generate new, scribble-like images from random input. Together, these demos show how machines begin to "see" — not by understanding, but by building patterns from data.


---

## What’s Inside

- `02_01_simple_neural_network.ipynb` – The interactive Google Colab notebook ([Run on Google Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/02_neural_networks/02_01_simple_neural_network.ipynb))
- `02_02_convolutional_neural_network.ipynb` - The interactive Google Colab notebook ([Run on Google Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/02_neural_networks/02_02_convolutional_neural_network.ipynb))  
- `models/` - Pre-trained models to load into the notebooks 

---

## What You'll Learn

- How neural networks "recognizes" hand-written digits and associate them with numbers
- What features are learnt by neural network models
- How to generate patterns based on features learnt by the neural networks.

## Take-Home Messages

- Neural networks learns "patterns": curves, blobs, lines, corners, etc.
- The patterns learnt by different neural nodes in the network are "activated" by different inputs, which leads to "recognition" of the inputs.
- With the patterns learnt, neural networks can generate new images, which is the early basis of more sophisticated AIs. 

## Data
This demo uses the MNIST data set, a public collection of handwritten digit images (0-9), originally created by the Modified National Institute of Standards and Technology (MNIST), widely used to teach and evaluate machin-learning models.


## Data Source:

The MNIST dataset is freely available through TensorFlow, an open-source library developed by Google. MNIST is in the public domain. 


## References
- **Neural Network**: Schmidhuber, Jürgen. "Deep learning in neural networks: An overview." Neural networks 61 (2015): 85-117. 
- **MNIST data set**: LeCun, Yann, et al. "Gradient-based learning applied to document recognition." Proceedings of the IEEE 86.11 (2002): 2278-2324. 
 
