import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from sklearn import svm
from sklearn.metrics import classification_report

trainData = pd.read_csv(r'E:\DinuData\dd\train.csv')
testData = pd.read_csv(r'E:\DinuData\dd\test.csv')

print(trainData.sample(frac=1).head(5))

# Create feature vectors
vectorizer = TfidfVectorizer(min_df = 5,
                             max_df = 0.8,
                             sublinear_tf = True,
                             use_idf = True)
train_vectors = vectorizer.fit_transform(trainData['text'])
test_vectors = vectorizer.transform(testData['text'])

# Perform classification with SVM, kernel=linear
classifier_linear = svm.SVC(kernel='linear', probability = True)
t0 = time.time()
classifier_linear.fit(train_vectors, trainData['label'])
t1 = time.time()
prediction_linear = classifier_linear.predict(test_vectors)
t2 = time.time()
time_linear_train = t1-t0
time_linear_predict = t2-t1
# results
print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
report = classification_report(testData['label'], prediction_linear, output_dict=True)
print('positive: ', report['positive'])
print('negative: ', report['negative'])



review = """I went into this film expecting/hoping for a sleazy drive-in style slice of seventies exploitation, but what I got was more of a bizarre pseudo western with far too much talking and not enough action. It's clear that this film was made on a budget; the locations are drab and poorly shot, while the acting leaves a lot to be desired also. The plot focuses on a trio of robbers (a father and two sons) that steal a load of gold after killing some miners. They come across a cabin inhabited by a young girl and her stepmother...and all this is told in flashbacks by the young girl, currently residing in an asylum. It's clear that directors Louis Leahman and William Sachs thought they were making something really shocking; but despite its best efforts, South of Hell Mountain is just too boring to shock the viewer. The film drones on for about eighty minutes and most of it consists of boring characters spouting off boring and long-winded dialogue. The only good thing I have to say about the film is with regards to the music; which is good in places. The ending is the only other good thing about the movie; and that's only because it's the last thing that happens. I wouldn't recommend anyone bothers tracking this down...there was much better trash made in the seventies."""
review_vector = vectorizer.transform([review]) # vectorizing

print(classifier_linear.predict(review_vector))
print(classifier_linear.predict_proba(review_vector))