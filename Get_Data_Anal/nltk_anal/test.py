import nltk
from nltk.corpus import reuters
from nltk import word_tokenize
from nltk import FreqDist
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from collections import Counter
import numpy as np
import pickle
# NLTK downloads
nltk.download('reuters')
nltk.download('punkt')
nltk.download('stopwords')

# 영어 불용어 가져오기
stop_words = set(stopwords.words('english'))

# reuters 코퍼스의 모든 파일 id 가져오기
# reuters.raw('test/14826') -> 해당 문서의 텍스트 반환
# print(reuters.categories('training/4282')) -> 카테고리 나옴(acq-합병)
files = reuters.fileids()

# print(files)    # training/4273 과 같은 값 출력
# 문서와 레이블을 분리
documents, labels = [], []
for file in files:
    # 문서를 토큰화하고, 불용어 제거 후, 문서와 레이블을 리스트에 추가합니다.
    tokenized_doc = word_tokenize(reuters.raw(file))
    # filtered_doc = [word for word in tokenized_doc if word not in stop_words]
    # 소문자화
    filtered_doc = [word.lower() for word in tokenized_doc if word not in stop_words]
    documents.append(filtered_doc)
    labels.append(reuters.categories(file)[0])

# Calculate label frequencies
label_freq = Counter(labels)

# Select only the documents with labels that appear more than once
filtered_documents, filtered_labels = [], []
for doc, label in zip(documents, labels):
    if label_freq[label] > 1:
        filtered_documents.append(doc)
        filtered_labels.append(label)

# Convert the documents to FreqDist objects
filtered_documents = [FreqDist(doc) for doc in filtered_documents]

# Convert to numpy arrays
filtered_documents_np = np.array(filtered_documents)
filtered_labels_np = np.array(filtered_labels)

# Split the data into training and testing sets
train_docs, test_docs, train_labels, test_labels = train_test_split(
    filtered_documents_np, filtered_labels_np, test_size=0.3, stratify=filtered_labels_np, random_state=0)

# Train the classifier
classifier = NaiveBayesClassifier.train(zip(train_docs, train_labels))

# Evaluate the classifier using the test data
print("Accuracy:", accuracy(classifier, zip(test_docs, test_labels)))

# 모델 저장하기
with open('./model/naive_bayes_classifier.pickle', 'wb') as f:
    pickle.dump(classifier, f)