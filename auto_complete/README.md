# N-Gram Text GeneratorA statistical

 language model implemented in Python that generates text using N-gram probability distributions. This project demonstrates the fundamental concepts of Natural Language Processing (NLP), including tokenization, vocabulary management, and perplexity evaluation.
 
## 📌 Project Overview

 This notebook builds an  ***N-gram*** language model (specifically a trigram model) trained on a corpus of text (Tweets). It learns the probability of a word occurring based on the previous $N-1$ words and uses these probabilities to generate new, random sentences that mimic the style of the training data.
 
 ⚙️ ***Key Features***
 - ***Text Preprocessing:*** efficient cleaning pipeline including lowercasing, punctuation removal, and tokenization using nltk.
 - ***OOV Handling:*** Handles Out-Of-Vocabulary words by filtering low-frequency tokens and replacing them with an <unk> token to improve model robustness.
 - ***N-Gram Modeling:*** customized function to generate N-grams and build a frequency-based dictionary model.
 - ***Stochastic Generation:*** Generates novel sentences using weighted random sampling based on context history.
 - ***Evaluation:*** Implements Perplexity calculation with smoothing to quantitatively measure model performance.
 
 ## 🚀 WorkflowThe
project follows these specific steps:
1. Data Loading: Imports raw text data (twits.txt).
2. Preprocessing: Tokenizes sentences and cleans special characters.Vocabulary Building: Identifies words with frequency $< N$ and marks them as <unk>.
3. Model Construction: Creates a dictionary mapping $(n-1)$ contexts to next-word probabilities.
4. Generation: Produces new text sequences.
5. Visualization: Plots the perplexity distribution of generated sentences using matplotlib.

## 🛠️ Dependencies
- Python3
- xNLTK (Natural Language Toolkit)
- Pandas
- Matplotlib
- NumPy (via Pandas/Math)

## 📊 Example Usage
```Python
# Build the model
n = 3
ngram_model = build_ngram_model(train_data, n)

# Generate a sentence
print(generate_sentence_no_unk(ngram_model, n, start_word='town'))

# Output: "town needs a who before you even walked through the bottom of the best thing"
```





## 📈 Results
The model successfully generates coherent short sentences. The quality of the model is verified via a Perplexity distribution plot, showing low perplexity (high confidence) for the generated text.