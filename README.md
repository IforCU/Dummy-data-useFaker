# 파이썬의 Faker 라이브러리를 이용한 더미 데이터 생성 및 엑셀로 저장함.

## 목표

- Database Test에 필요한 더미 데이터 생성
- 생성된 데이터를 Excel에 저장하여 다른 용도로 활용 가능하게 함.

## 사용 라이브러리 Faker, openpyxl

- pip를 이용해 다음 라이브러리 설치

```bash
pip install openpyxl
pip install Faker
```

## 다양한 데이터 셋을 제공함

- 초기 설정

```python
from faker import Faker
# default 영어
# 필요하면 "ko_KR" 을 이용하면 한국 데이터로 만들 수 있음 : Faker("ko_KR")
faker = Faker()

# 기본적인 사용 방법은 간단하게 (.)를 이용하여 사용함.
name = faker.name()
```

- 기본 유저 관련

  - name() : 이름
  - image_url() : 이미지 URL
  - country() : 국적
  - city() : 도시
  - phone_number() : 전화번호
  - email() : 이메일
  - job() : 직업
  - company() : 회사이름

- 주소 관련

  - address() : 전체주소
  - street_address() : 도로명 주소
  - postcode() : 우편번호
  - state() : 주(미국)
  - locale() : 임의의 지역 설정

- 날짜 및 시간 관련

  - date() : 날짜
  - time() : 시간
  - date_time() : 날짜 및 시간
  - date_of_birth() : 생년월일
  - date_this_century() : 20세기 내에서 임의의 날짜
  - time_object() : 임의의 시간
  - date_time_between(start_date, end_date) : 주어진 범위 내에서 임의의 날짜와 시간

- 금융 관련

  - credit_card_number() : 신용카드 번호
  - credit_card_expire() : 신용카드 만료일
  - credit_card_provider() : 신용카드 발급사
  - iban() : 국제 은행 계좌 번호
  - swift() : SWIFT/BIC 코드

- 인터넷 관련

  - ipv4() : IPv4 주소
  - ipv6() : IPv6 주소
  - url() : URL
  - domain_name() : 도메인 이름

- 회사 관련

  - company() : 회사 이름
  - job() : 직업
  - bs() : 회사 슬로건

- 개인 정보 관련

  - ssn() : 사회보장번호 (미국)
  - passport_number() : 여권번호
  - profile() : 프로필 정보(이름, 주소, 이메일, 생년월일 등의 조합)

- 게시글

  - text() : 임의의 텍스트
  - sentence() : 문장
  - paragraph() : 단락

- 기타
  - boolean() : 임의의 불리언 값
  - random_number() : 임의의 숫자
  - uuid4() : UUID4
  - file_extension() : 임의의 파일 확장자
