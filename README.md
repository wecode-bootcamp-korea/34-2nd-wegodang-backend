# Wegodang Client Project

## 🌟 What is project Goal

- 1차 프로젝트때 해보지 못했던 기능, 기술스택을 적용시켜보기
- 소셜로그인/회원가입(kakao) 기능 구현
- AWS의 EC2, RDS, S3를 사용한 배포, 데이터베이스 관리, 파일 업로드 기능 적용

## 🌟 Wegodang Project Family

- F.E<br />
  [서한샘](https://github.com/kor-sams-dev)
  [최재혁](https://github.com/chlwogur31)
  [안중영](https://github.com/Ahnjungyoung)
  <br />
- B.E<br />
  [김우식](https://github.com/Kws1995)

## 🌟개발 인원 및 기간

- 개발기간<br />2022/07/04 ~ 2022/07/15
- 개발 인원<br />프론트엔드 3명, 백엔드 1명

## 🌟 적용 기술 및 구현 기능

### 적용 기술

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"><img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"><img src="https://img.shields.io/badge/Kakao REST API-FFCD00?style=for-the-badge&logo=Kakao&logoColor=white">

## 🌟 ERD

<img width="1352" alt="스크린샷 2022-07-17 오후 2 55 35" src="https://user-images.githubusercontent.com/104283159/179389591-bf1f91b9-20ef-485a-b099-1377817ddf98.png">

## 🌟 구현 Api

### Users
#### 1. 카카오 소셜 로그인/회원가입 Api

[GET]
- FE로부터 카카오 액세스 토큰을 전달받기
- 전달받은 토큰을 카카오 Api 서버에 전송하여 카카오 사용자 데이터받기
- 카카오 사용자 데이터를 그대로 FE에 response

[POST]
- FE로부터 사용자 데이터(kakao_id, user_name, email) 전달받기
- 전달받은 데이터중 kakao_id가 중복되는 데이터가 존재할 경우 update, 로그인 메세지와 status 200 반환하기
- 존재하지 않을 경우 create하여 새로운 회원정보를 생성하고 회원가입 메세지와 status 201 반환하기

#### 2. 사용자 프로필 정보 Api

[GET]
- 로그인 유효성 검사 진행
- 로그인된 해당 유저의 사용자 프로필 정보와 status 200 반환하기

[POST]
- 로그인 유효성 검사 진행
- 이미지 수정시 FE로부터 formdata로 이미지 파일 전송받기
- 전송받은 파일을 s3에 업로드하여 url생성하기
- 해당 유저의 프로필 이미지를 업로드된 url로 update
- 파일 전송에 문제가 있는 경우 에러 메세지와 status 400 반환하기
- 입력에 문제가 있는 경우 키 에러 메세지와 status 400 반환하기

### Products
#### 1. 카레고리 데이터 반환 Api
- 카테고리 모든 데이터와 status 200 반환하기

#### 2. 펀딩(상품) 상세 데이터 반환 Api
- FE로부터 path parameter로 펀딩(상품)의 id 전달받기
- 해당 id의 펀딩(상품)데이터와 status 200 반환하기

#### 3. 펀딩(상품) 목록, 슬라이더(캐러셀)에 들어갈 펀딩(상품) 데이터 반환 Api
- FE로부터 query parameter에 (category_id, offset, limit, order) 데이터 전달받기
- 전달받은 데이터를 Q method에 저장하여 필터링
- 필터링된 펀딩(상품)의 데이터, status 200 반환하기

## 🌟 Links

[Wadiz](https://www.wadiz.kr/web/main)

[Wegodang FrontEnd Repository](https://github.com/wecode-bootcamp-korea/34-2nd-wegodang-frontend)

[Wegodang 프로젝트 회고 - BackEnd](https://velog.io/@wsvgc95/Wegodang-Wecode-2%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0)
