# Wegodang Client Project

## ๐ What is project Goal

- 1์ฐจ ํ๋ก์ ํธ๋ ํด๋ณด์ง ๋ชปํ๋ ๊ธฐ๋ฅ, ๊ธฐ์ ์คํ์ ์ ์ฉ์์ผ๋ณด๊ธฐ
- ์์๋ก๊ทธ์ธ/ํ์๊ฐ์(kakao) ๊ธฐ๋ฅ ๊ตฌํ
- AWS์ EC2, RDS, S3๋ฅผ ์ฌ์ฉํ ๋ฐฐํฌ, ๋ฐ์ดํฐ๋ฒ ์ด์ค ๊ด๋ฆฌ, ํ์ผ ์๋ก๋ ๊ธฐ๋ฅ ์ ์ฉ

## ๐ Wegodang Project Family

- F.E<br />
  [์ํ์](https://github.com/kor-sams-dev)
  [์ต์ฌํ](https://github.com/chlwogur31)
  [์์ค์](https://github.com/Ahnjungyoung)
  <br />
- B.E<br />
  [๊น์ฐ์](https://github.com/Kws1995)

## ๐๊ฐ๋ฐ ์ธ์ ๋ฐ ๊ธฐ๊ฐ

- ๊ฐ๋ฐ๊ธฐ๊ฐ<br />2022/07/04 ~ 2022/07/15
- ๊ฐ๋ฐ ์ธ์<br />ํ๋ก ํธ์๋ 3๋ช, ๋ฐฑ์๋ 1๋ช

## ๐ ์ ์ฉ ๊ธฐ์  ๋ฐ ๊ตฌํ ๊ธฐ๋ฅ

### ์ ์ฉ ๊ธฐ์ 

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"><img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"><img src="https://img.shields.io/badge/Kakao REST API-FFCD00?style=for-the-badge&logo=Kakao&logoColor=white">

## ๐ ERD

<img width="1352" alt="แแณแแณแแตแซแแฃแบ 2022-07-17 แแฉแแฎ 2 55 35" src="https://user-images.githubusercontent.com/104283159/179389591-bf1f91b9-20ef-485a-b099-1377817ddf98.png">

## ๐ ๊ตฌํ Api

### Users
#### 1. ์นด์นด์ค ์์ ๋ก๊ทธ์ธ/ํ์๊ฐ์ Api

[GET]
- FE๋ก๋ถํฐ ์นด์นด์ค ์ก์ธ์ค ํ ํฐ์ ์ ๋ฌ๋ฐ๊ธฐ
- ์ ๋ฌ๋ฐ์ ํ ํฐ์ ์นด์นด์ค Api ์๋ฒ์ ์ ์กํ์ฌ ์นด์นด์ค ์ฌ์ฉ์ ๋ฐ์ดํฐ๋ฐ๊ธฐ
- ์นด์นด์ค ์ฌ์ฉ์ ๋ฐ์ดํฐ๋ฅผ ๊ทธ๋๋ก FE์ response

[POST]
- FE๋ก๋ถํฐ ์ฌ์ฉ์ ๋ฐ์ดํฐ(kakao_id, user_name, email) ์ ๋ฌ๋ฐ๊ธฐ
- ์ ๋ฌ๋ฐ์ ๋ฐ์ดํฐ์ค kakao_id๊ฐ ์ค๋ณต๋๋ ๋ฐ์ดํฐ๊ฐ ์กด์ฌํ  ๊ฒฝ์ฐ update, ๋ก๊ทธ์ธ ๋ฉ์ธ์ง์ status 200 ๋ฐํํ๊ธฐ
- ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ createํ์ฌ ์๋ก์ด ํ์์ ๋ณด๋ฅผ ์์ฑํ๊ณ  ํ์๊ฐ์ ๋ฉ์ธ์ง์ status 201 ๋ฐํํ๊ธฐ

#### 2. ์ฌ์ฉ์ ํ๋กํ ์ ๋ณด Api

[GET]
- ๋ก๊ทธ์ธ ์ ํจ์ฑ ๊ฒ์ฌ ์งํ
- ๋ก๊ทธ์ธ๋ ํด๋น ์ ์ ์ ์ฌ์ฉ์ ํ๋กํ ์ ๋ณด์ status 200 ๋ฐํํ๊ธฐ

[POST]
- ๋ก๊ทธ์ธ ์ ํจ์ฑ ๊ฒ์ฌ ์งํ
- ์ด๋ฏธ์ง ์์ ์ FE๋ก๋ถํฐ formdata๋ก ์ด๋ฏธ์ง ํ์ผ ์ ์ก๋ฐ๊ธฐ
- ์ ์ก๋ฐ์ ํ์ผ์ s3์ ์๋ก๋ํ์ฌ url์์ฑํ๊ธฐ
- ํด๋น ์ ์ ์ ํ๋กํ ์ด๋ฏธ์ง๋ฅผ ์๋ก๋๋ url๋ก update
- ํ์ผ ์ ์ก์ ๋ฌธ์ ๊ฐ ์๋ ๊ฒฝ์ฐ ์๋ฌ ๋ฉ์ธ์ง์ status 400 ๋ฐํํ๊ธฐ
- ์๋ ฅ์ ๋ฌธ์ ๊ฐ ์๋ ๊ฒฝ์ฐ ํค ์๋ฌ ๋ฉ์ธ์ง์ status 400 ๋ฐํํ๊ธฐ

### Products
#### 1. ์นด๋ ๊ณ ๋ฆฌ ๋ฐ์ดํฐ ๋ฐํ Api
- ์นดํ๊ณ ๋ฆฌ ๋ชจ๋  ๋ฐ์ดํฐ์ status 200 ๋ฐํํ๊ธฐ

#### 2. ํ๋ฉ(์ํ) ์์ธ ๋ฐ์ดํฐ ๋ฐํ Api
- FE๋ก๋ถํฐ path parameter๋ก ํ๋ฉ(์ํ)์ id ์ ๋ฌ๋ฐ๊ธฐ
- ํด๋น id์ ํ๋ฉ(์ํ)๋ฐ์ดํฐ์ status 200 ๋ฐํํ๊ธฐ

#### 3. ํ๋ฉ(์ํ) ๋ชฉ๋ก, ์ฌ๋ผ์ด๋(์บ๋ฌ์)์ ๋ค์ด๊ฐ ํ๋ฉ(์ํ) ๋ฐ์ดํฐ ๋ฐํ Api
- FE๋ก๋ถํฐ query parameter์ (category_id, offset, limit, order) ๋ฐ์ดํฐ ์ ๋ฌ๋ฐ๊ธฐ
- ์ ๋ฌ๋ฐ์ ๋ฐ์ดํฐ๋ฅผ Q method์ ์ ์ฅํ์ฌ ํํฐ๋ง
- ํํฐ๋ง๋ ํ๋ฉ(์ํ)์ ๋ฐ์ดํฐ, status 200 ๋ฐํํ๊ธฐ

## ๐ Links

[Wadiz](https://www.wadiz.kr/web/main)

[Wegodang FrontEnd Repository](https://github.com/wecode-bootcamp-korea/34-2nd-wegodang-frontend)

[Wegodang ํ๋ก์ ํธ ํ๊ณ  - BackEnd](https://velog.io/@wsvgc95/Wegodang-Wecode-2%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0)
