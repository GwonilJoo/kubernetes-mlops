# kubernetes-mlops

kubernetest를 활용해서 classification 모델의 hyperparameter 실험을 수행하는 API 개발

### hypyerparamter 목록

- learning rate
- batch size
- epochs

## Setup

### 실행 환경
```
macos M2
docker
kubernetes (docker desktop)
```

### database pod 및 service

```
kubectl apply -f kubernetes/dataset.yml
```

### 패키지 설치

```
pipenv install
```

## Execute

### application 실행

```
pipenv run python main.py
```

### 실행 확인

```
localhost:8000/healthcheck
```

## Swagger

```
localhost:8000/docs
```

## 다음 과제

- [ ] Inference 기능 추가
- [ ] API Application 이미지 빌드
- [ ] AWS EKS 환경 적용
- [ ] Model 및 hyperparamter 추가
