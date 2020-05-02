# -*- coding: utf-8 -*-
"""dulanga_final

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ErMPEE5wJgto_rKZPMMXaDYKpyLJX8SG
"""

from __future__ import division, print_function
import pandas as pd
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.decomposition import PCA

DATASET_URL = "https://raw.githubusercontent.com/dasaCoder/FCM_TEST/master/dataset/finaldataset.csv"

dataset = pd.read_csv(DATASET_URL)
#dataset.shape
#dataset.head()

## encode dataset

Org1 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business Analysis':3,
        'Networking':4,
        'Management':5,
        'Research':6,
        'Lecturing':7,
        'Database':8,
        'Data Science':9,
        'Computer Science':10,
        'Information Technology':11,
        'Computer Architecture':12,
        'Distributed System':13,
        'Cloud Computing':14,
        'Data Structures and Algorithms':15,
        'Programming Languages':16,
        'Mathematics':17,
        'Operating Systems':18,
        'Multimedia, Animation and Graphic Design':19,
        'Cyber Security':20,
        'Information System':21,
        'Artificial Intelligence':22,
        'Bio-informatics':23,
        'Telecommunication':24,
        'Embedded System':25,
        'Marketing and E-Commerce':26,
        'E-Governance':27,
        'GIS':28,
        'HCI':29,
        'Big Data':30,
        'Human computer interaction':31,
        'Other':100 }

def endcode_record(record):
  encoded_test_data = []
  for i in record:
    if i in Org1:
      encoded_test_data.append(Org1[i])
    else: encoded_test_data.append(0)
  return encoded_test_data

def encode_for_clusters(record):
  encoded_test_data = []
  ## remove duplicates
  l = list(set(record))
  for d in Org1:
    if d in l:
      encoded_test_data.append(Org1[d])
    #else: encoded_test_data.append(0)
  return encoded_test_data

def encode_dataset(dataset):
  new_dataset = [encode_for_clusters(record) for record in dataset]  
  df = pd.DataFrame(new_dataset)
  return df.fillna(100)

## encode given dataset
encoded_df = encode_dataset(dataset.values)

processed_data = encoded_df.T
alldata = dataset
fpcs = []
U_matrix = []

for ncenters in list(range(2,11)):
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        processed_data, ncenters, 2, error=0.005, maxiter=1000, init=None)
    
    # Store fpc values for later
    fpcs.append(fpc)
    U_matrix.append(u)

fig2, ax2 = plt.subplots()
ax2.plot(np.r_[2:11], fpcs)
ax2.set_xlabel("Number of centers")
ax2.set_ylabel("Fuzzy partition coefficient")

# Opening JSON file 
fuzz_matrix = pd.read_json('https://raw.githubusercontent.com/dasaCoder/FCM_TEST/master/fuzz_matrix.json',)

cntr_final, u_final, u0, d, jm, p, fpc_final = fuzz.cluster.cmeans(processed_data, 5, m=2, error=0.005, maxiter=1000, init=fuzz_matrix.values)

u_predicted, u0, d, jm, p, fpc_predicted = fuzz.cluster.cmeans_predict(encoded_df[:1].T, cntr_final, 2, error=0.005, maxiter=1000)

def predict_cluster(record):
  u_predicted, u0, d, jm, p, fpc_predicted = fuzz.cluster.cmeans_predict(record, cntr_final, 2, error=0.005, maxiter=1000)
  pred_list = np.array(u_predicted)
  arr = np.around(pred_list,3)*100

  related_clusters = []
  cluster_count = 1
  for r in arr:
    if r[0] > 70:
      related_clusters.append(cluster_count)
    cluster_count = cluster_count + 1
  return related_clusters

def prepare_record(record):
  test_list = [[],[],[],[],[],[],[],[]]
  n = 0
  for i in record:
    test_list[n] = [i]
    n = n + 1
  return test_list

def devide_clusters(df):
  n = 0
  cluster_members = {}
  cluster_members[1] = []
  cluster_members[2] = []
  cluster_members[3] = []
  cluster_members[4] = []
  cluster_members[5] = []

  for record in df.values:
    prepared_record = prepare_record(record)
    clusters = predict_cluster(pd.DataFrame(prepared_record))
    for i in clusters:
      cluster_members[i].append(n)
    n = n + 1
  return cluster_members

#x = [[1],[5],[10],[19],[100],[100],[100],[100]]

cluster_members = devide_clusters(encoded_df)

from mlxtend.frequent_patterns import apriori, association_rules

items = ['Software Engineering',
        'Quality Assurance',
        'Business Analysis',
        'Networking',
        'Management',
        'Research',
        'Lecturing',
        'Database',
        'Data Science',
        'Computer Science',
        'Information Technology',
        'Computer Architecture',
        'Distributed System',
        'Cloud Computing',
        'Data Structures and Algorithms',
        'Programming Languages',
        'Mathematics',
        'Operating Systems',
        'Multimedia, Animation and Graphic Design',
        'Cyber Security',
        'Information System',
        'Artificial Intelligence',
        'Bio-informatics',
        'Telecommunication',
        'Embedded System',
        'Marketing and E-Commerce',
        'E-Governance',
        'GIS',
        'HCI',
        'Big Data',
        'Human computer interaction',
        'Other'  ]

encoded_vals = []
for index, row in dataset.iterrows():
    labels = {}
    uncommons = list(set(items) - set(row))
    commons = list(set(items).intersection(row))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
#print(encoded_vals[0])
ohe_df = pd.DataFrame(encoded_vals)
ohe_df = ohe_df.drop('Other',axis=1)

rules_for_cluster = {}

cluster1_data = ohe_df.loc[cluster_members[1]]
freq_items_for_cluster1 = apriori(cluster1_data, min_support=0.2, use_colnames=True)
freq_items_for_cluster1.head(7)

rules_for_cluster[1] = []
rules_for_cluster[1] = association_rules(freq_items_for_cluster1, metric="confidence", min_threshold=0.1)
rules_for_cluster[1]

cluster2_data = ohe_df.loc[cluster_members[2]]
freq_items_for_cluster2 = apriori(cluster2_data, min_support=0.1, use_colnames=True)
rules_for_cluster[2] = []
rules_for_cluster[2] = association_rules(freq_items_for_cluster2, metric="confidence", min_threshold=0.2)
rules_for_cluster[2].head()

cluster3_data = ohe_df.loc[cluster_members[3]]
freq_items_for_cluster3 = apriori(cluster3_data, min_support=0.01, use_colnames=True)
rules_for_cluster[3] = []
rules_for_cluster[3] = association_rules(freq_items_for_cluster3, metric="confidence", min_threshold=0.01)
rules_for_cluster[3].head()

cluster4_data = ohe_df.loc[cluster_members[4]]
freq_items_for_cluster4 = apriori(cluster4_data, min_support=0.1, use_colnames=True)
rules_for_cluster[4] = []
rules_for_cluster[4] = association_rules(freq_items_for_cluster4, metric="confidence", min_threshold=0.6)
rules_for_cluster[4].head()

cluster5_data = ohe_df.loc[cluster_members[5]]
freq_items_for_cluster5 = apriori(cluster5_data, min_support=0.2, use_colnames=True)
rules_for_cluster[5] = []
rules_for_cluster[5] = association_rules(freq_items_for_cluster5, metric="confidence", min_threshold=0.1)
rules_for_cluster[5].head()

import itertools

def get_apriori_suggestions(record, cluster_id):
  ## get all features of the record while removing duplicates
  full_features = list(set(record))

  all_antecedents = []
  all_consequents = []

  for i in rules_for_cluster[cluster_id]['antecedents'][:3]:
    val, = i
    all_antecedents.append(val.split(","))  
  all_antecedents = list(itertools.chain(*all_antecedents))

  for i in rules_for_cluster[cluster_id]['consequents'][:3]:
    val2, = i
    all_consequents.append(val2.split(",")) 
  all_consequents = list(itertools.chain(*all_consequents))

  return list(set(all_antecedents) - set(full_features))

get_apriori_suggestions(dataset.values[10],3)

def encode_for_apriori(row):
    encoded_list_apri = []
    labels = {}
    uncommons = list(set(items) - set(row))
    commons = list(set(items).intersection(row))
    for uc in uncommons:
      labels[uc] = 0
    for com in commons:
      labels[com] = 1
    encoded_list_apri.append(labels)
    return encoded_list_apri[0]
  
#print(encode_for_apriori(dataset.values[3]))

def get_suggestions(record):
  encoded_rec = encode_for_clusters(record)
  ## add padding
  count = 0
  if len(encoded_rec) < 8:
    len_encoded_rec = len(encoded_rec)

    while count < (8 - len_encoded_rec):
      encoded_rec.append(100)
      count = count + 1
  encoded_df_pred = pd.DataFrame(encoded_rec)
  
  cluster_list_pred = predict_cluster(encoded_df_pred)

  final_suggestions = []
  for cluster_id in cluster_list_pred:
    final_suggestions.append(get_apriori_suggestions(record,cluster_id))

  return final_suggestions

test_values = ['Software Engineering', 'Other', 'Other', 'Other', 'Other', 'Other', 'Research', 'Data Structures and Algorithms', 'Software Engineering', 'Programming Languages', 'Programming Languages', 'Software Engineering']

#print(get_suggestions(test_values))
