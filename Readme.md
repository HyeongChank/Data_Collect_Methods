# 다음, 네이버 기사 크롤링, 분석
## 기간별 키워드 노출 횟수 나타내는 그래프와 wordcloud 이미지 생성

## Category 분류(reuters 예제)
- NaiveBayesClassifier 사용 정확도 20% 미만
- RandomForestClassifier 사용 정확도 80%
- RandomForestClassifier 사용 정확도 82%(어간, 표제어 추출)
- GridSearchCV 는 너무 오래걸려 돌려보지 못함 다시 해봐야 함

- requirements
    - pip freeze > requirements.txt
    - pip install -r requirements.txt


- chromedriver 설치 시 주의사항
chrome 버전이랑 맞춰야 함
