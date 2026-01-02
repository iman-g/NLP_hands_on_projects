# Semantic Analysis of News Articles 📰


## Project Overview
This project performs unsupervised Natural Language Processing (NLP) on a dataset of news articles to discover hidden semantic structures. By utilizing both **LDA (Latent Dirichlet Allocation)** for topic modeling and **K-Means** for document clustering, we identify distinct themes across various news outlets.

## 🛠 Technologies Used
* **NLP:** Spacy, NLTK
* **Vectorization:** TF-IDF, Gensim Dictionary
* **Modeling:** Scikit-Learn (K-Means), Gensim (LDA)
* **Optimization:** KneeLocator (Elbow Method), Coherence Scores

## 📊 Methodology

### 1. Data Preprocessing
The raw text data undergoes a rigorous cleaning pipeline:
* **Lemmatization:** Converting words to their base forms (e.g., "running" -> "run").
* **POS Filtering:** Retaining only Nouns, Verbs, Adjectives, and Proper Nouns using Spacy.
* **Stopword Removal:** Eliminating common noise words.

### 2. Topic Modeling (LDA)
We utilized Gensim's LDA Multicore model to extract topics. To determine the optimal number of topics, we calculated the **Coherence Score ($C_v$)** across varying parameter inputs.
* *Result:* The coherence analysis suggested high semantic similarity with ~17 topics.

### 3. Clustering (K-Means)
We vectorized the cleaned text using **TF-IDF** (Term Frequency-Inverse Document Frequency) to highlight unique keywords per document.
* **Elbow Method:** Used to find the optimal $K$ (clusters).
* **Result:** The KneeLocator identified **5 optimal clusters**.

## 📈 Key Findings (Cluster Analysis)

Based on the K-Means analysis, the news articles naturally grouped into these 5 distinct categories:

| Cluster | Top Keywords | Inferred Theme |
| :--- | :--- | :--- |
| **0** | firepit, fireplace, firestarter | *Lifestyle / Home (Outlier)* |
| **1** | company, facebook, google, tech | *Big Tech & Business* |
| **2** | ai, human, robot, intelligence | *Artificial Intelligence* |
| **3** | content, site, view, theater | *Media & Entertainment* |
| **4** | game, world, video, play | *Gaming & Virtual Reality* |

## 🚀 How to Run
1. Open the notebook in Google Colab.
2. Run the installation cell to install `kneed` and `gensim`.
3. Execute all cells to fetch the data and generate models.

## Interpretation of Results: LDA vs. K-Means
In this analysis, we applied two distinct unsupervised learning techniques to extract structure from news articles: ***Topic Modeling (LDA)*** and ***Clustering (K-Means)***. While both methods organize data, they function differently and offer unique insights.

**1. Methodological Differences:**
   - ***LDA (Latent Dirichlet Allocation):*** This is a probabilistic model. It assumes that every document is a mixture of multiple topics (e.g., an article could be 70% "AI" and 30% "Business"). It looks for groups of words that frequently appear together (co-occurrence) to define "topics."
   - ***K-Means Clustering:*** This is a geometric model. It forces every document into exactly one cluster based on distance in the vector space (using TF-IDF). It creates hard boundaries between groups.

***2. Analysis of Our Results:***
   - ***LDA Results:*** Our Coherence Score analysis showed an upward trend, suggesting that as we increased the number of topics (up to 20), the semantic consistency improved. This indicates the news dataset contains many nuanced sub-topics (e.g., "VR Gaming" vs. "PC Gaming" might be separate topics in LDA).
   - ***K-Means Results:*** The Elbow Method (KneeLocator) identified $k=13$ as the optimal number of clusters. K-Means aggregated these nuances into broader, distinct categories.

***3. Conclusion:***

The K-Means model provided the most actionable high-level categorization, successfully separating Big Tech (Cluster 1), Artificial Intelligence (Cluster 2), and Gaming (Cluster 4). However, the LDA analysis suggests that if we needed to build a granular recommendation system, we would benefit from allowing documents to have multiple tags (topics) rather than a single cluster label.
