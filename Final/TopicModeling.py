import pandas as pd
import  numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import random

reviews_datasets = pd.read_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Monkey.csv')
reviews_datasets = reviews_datasets.head(20000)
reviews_datasets.dropna()

reviews_datasets.head()

count_vect = CountVectorizer(max_df=0.8, min_df=2, stop_words='english')
doc_term_matrix = count_vect.fit_transform(reviews_datasets['Education FOS 1'].values.astype('U'))


LDA = LatentDirichletAllocation(n_components=5, random_state=42)
LDA.fit(doc_term_matrix)

for i in range(10):
    random_id = random.randint(0,len(count_vect.get_feature_names()))
    print(count_vect.get_feature_names()[random_id])

first_topic = LDA.components_[0]
top_topic_words = first_topic.argsort()[-10:]

for i in top_topic_words:
    print(count_vect.get_feature_names()[i])

for i,topic in enumerate(LDA.components_):
    print(f'Top 10 words for topic #{i}:')
    print([count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')

topic_values = LDA.transform(doc_term_matrix)
topic_values.shape

reviews_datasets['Topic'] = topic_values.argmax(axis=1)

print(reviews_datasets.head(100))