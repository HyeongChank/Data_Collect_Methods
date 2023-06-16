import nltk
nltk.download('reuters')
nltk.download('punkt')
from nltk.corpus import reuters
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
import numpy as np
import pickle

# 영어 불용어 가져오기
stop_words = set(stopwords.words('english'))

# reuters 코퍼스의 모든 파일 id 가져오기
files = reuters.fileids()

# 문서와 레이블을 분리
documents, labels = [], []
for file in files:
    # 문서를 토큰화하고, 불용어 제거 후, 문서와 레이블을 리스트에 추가합니다.
    tokenized_doc = word_tokenize(reuters.raw(file))
    filtered_doc = [word.lower() for word in tokenized_doc if word not in stop_words]
    documents.append(' '.join(filtered_doc))  # sklearn의 CountVectorizer는 문자열을 입력으로 받습니다.
    labels.append(reuters.categories(file)[0])

# CountVectorizer를 사용하여 문서를 벡터 형태로 변환합니다.
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# 레이블을 정수 형태로 변환합니다.
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# 데이터를 훈련 세트와 테스트 세트로 분리합니다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 그리드 검색을 위한 파라미터 그리드를 정의합니다.
# param_grid = {
#     'n_estimators': [100, 200, 300],
#     'max_depth': [None, 5, 10],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4],
#     'max_features': ['auto', 'sqrt']
# }
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [None, 3],
    'min_samples_split': [1, 3],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt']
}

# 랜덤 포레스트 모델 생성
rf_model = RandomForestClassifier()

# 그리드 검색 수행
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3)
grid_search.fit(X_train, y_train)

# 최적의 모델과 파라미터 출력
print("Best Parameters:", grid_search.best_params_)
print("Best Model:", grid_search.best_estimator_)

# 최적의 모델로 테스트 데이터 평가
y_pred = grid_search.best_estimator
print("Accuracy:", accuracy_score(y_test, y_pred))