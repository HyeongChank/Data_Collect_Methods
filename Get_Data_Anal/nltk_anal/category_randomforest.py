import nltk
from nltk.corpus import reuters
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
import numpy as np
import pickle
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('reuters')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


# 영어 불용어 가져오기
stop_words = set(stopwords.words('english'))
# reuters 코퍼스의 모든 파일 id 가져오기
files = reuters.fileids()
# 어간(형태소 중 단어의 핵심 부분) 추출기와 표제어(단어의 사전적 기본 형태) 추출기를 생성
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
# 문서와 레이블을 분리
documents, labels = [], []
for file in files:
    # 문서를 토큰화하고, 불용어 제거 후, 문서와 레이블을 리스트에 추가
    tokenized_doc = word_tokenize(reuters.raw(file))
    filtered_doc = [word.lower() for word in tokenized_doc if word not in stop_words]
    # documents.append(' '.join(filtered_doc))  # 문자열 입력받음
    stemmed_doc = [stemmer.stem(word) for word in filtered_doc]
    lemmatized_doc = [lemmatizer.lemmatize(word) for word in stemmed_doc]
    documents.append(' '.join(lemmatized_doc))
    labels.append(reuters.categories(file)[0])

# CountVectorizer를 사용하여 문서를 벡터 형태로 변환
# randomforest는 2차원 배열 필요
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# 레이블을 정수 형태로 변환합니다.
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# 데이터를 훈련 세트와 테스트 세트로 분리합니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

classifier = RandomForestClassifier(n_estimators=200)
classifier.fit(X_train, y_train)

# 테스트 데이터로 분류기를 평가
y_pred = classifier.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 모델 저장하기
with open('./model/random_forest_classifier.pickle', 'wb') as f:
    pickle.dump(classifier, f)
