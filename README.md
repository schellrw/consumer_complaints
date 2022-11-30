# consumer_complaints
NLP with various methodologies using consumer_complaints kaggle dataset
url: https://www.kaggle.com/datasets/kaggle/us-consumer-finance-complaints

consumer_complaints_tfidf.ipynb is a jupyter notebook performing NLP with industry standard TfidfVectorizer from sklearn and product classification with several classification techniques.

consumer_complaints_Doc2Vec.ipynb is a jupyter notebook performing NLP with Gensim's Doc2Vec embedded vectors and product classification with several classification techniques.

Thus far, results using TfidfVectorizer have been superior to Doc2Vec.  An additional methodology using huggingface Transformers will also be explored.
